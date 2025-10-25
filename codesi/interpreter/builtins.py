import os
import json
import math
import time
import random
import shutil
from typing import Any
from ..exceptions import CodesiError, ReturnException, BreakException, ContinueException


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def _to_string(value):
    """Convert value to string representation"""
    if isinstance(value, bool):
        return 'sach' if value else 'jhooth'
    elif value is None:
        return 'khaali'
    elif isinstance(value, list):
        return '[' + ', '.join(_to_string(v) for v in value) + ']'
    elif isinstance(value, dict):
        items = [f'{k}: {_to_string(v)}' for k, v in value.items()]
        return '{' + ', '.join(items) + '}'
    return str(value)

def _get_type_name(value):
    """Get type name of a value"""
    from .runtime import CodesiFunction, CodesiClass, CodesiObject
    
    if isinstance(value, bool):
        return 'sach_jhooth'
    elif isinstance(value, int):
        return 'Integer'
    elif isinstance(value, float):
        return 'Float/Decimal'
    elif isinstance(value, str):
        return 'shabd'
    elif isinstance(value, list):
        return 'array'
    elif isinstance(value, dict):
        return 'object'
    elif isinstance(value, CodesiFunction):
        return 'karya'
    elif isinstance(value, CodesiClass):
        return 'class'
    elif isinstance(value, CodesiObject):
        return 'instance'
    elif value is None:
        return 'khaali'
    return 'unknown'

# ============================================================================
# BUILTIN IMPLEMENTATIONS
# ============================================================================

def _builtin_print(*args):
    """Built-in print function"""
    output = ' '.join(_to_string(arg) for arg in args)
    print(output)
    return None

def _builtin_input(prompt=""):
    """Built-in input function - returns string"""
    if prompt:
        return input(str(prompt))
    return input()

def _builtin_input_float(prompt=""):
    """Built-in input function - returns float"""
    try:
        if prompt:
            return float(input(str(prompt)))
        return float(input())
    except ValueError:
        from ..exceptions import CodesiError
        raise CodesiError("Ye parse nahi kar sake - valid float/decimal dalo")

def _builtin_input_int(prompt=""):
    """Built-in input function - returns integer"""
    try:
        if prompt:
            return int(input(str(prompt)))
        return int(input())
    except ValueError:
        from ..exceptions import CodesiError
        raise CodesiError("Ye parse nahi kar sake - valid integer dalo")

def _builtin_int_bnao(x):
    """Convert to int - handle floats gracefully"""
    if isinstance(x, str):
        try:
            return int(float(x))
        except (ValueError, TypeError):
            from ..exceptions import CodesiError
            raise CodesiError(f"'{x}' ko integer mein convert nahi kar sake")
    return int(x)

def _builtin_float_bnao(x):
    """Convert to float - handle strings gracefully"""
    try:
        return float(x) if x is not None else 0
    except (ValueError, TypeError):
        from ..exceptions import CodesiError
        raise CodesiError(f"'{x}' ko float/decimal mein convert nahi kar sake")

