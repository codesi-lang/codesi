import os
import sys
from codesi.lexer.lexer import CodesiLexer
from codesi.parser.parser import CodesiParser
from codesi.interpreter.interpreter import CodesiInterpreter
from codesi.features.jaadu import jaadu_system
from codesi.exceptions import (
    CodesiError, 
    ReturnException, 
    BreakException, 
    ContinueException,
)

def run_codesi(code: str, debug=False, jaadu_mode=False):
    """Run Codesi code"""
    try:
        # Apply auto-correction only if JAADU mode is enabled
        if jaadu_mode:
            fixed_code, fixes = jaadu_system.auto_fix_code(code)
            if fixes:
                print("JAADU Auto-Corrections:")
                for wrong, correct in fixes:
                    print(f"   '{wrong}' -> '{correct}'")
                print()
            code = fixed_code
        
        lexer = CodesiLexer(code)
        tokens = lexer.tokenize()
        
        if debug:
            print("=== TOKENS ===")
            for token in tokens:
                print(f"{token.type.name}: {token.value}")
            print()
        
        parser = CodesiParser(tokens)
        ast = parser.parse()
        
        if debug:
            print("=== AST ===")
            print(ast)
            print()
        
        interpreter = CodesiInterpreter(jaadu_mode=jaadu_mode)
        interpreter.interpret(ast)
        
    except SyntaxError as e:
        print(f"Syntax Error: {e}")
        return False
    except CodesiError as e:
        print(f"Codesi Runtime Error: {e.message}")
        if hasattr(e, 'suggestion') and e.suggestion:
            print(f"Suggestion: {e.suggestion}")
        return False
    except BreakException:
        print("Codesi Error: 'break' sirf loop ke andar use kar sakte hain")
        return False
    except ContinueException:
        print("Codesi Error: 'continue' sirf loop ke andar use kar sakte hain")
        return False
    except Exception as e:
        print(f"Error: {e}")
        if debug:
            import traceback
            traceback.print_exc()
        return False
    
    return True

def run_file(filename: str, debug=False, jaadu_mode=False):
    """Run a Codesi file (.cds)"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            code = f.read()
        
        if not debug:
            mode_info = " (JAADU Mode)" if jaadu_mode else ""
            print(f"Running {filename}...{mode_info}")
            print("-" * 50)
        
        success = run_codesi(code, debug, jaadu_mode)
        
        if not debug:
            print("-" * 50)
            if success:
                print("Program completed successfully")
            else:
                print("Program terminated with errors")
        
        return success
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' nhi mila")
        return False
    except Exception as e:
        print(f"File padhne mein error: {e}")
        return False