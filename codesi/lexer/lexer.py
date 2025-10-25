from typing import Optional, List
from .tokens import Token, TokenType

class CodesiLexer:
    def __init__(self, code: str):
        self.code = code
        self.pos = 0
        self.line = 1
        self.column = 1
        self.tokens = []
        
        self.keywords = {
            'agar': TokenType.AGAR, 'nahi_to': TokenType.NAHI_TO, 'ya_phir': TokenType.YA_PHIR,
            'jabtak': TokenType.JABTAK, 'liye': TokenType.LIYE, 'karo': TokenType.KARO,
            'karya': TokenType.KARYA, 'vapas': TokenType.VAPAS, 'break': TokenType.BREAK,
            'continue': TokenType.CONTINUE, 'class': TokenType.CLASS, 'banao': TokenType.BANAO,
            'ye': TokenType.YE, 'super': TokenType.SUPER, 'extends': TokenType.EXTENDS,
            'static': TokenType.STATIC, 'new': TokenType.NEW, 'sach': TokenType.SACH,
            'jhooth': TokenType.JHOOTH, 'khaali': TokenType.KHAALI, 'aur': TokenType.AUR,
            'ya': TokenType.YA, 'nahi': TokenType.NAHI, 'try': TokenType.TRY,
            'catch': TokenType.CATCH, 'finally': TokenType.FINALLY, 'throw': TokenType.THROW,
            'lambda': TokenType.LAMBDA, 'export': TokenType.EXPORT,
            'from': TokenType.FROM, 'as': TokenType.AS, 'in': TokenType.IN,
            'se': TokenType.SE, 'tak': TokenType.TAK, 'mein': TokenType.MEIN,
            'ke': TokenType.KE, 'const': TokenType.CONST, 'readonly': TokenType.READONLY,
            'har': TokenType.HAR, 'get': TokenType.GET, 'set': TokenType.SET, 'case': TokenType.CASE,
            'default': TokenType.DEFAULT,
        }
    
    def current_char(self) -> Optional[str]:
        if self.pos >= len(self.code):
            return None
        return self.code[self.pos]
    
    def peek(self, offset=1) -> Optional[str]:
        pos = self.pos + offset
        if pos >= len(self.code):
            return None
        return self.code[pos]
    
    def advance(self):
        if self.pos < len(self.code):
            if self.code[self.pos] == '\n':
                self.line += 1
                self.column = 1
            else:
                self.column += 1
            self.pos += 1
    
    def skip_whitespace(self):
        while self.current_char() and self.current_char() in ' \t\r\n':
            self.advance()
    
    def skip_comment(self):
        if self.current_char() == '/' and self.peek() == '/':
            while self.current_char() and self.current_char() != '\n':
                self.advance()
    
    def read_number(self) -> Token:
        num_str = ''
        start_col = self.column
        has_dot = False
        
        while self.current_char() and (self.current_char().isdigit() or self.current_char() == '.'):
            if self.current_char() == '.':
                if has_dot:
                    break
                has_dot = True
            num_str += self.current_char()
            self.advance()
        
        value = float(num_str) if has_dot else int(num_str)
        return Token(TokenType.SANKHYA, value, self.line, start_col)
    
    def read_string(self, quote_char: str) -> Token:
        string = ''
        start_line = self.line
        start_col = self.column
        self.advance()  # Consume the opening quote
        
        while self.current_char() and self.current_char() != quote_char:
            if self.current_char() == '\\':
                self.advance()
                if self.current_char() == 'n':
                    string += '\n'
                elif self.current_char() == 't':
                    string += '\t'
                elif self.current_char() == 'r':
                    string += '\r'
                elif self.current_char() == 'b':
                    string += '\b'
                elif self.current_char() == 'f':
                    string += '\f'
                elif self.current_char() == 'v':
                    string += '\v'
                elif self.current_char() == '\\':
                    string += '\\'
                elif self.current_char() == quote_char:
                    string += quote_char
                elif self.current_char() == '0':
                    string += '\0'
                else:
                    string += self.current_char() if self.current_char() else ''
                self.advance()
            else:
                string += self.current_char()
                self.advance()
        
        # Check for unterminated string
        if self.current_char() != quote_char:
            raise SyntaxError(f"Line {start_line} par string poora nahi hua (unterminated string).")
        
        self.advance()  # Consume the closing quote
        
        return Token(TokenType.SHABD, string, start_line, start_col)
    
    def read_identifier(self) -> Token:
        ident = ''
        start_col = self.column
        
        while self.current_char() and (self.current_char().isalnum() or self.current_char() == '_'):
            ident += self.current_char()
            self.advance()
        
        token_type = self.keywords.get(ident, TokenType.IDENTIFIER)
        value = ident
        
        return Token(token_type, value, self.line, start_col)
    
    def tokenize(self) -> List[Token]:
        while self.pos < len(self.code):
            self.skip_whitespace()
            
            if self.current_char() is None:
                break
            
            if self.current_char() == '/' and self.peek() == '/':
                self.skip_comment()
                continue
            
            if self.current_char().isdigit():
                self.tokens.append(self.read_number())
                continue
            
            if self.current_char() in '"\'':
                quote = self.current_char()
                self.tokens.append(self.read_string(quote))
                continue
            
            if self.current_char().isalpha() or self.current_char() == '_':
                self.tokens.append(self.read_identifier())
                continue
            
            char = self.current_char()
            col = self.column
            
            # Two-character operators
            if char == '=' and self.peek() == '=':
                self.tokens.append(Token(TokenType.BARABAR, '==', self.line, col))
                self.advance()
                self.advance()
            elif char == '!' and self.peek() == '=':
                self.tokens.append(Token(TokenType.NAHI_BARABAR, '!=', self.line, col))
                self.advance()
                self.advance()
            elif char == '<' and self.peek() == '=':
                self.tokens.append(Token(TokenType.CHOTA_BARABAR, '<=', self.line, col))
                self.advance()
                self.advance()
            elif char == '>' and self.peek() == '=':
                self.tokens.append(Token(TokenType.BADA_BARABAR, '>=', self.line, col))
                self.advance()
                self.advance()
            elif char == '+' and self.peek() == '=':
                self.tokens.append(Token(TokenType.JODA_DEDO, '+=', self.line, col))
                self.advance()
                self.advance()
            elif char == '-' and self.peek() == '=':
                self.tokens.append(Token(TokenType.GHATAO_DEDO, '-=', self.line, col))
                self.advance()
                self.advance()
            elif char == '*' and self.peek() == '=':
                self.tokens.append(Token(TokenType.GUNA_DEDO, '*=', self.line, col))
                self.advance()
                self.advance()
            elif char == '/' and self.peek() == '=':
                self.tokens.append(Token(TokenType.BHAG_DEDO, '/=', self.line, col))
                self.advance()
                self.advance()
            elif char == '*' and self.peek() == '*':
                self.tokens.append(Token(TokenType.POWER, '**', self.line, col))
                self.advance()
                self.advance()
            elif char == '-' and self.peek() == '>':
                self.tokens.append(Token(TokenType.ARROW, '->', self.line, col))
                self.advance()
                self.advance()
            elif char == '.' and self.peek() == '.' and self.peek(2) == '.':
                self.tokens.append(Token(TokenType.ELLIPSIS, '...', self.line, col))
                self.advance()
                self.advance()
                self.advance()
            # Single-character operators
            elif char == '+':
                self.tokens.append(Token(TokenType.JODA, '+', self.line, col))
                self.advance()
            elif char == '-':
                self.tokens.append(Token(TokenType.GHATAO, '-', self.line, col))
                self.advance()
            elif char == '*':
                self.tokens.append(Token(TokenType.GUNA, '*', self.line, col))
                self.advance()
            elif char == '/':
                self.tokens.append(Token(TokenType.BHAG, '/', self.line, col))
                self.advance()
            elif char == '%':
                self.tokens.append(Token(TokenType.MODULO, '%', self.line, col))
                self.advance()
            elif char == '=':
                self.tokens.append(Token(TokenType.DEDO, '=', self.line, col))
                self.advance()
            elif char == '<':
                self.tokens.append(Token(TokenType.CHOTA, '<', self.line, col))
                self.advance()
            elif char == '>':
                self.tokens.append(Token(TokenType.BADA, '>', self.line, col))
                self.advance()
            elif char == '{':
                self.tokens.append(Token(TokenType.KHOLO, '{', self.line, col))
                self.advance()
            elif char == '}':
                self.tokens.append(Token(TokenType.BANDO, '}', self.line, col))
                self.advance()
            elif char == '[':
                self.tokens.append(Token(TokenType.BRACKET_KHOLO, '[', self.line, col))
                self.advance()
            elif char == ']':
                self.tokens.append(Token(TokenType.BRACKET_BANDO, ']', self.line, col))
                self.advance()
            elif char == '(':
                self.tokens.append(Token(TokenType.PAREN_KHOLO, '(', self.line, col))
                self.advance()
            elif char == ')':
                self.tokens.append(Token(TokenType.PAREN_BANDO, ')', self.line, col))
                self.advance()
            elif char == ';':
                self.tokens.append(Token(TokenType.SEMICOLON, ';', self.line, col))
                self.advance()
            elif char == ',':
                self.tokens.append(Token(TokenType.COMMA, ',', self.line, col))
                self.advance()
            elif char == '.':
                self.tokens.append(Token(TokenType.DOT, '.', self.line, col))
                self.advance()
            elif char == ':':
                self.tokens.append(Token(TokenType.COLON, ':', self.line, col))
                self.advance()
            elif char == '?':
                self.tokens.append(Token(TokenType.QUESTION, '?', self.line, col))
                self.advance()
            elif char == '@':
                self.tokens.append(Token(TokenType.AT, '@', self.line, col))
                self.advance()
            else:
                raise SyntaxError(f"Line {self.line}, column {col} par '{char}' naam ka character unknown hai.")
        
        self.tokens.append(Token(TokenType.EOF, None, self.line, self.column))
        return self.tokens