def _file_padho(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        from ..exceptions import CodesiError
        raise CodesiError(f"File padh nahi sake: {str(e)}")

def _file_likho(path, content):
    try:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(str(content))
        return True
    except Exception as e:
        from ..exceptions import CodesiError
        raise CodesiError(f"File likh nahi sake: {str(e)}")

def _file_append(path, content):
    try:
        with open(path, 'a', encoding='utf-8') as f:
            f.write(str(content))
        return True
    except Exception as e:
        from ..exceptions import CodesiError
        raise CodesiError(f"File append nahi kar sake: {str(e)}")

def _builtin_import(filepath, interpreter_instance):
    """Import another Codesi file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            code = f.read()
        
        from ..lexer.lexer import CodesiLexer
        from ..parser.parser import CodesiParser
        
        lexer = CodesiLexer(code)
        tokens = lexer.tokenize()
        parser = CodesiParser(tokens)
        ast = parser.parse()
        
        # Execute in the context of the provided interpreter instance
        for statement in ast.statements:
            interpreter_instance.visit(statement)
        
        return True
    except Exception as e:
        from ..exceptions import CodesiError
        raise CodesiError(f"Import failed: {str(e)}")

# ============================================================================
# MAIN BUILTINS FUNCTION
# ============================================================================

def get_builtins(interpreter_instance):
    """
    Returns dictionary of all builtin functions
    NOTE: interpreter_instance pass karna MUST for import_karo
    """
    from ..features.timemachine import time_machine
    from ..features.samjho import samjho_system
    
    
    def _time_machine_on(max=100):
        time_machine.enable(max_snapshots=max)
        return None
    
    def _peeche(steps=1):
        return interpreter_instance._time_travel_back(steps)
    
    def _aage(steps=1):
        return interpreter_instance._time_travel_forward(steps)
    
    def _timeline():
        print(time_machine.show_all_steps())
        return None
    
    
    def _samjhao_on():
        samjho_system.enable()
        return "  Samjhao mode activated! Har step explain hoga."
    
    def _samjhao_off():
        samjho_system.disable()
        return "  Samjhao mode deactivated!"
    
    def _samjhao():
        print(samjho_system.get_explanation())
        return None
    
   
    return {
        # Import function
        'import_karo': lambda filepath: _builtin_import(filepath, interpreter_instance),
        
        # Output functions
        'likho': _builtin_print,
        
        # Time Machine functions
        'time_machine_status': lambda: time_machine.status(),
        'time_machine_on': _time_machine_on,
        'time_machine_off': lambda: time_machine.disable(),
        'peeche': _peeche,
        'aage': _aage,
        'timeline': _timeline,
        
        # Samjhao functions
        'samjhao_on': _samjhao_on,
        'samjhao_off': _samjhao_off,
        'samjhao': _samjhao,
        
        # Input functions
        'input_lo': _builtin_input,
        'float_lo': _builtin_input_float,
        'int_lo': _builtin_input_int,
        
        # Math functions
        'math_absolute': abs,
        'math_square': math.sqrt,
        'math_power': pow,
        'math_random': lambda a, b: random.randint(a, b),
        'math_niche': math.floor,
        'math_upar': math.ceil,
        'math_gol': round,
        'math_sin': math.sin,
        'math_cos': math.cos,
        'math_tan': math.tan,
        'math_log': math.log,
        'math_exp': math.exp,
        
        # Type functions
        'type_of': _get_type_name,
        'prakar': _get_type_name,
        'string_hai': lambda x: isinstance(x, str),
        'array_hai': lambda x: isinstance(x, list),
        'int_hai': lambda x: isinstance(x, int),
        'float_hai': lambda x: isinstance(x, float) and not isinstance(x, bool),
        'bool_hai': lambda x: isinstance(x, bool),
        'obj_hai': lambda x: isinstance(x, dict),
        
        # Conversion functions
        'string_bnao': str,
        'float_bnao': _builtin_float_bnao,
        'int_bnao': _builtin_int_bnao,
        'bool_bnao': bool,
        
        # Utility functions
        'lambai': len,
        'range': lambda start, end=None: list(range(start, end) if end else range(start)),
        'repeatkr': lambda s, n: s * n,
        
        # File operations
        'file_padho': _file_padho,
        'file_likho': _file_likho,
        'file_append': _file_append,
        'file_hai': os.path.exists,
        'file_delete': os.remove,
        'file_copy': lambda src, dst: shutil.copy(src, dst),
        'file_move': lambda src, dst: shutil.move(src, dst),
        'file_size': lambda path: os.path.getsize(path),
        'dir_banao': os.makedirs,
        'dir_list': os.listdir,
        
        # JSON operations
        'json_parse': json.loads,
        'json_stringify': lambda obj: json.dumps(obj),
        
        # Date/Time functions
        'time_now': time.time,
        'time_sleep': time.sleep,
    }