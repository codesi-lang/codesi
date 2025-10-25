from typing import List, Optional, Union, Any
from ..lexer.tokens import Token, TokenType
from .ast_nodes import *

class CodesiParser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0
    
    def current_token(self) -> Token:
        if self.pos < len(self.tokens):
            return self.tokens[self.pos]
        return self.tokens[-1]
    
    def peek(self, offset=1) -> Token:
        pos = self.pos + offset
        if pos < len(self.tokens):
            return self.tokens[pos]
        return self.tokens[-1]
    
    def advance(self):
        if self.pos < len(self.tokens) - 1:
            self.pos += 1
    
    def expect(self, token_type: TokenType) -> Token:
        token = self.current_token()
        if token.type != token_type:
            # Create a reverse map from TokenType to the keyword string
            from ..lexer.lexer import CodesiLexer
            keyword_map = {v: k for k, v in CodesiLexer("").keywords.items()}

            # Add symbols to the map
            symbol_map = {
                TokenType.PAREN_KHOLO: '(', TokenType.PAREN_BANDO: ')',
                TokenType.KHOLO: '{', TokenType.BANDO: '}',
                TokenType.BRACKET_KHOLO: '[', TokenType.BRACKET_BANDO: ']',
                TokenType.DEDO: '=', TokenType.SEMICOLON: ';',
                TokenType.COMMA: ',', TokenType.DOT: '.', TokenType.COLON: ':',
                TokenType.ARROW: '->'
            }
            keyword_map.update(symbol_map)

            # Get the display text for the token we got
            got = f"'{token.value}'" if token.value is not None else token.type.name

            # Get the display text for the token we expected
            expected = f"'{keyword_map.get(token_type)}'" if token_type in keyword_map else token_type.name
            
            raise SyntaxError(f"Line {token.line} par {expected} ki ummeed thi, lekin {got} mil gaya.")
        self.advance()
        return token
    
    def parse(self) -> Program:
        statements = []
        while self.current_token().type != TokenType.EOF:
            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)
        return Program(statements)
    
    def parse_statement(self) -> Optional[ASTNode]:
        token = self.current_token()
        
        if token.type == TokenType.SEMICOLON:
            self.advance()
            return None
        
        if token.type == TokenType.EOF:
            return None
        
        if token.type == TokenType.AGAR:
            return self.parse_if_statement()
        elif token.type == TokenType.JABTAK:
            return self.parse_while_loop()
        elif token.type == TokenType.KARO:
            return self.parse_do_while_loop()
        elif token.type == TokenType.HAR:
            return self.parse_har_loop()
        elif token.type == TokenType.KARYA:
            return self.parse_function_def()
        elif token.type == TokenType.CLASS:
            return self.parse_class_def()
        elif token.type == TokenType.VAPAS:
            return self.parse_return_statement()
        elif token.type == TokenType.CONST:
            self.advance()
            name = self.expect(TokenType.IDENTIFIER).value
            self.expect(TokenType.DEDO)
            value = self.parse_expression()
            self.skip_semicolon()
            return ConstDeclaration(name, value)
        elif token.type == TokenType.BREAK:
            self.advance()
            self.skip_semicolon()
            return BreakStatement()
        elif token.type == TokenType.CONTINUE:
            self.advance()
            self.skip_semicolon()
            return ContinueStatement()
        elif token.type == TokenType.TRY:
            return self.parse_try_catch()
        elif token.type == TokenType.THROW:
            return self.parse_throw_statement()
        elif token.type == TokenType.IDENTIFIER:
            # Check if it's old syntax: x ke liye arr mein
            if token.type == TokenType.IDENTIFIER:
             # Check if it's switch-case: var ke case mein
                if (self.peek().type == TokenType.KE and 
                    self.peek(2).type == TokenType.CASE):
                    return self.parse_switch_case()
                else:
                    expr = self.parse_expression()
                    self.skip_semicolon()
                    return expr
        
        expr = self.parse_expression()
        self.skip_semicolon()
        return expr
    
    def skip_semicolon(self):
        if self.current_token().type == TokenType.SEMICOLON:
            self.advance()
    
    def parse_if_statement(self) -> IfStatement:
        self.expect(TokenType.AGAR)
        self.expect(TokenType.PAREN_KHOLO)
        condition = self.parse_expression()
        self.expect(TokenType.PAREN_BANDO)
        then_block = self.parse_block()
        
        elif_blocks = []
        while self.current_token().type == TokenType.YA_PHIR:
            self.advance()
            self.expect(TokenType.PAREN_KHOLO)
            elif_cond = self.parse_expression()
            self.expect(TokenType.PAREN_BANDO)
            elif_body = self.parse_block()
            elif_blocks.append((elif_cond, elif_body))
        
        else_block = None
        if self.current_token().type == TokenType.NAHI_TO:
            self.advance()
            else_block = self.parse_block()
        
        return IfStatement(condition, then_block, elif_blocks, else_block)
    
    def parse_while_loop(self) -> WhileLoop:
        self.expect(TokenType.JABTAK)
        self.expect(TokenType.PAREN_KHOLO)
        condition = self.parse_expression()
        self.expect(TokenType.PAREN_BANDO)
        body = self.parse_block()
        return WhileLoop(condition, body)
    
    def parse_do_while_loop(self) -> DoWhileLoop:
        self.expect(TokenType.KARO)
        body = self.parse_block()
        self.expect(TokenType.JABTAK)
        self.expect(TokenType.PAREN_KHOLO)
        condition = self.parse_expression()
        self.expect(TokenType.PAREN_BANDO)
        self.skip_semicolon()
        return DoWhileLoop(body, condition)
    
    def parse_switch_case(self) -> SwitchCase:
        expr_name = self.expect(TokenType.IDENTIFIER).value
        expr = Identifier(expr_name)
        self.expect(TokenType.KE)
        self.expect(TokenType.CASE)
        self.expect(TokenType.MEIN)
        self.expect(TokenType.KHOLO)
        
        cases = []
        default_case = None
        
        while self.current_token().type != TokenType.BANDO:
            if self.current_token().type == TokenType.DEFAULT:
                self.advance()
                self.expect(TokenType.ARROW)
                default_stmt = self.parse_statement()
                default_case = [default_stmt] if default_stmt else []
                self.skip_semicolon()
            elif self.current_token().type in [TokenType.SHABD, TokenType.SANKHYA]:
                case_value = self.parse_primary()
                self.expect(TokenType.ARROW)
                case_stmt = self.parse_statement()
                cases.append((case_value, [case_stmt] if case_stmt else []))
                self.skip_semicolon()
            else:
                break
        
        self.expect(TokenType.BANDO)
        return SwitchCase(expr, cases, default_case)
    
    def parse_har_loop(self) -> Union[ForLoop, ForEachLoop]:
        """
        Syntax variations:
        1. har i se 0 tak 5 { ... }           // Traditional for loop
        2. har item mein array { ... }         // ForEach loop
        3. har (i se 0 tak 5) { ... }         // With parens
        """
        self.expect(TokenType.HAR)
        
        # Get loop variable
        var = self.expect(TokenType.IDENTIFIER).value
        
        # Check loop type

        if self.current_token().type == TokenType.KE:
            self.advance()
            self.expect(TokenType.LIYE)
            
            # Check if paren follows (traditional for) or expression (foreach)
            if self.current_token().type == TokenType.PAREN_KHOLO:
                # Traditional: har i ke liye (0 se 3 tak)
                self.advance()
                start = self.parse_expression()
                self.expect(TokenType.SE)
                end = self.parse_expression()
                self.expect(TokenType.TAK)
                self.expect(TokenType.PAREN_BANDO)
                body = self.parse_block()
                return ForLoop(var, start, end, body)
            else:
                # ForEach: har fruit ke liye fruits mein
                iterable = self.parse_expression()
                if self.current_token().type == TokenType.MEIN:
                    self.advance()
                body = self.parse_block()
                return ForEachLoop(var, iterable, body)
        
        elif self.current_token().type == TokenType.SE:
            self.advance()
            start = self.parse_expression()
            self.expect(TokenType.TAK)
            end = self.parse_expression()
            body = self.parse_block()
            return ForLoop(var, start, end, body)
        
        elif self.current_token().type == TokenType.MEIN:
            self.advance()
            iterable = self.parse_expression()
            body = self.parse_block()
            return ForEachLoop(var, iterable, body)
        
        else:
            raise SyntaxError(f"Line {self.current_token().line} par loop variable ke baad 'ke liye', 'se', ya 'mein' aana chahiye tha.")
        
    def parse_old_for_loop(self) -> Union[ForLoop, ForEachLoop]:
        """
        Old syntax (still supported):
        x ke liye arr mein { ... }
        """
        var = self.expect(TokenType.IDENTIFIER).value
        self.expect(TokenType.KE)
        self.expect(TokenType.LIYE)
        iterable = self.parse_expression()
        
        if self.current_token().type == TokenType.MEIN:
            self.advance()
        
        body = self.parse_block()
        return ForEachLoop(var, iterable, body)

    def parse_function_def(self) -> FunctionDef:
        self.expect(TokenType.KARYA)
        name = self.expect(TokenType.IDENTIFIER).value
        
        self.expect(TokenType.PAREN_KHOLO)
        parameters = self.parse_parameter_list()
        self.expect(TokenType.PAREN_BANDO)
        
        return_type = None
        if self.current_token().type == TokenType.ARROW:
            self.advance()
            return_type = self.current_token().value
            self.advance()
        
        body = self.parse_block()
        return FunctionDef(name, parameters, body, return_type)
    
    def parse_parameter_list(self) -> List[tuple]:
        params = []
        while self.current_token().type != TokenType.PAREN_BANDO:
            is_variadic = False
            if self.current_token().type == TokenType.ELLIPSIS:
                self.advance()
                is_variadic = True
            
            if self.current_token().type == TokenType.IDENTIFIER:
                name = self.current_token().value
                self.advance()
                
                type_annotation = None
                default_value = None
                
                if self.current_token().type == TokenType.COLON:
                    self.advance()
                    type_annotation = self.current_token().value
                    self.advance()
                
                if self.current_token().type == TokenType.DEDO:
                    self.advance()
                    default_value = self.parse_expression()
                
                # Always return 4-tuple for consistency
                params.append((name, type_annotation, default_value, is_variadic))
            
            if self.current_token().type == TokenType.COMMA:
                self.advance()
            elif self.current_token().type != TokenType.PAREN_BANDO:
                break
        
        return params
   
    def parse_class_def(self) -> ClassDef:
        self.expect(TokenType.CLASS)
        name = self.expect(TokenType.IDENTIFIER).value
        
        parent = None
        if self.current_token().type == TokenType.EXTENDS:
            self.advance()
            parent = self.expect(TokenType.IDENTIFIER).value
        
        self.expect(TokenType.KHOLO)
        
        constructor = None
        methods = []
        
        static_methods = []  

        while self.current_token().type != TokenType.BANDO:
            if self.current_token().type == TokenType.BANAO:
                constructor = self.parse_constructor()
            elif self.current_token().type == TokenType.STATIC:
                self.advance()  
                method = self.parse_function_def()
                static_methods.append(method)
            elif self.current_token().type == TokenType.KARYA:
                methods.append(self.parse_function_def())
            else:
                self.advance()
        
        self.expect(TokenType.BANDO)
        return ClassDef(name, parent, methods, constructor, static_methods)  
    
    def parse_constructor(self) -> FunctionDef:
        self.expect(TokenType.BANAO)
        self.expect(TokenType.PAREN_KHOLO)
        parameters = self.parse_parameter_list()
        self.expect(TokenType.PAREN_BANDO)
        body = self.parse_block()
        return FunctionDef('banao', parameters, body)
    
    def parse_return_statement(self) -> ReturnStatement:
        self.expect(TokenType.VAPAS)
        value = None
        if self.current_token().type not in [TokenType.SEMICOLON, TokenType.BANDO]:
            value = self.parse_expression()
        self.skip_semicolon()
        return ReturnStatement(value)
    
    def parse_try_catch(self) -> TryCatch:
        self.expect(TokenType.TRY)
        try_block = self.parse_block()
        
        catch_var = None
        catch_block = []
        if self.current_token().type == TokenType.CATCH:
            self.advance()
            self.expect(TokenType.PAREN_KHOLO)
            catch_var = self.expect(TokenType.IDENTIFIER).value
            self.expect(TokenType.PAREN_BANDO)
            catch_block = self.parse_block()
        
        finally_block = None
        if self.current_token().type == TokenType.FINALLY:
            self.advance()
            finally_block = self.parse_block()
        
        return TryCatch(try_block, catch_var, catch_block, finally_block)
    
    def parse_throw_statement(self) -> ThrowStatement:
        self.expect(TokenType.THROW)
        value = self.parse_expression()
        self.skip_semicolon()
        return ThrowStatement(value)
    
    def parse_block(self) -> List[ASTNode]:
        if self.current_token().type != TokenType.KHOLO:
            stmt = self.parse_statement()
            return [stmt] if stmt else []
        
        self.expect(TokenType.KHOLO)
        statements = []
        while self.current_token().type not in [TokenType.BANDO, TokenType.EOF]:
            stmt = self.parse_statement()
            if stmt:
                statements.append(stmt)
        
        if self.current_token().type == TokenType.BANDO:
            self.expect(TokenType.BANDO)
        
        return statements
    
    def parse_expression(self) -> ASTNode:
        return self.parse_ternary()
    
    def parse_ternary(self) -> ASTNode:
        expr = self.parse_logical_or()
        
        if self.current_token().type == TokenType.QUESTION:
            self.advance()
            true_val = self.parse_expression()
            self.expect(TokenType.COLON)
            false_val = self.parse_expression()
            return TernaryOp(expr, true_val, false_val)
        
        return expr
    
    def parse_logical_or(self) -> ASTNode:
        left = self.parse_logical_and()
        
        while self.current_token().type == TokenType.YA:
            op = self.current_token().type
            self.advance()
            right = self.parse_logical_and()
            left = BinaryOp(left, op, right)
        
        return left
    
    def parse_logical_and(self) -> ASTNode:
        left = self.parse_equality()
        
        while self.current_token().type == TokenType.AUR:
            op = self.current_token().type
            self.advance()
            right = self.parse_equality()
            left = BinaryOp(left, op, right)
        
        return left
    
    def parse_equality(self) -> ASTNode:
        left = self.parse_comparison()
        
        while self.current_token().type in [TokenType.BARABAR, TokenType.NAHI_BARABAR]:
            op = self.current_token().type
            self.advance()
            right = self.parse_comparison()
            left = BinaryOp(left, op, right)
        
        return left
    
    def parse_comparison(self) -> ASTNode:
        left = self.parse_term()
        
        while self.current_token().type in [TokenType.CHOTA, TokenType.BADA, 
                                             TokenType.CHOTA_BARABAR, TokenType.BADA_BARABAR]:
            op = self.current_token().type
            self.advance()
            right = self.parse_term()
            left = BinaryOp(left, op, right)
        
        return left
    
    def parse_term(self) -> ASTNode:
        left = self.parse_factor()
        
        while self.current_token().type in [TokenType.JODA, TokenType.GHATAO]:
            op = self.current_token().type
            self.advance()
            
            # CHECK: If next is assignment, this is invalid
            if self.current_token().type == TokenType.DEDO:
                raise SyntaxError(
                    f"Line {self.current_token().line} par galat assignment hai.\n"
                    f"   Error: Expression 'x - y' ko assign nahi kar sakte\n"
                    f"   Hint: Pehle variable mein result store karo:\n"
                    f"         result = x - y\n"
                    f"         result = value"
                )
            
            right = self.parse_factor()
            left = BinaryOp(left, op, right)
        
        return left
    
    def parse_factor(self) -> ASTNode:
        left = self.parse_power()
        
        while self.current_token().type in [TokenType.GUNA, TokenType.BHAG, TokenType.MODULO]:
            op = self.current_token().type
            self.advance()
            right = self.parse_power()
            left = BinaryOp(left, op, right)
        
        return left
    
    def parse_power(self) -> ASTNode:
        left = self.parse_unary()
        
        if self.current_token().type == TokenType.POWER:
            self.advance()
            right = self.parse_power()
            return BinaryOp(left, TokenType.POWER, right)
        
        return left
    
    def parse_unary(self) -> ASTNode:
        if self.current_token().type in [TokenType.GHATAO, TokenType.NAHI]:
            op = self.current_token().type
            self.advance()
            operand = self.parse_unary()
            return UnaryOp(op, operand)
        
        return self.parse_postfix()
    
    def parse_postfix(self) -> ASTNode:
        expr = self.parse_primary()
        
        while True:
            if self.current_token().type == TokenType.PAREN_KHOLO:
                self.advance()
                args = self.parse_argument_list()
                self.expect(TokenType.PAREN_BANDO)
                expr = FunctionCall(expr, args)
            elif self.current_token().type == TokenType.BRACKET_KHOLO:
                self.advance()
                index = self.parse_expression()
                self.expect(TokenType.BRACKET_BANDO)
                
                # Check for assignment
                if self.current_token().type == TokenType.DEDO:
                    self.advance()
                    value = self.parse_expression()
                    return IndexAssignment(expr, index, value)
                
                expr = IndexAccess(expr, index)
            elif self.current_token().type == TokenType.DOT:
                self.advance()
                member = self.expect(TokenType.IDENTIFIER).value
                
                # Check for member assignment
                if self.current_token().type == TokenType.DEDO:
                    self.advance()
                    value = self.parse_expression()
                    return MemberAssignment(expr, member, value)
                
                expr = MemberAccess(expr, member)
            # ADD THIS: Detect invalid assignment attempts
            elif self.current_token().type == TokenType.DEDO:
                # If we reach here, it's an invalid assignment target
                raise SyntaxError(
                    f"Line {self.current_token().line} par galat assignment hai.\n"
                    f"   Hint: Assignment sirf variables, array[index], ya object.property pe ho sakti hai\n"
                    f"   Example: x = 5, arr[0] = 10, obj.naam = 'Raj'"
                )
            else:
                break
        
        return expr
        
    
    def parse_argument_list(self) -> List[ASTNode]:
        args = []
        while self.current_token().type != TokenType.PAREN_BANDO:
            args.append(self.parse_expression())
            if self.current_token().type == TokenType.COMMA:
                self.advance()
        return args
    
    def parse_primary(self) -> ASTNode:
        token = self.current_token()
        
        if token.type == TokenType.SANKHYA:
            self.advance()
            return NumberLiteral(token.value)
        elif token.type == TokenType.SHABD:
            self.advance()
            return StringLiteral(token.value)
        elif token.type == TokenType.SACH:
            self.advance()
            return BooleanLiteral(True)
        elif token.type == TokenType.JHOOTH:
            self.advance()
            return BooleanLiteral(False)
        elif token.type == TokenType.KHAALI:
            self.advance()
            return NullLiteral()
        elif token.type == TokenType.BRACKET_KHOLO:
            return self.parse_array_literal()
        elif token.type == TokenType.KHOLO:
            return self.parse_object_literal()
        elif token.type == TokenType.LAMBDA:
            return self.parse_lambda()
        elif token.type == TokenType.PAREN_KHOLO:
            self.advance()
            expr = self.parse_expression()
            self.expect(TokenType.PAREN_BANDO)
            return expr
        elif token.type == TokenType.NEW:
            self.advance()
            class_name = self.expect(TokenType.IDENTIFIER).value
            self.expect(TokenType.PAREN_KHOLO)
            args = self.parse_argument_list()
            self.expect(TokenType.PAREN_BANDO)
            return FunctionCall(Identifier(class_name), args)
        elif token.type == TokenType.SUPER:
            self.advance()
            self.expect(TokenType.DOT)
            method_name = self.expect(TokenType.IDENTIFIER).value
            return Identifier('__super__.' + method_name)
        elif token.type == TokenType.IDENTIFIER:
            name = token.value
            self.advance()
            
            if self.current_token().type == TokenType.DEDO:
                self.advance()
                value = self.parse_expression()
                return Assignment(name, value)
            elif self.current_token().type in [TokenType.JODA_DEDO, TokenType.GHATAO_DEDO,
                                                TokenType.GUNA_DEDO, TokenType.BHAG_DEDO]:
                op = self.current_token().type
                self.advance()
                value = self.parse_expression()
                return CompoundAssignment(name, op, value)
            
            return Identifier(name)

        elif token.type == TokenType.YE:
            self.advance()
            return Identifier('ye')
        
        # If no primary expression matches, raise a user-friendly error
        got = f"'{token.value}'" if token.value is not None else token.type.name
        raise SyntaxError(f"Line {token.line} par {got} ka unexpected use hai. Expression ke is jagah pr iska use nahi ho sakta.")
    
    def parse_array_literal(self) -> ArrayLiteral:
        self.expect(TokenType.BRACKET_KHOLO)
        elements = []
        while self.current_token().type != TokenType.BRACKET_BANDO:
            elements.append(self.parse_expression())
            if self.current_token().type == TokenType.COMMA:
                self.advance()
        self.expect(TokenType.BRACKET_BANDO)
        return ArrayLiteral(elements)
    
    def parse_object_literal(self) -> ObjectLiteral:
        self.expect(TokenType.KHOLO)
        properties = {}
        while self.current_token().type != TokenType.BANDO:
            if self.current_token().type == TokenType.IDENTIFIER:
                key = self.current_token().value
                self.advance()
                self.expect(TokenType.COLON)
                value = self.parse_expression()
                properties[key] = value
                if self.current_token().type == TokenType.COMMA:
                    self.advance()
            else:
                break
        self.expect(TokenType.BANDO)
        return ObjectLiteral(properties)
    
    def parse_lambda(self) -> LambdaFunction:
        self.expect(TokenType.LAMBDA)
        self.expect(TokenType.PAREN_KHOLO)
        
        params = []
        while self.current_token().type != TokenType.PAREN_BANDO:
            params.append(self.expect(TokenType.IDENTIFIER).value)
            if self.current_token().type == TokenType.COMMA:
                self.advance()
        
        self.expect(TokenType.PAREN_BANDO)
        self.expect(TokenType.ARROW)
        
        if self.current_token().type == TokenType.KHOLO:
            body = self.parse_block()
        else:
            body = self.parse_expression()
        
        return LambdaFunction(params, body)
