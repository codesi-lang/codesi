from enum import Enum, auto
from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass

class TokenType(Enum):
    # Literals
    SANKHYA = auto()  # Number
    SHABD = auto()  # String
    SACH = auto()  # True
    JHOOTH = auto()  # False
    KHAALI = auto()  # Null/None
    
    # Operators
    JODA = auto()  # +
    GHATAO = auto()  # -
    GUNA = auto()  # *
    BHAG = auto()  # /
    MODULO = auto()  # %
    POWER = auto()  # **
    
    # Comparison
    BARABAR = auto()  # ==
    NAHI_BARABAR = auto()  # !=
    CHOTA = auto()  # <
    BADA = auto()  # >
    CHOTA_BARABAR = auto()  # <=
    BADA_BARABAR = auto()  # >=
    
    # Logical
    AUR = auto()  # and
    YA = auto()  # or
    NAHI = auto()  # not
    
    # Assignment
    DEDO = auto()  # =
    JODA_DEDO = auto()  # +=
    GHATAO_DEDO = auto()  # -=
    GUNA_DEDO = auto()  # *=
    BHAG_DEDO = auto()  # /=
    
    # Keywords
    AGAR = auto()  # if
    NAHI_TO = auto()  # else
    YA_PHIR = auto()  # elif
    JABTAK = auto()  # while
    LIYE = auto()  # for
    KARO = auto()  # do
    KARYA = auto()  # function
    VAPAS = auto()  # return
    BREAK = auto()
    CONTINUE = auto()
    CLASS = auto()
    BANAO = auto()  # constructor
    YE = auto()  # this/self
    SUPER = auto()
    EXTENDS = auto()
    STATIC = auto()
    NEW = auto()
    TRY = auto()
    CATCH = auto()
    FINALLY = auto()
    THROW = auto()
    ASYNC = auto()
    AWAIT = auto()
    YIELD = auto()
    LAMBDA = auto()
    EXPORT = auto()
    FROM = auto()
    AS = auto()
    IN = auto()
    SE = auto()  # from
    TAK = auto()  # to
    MEIN = auto()  # in
    KE = auto()  # for possessive
    CONST = auto()
    READONLY = auto()
    GET = auto()
    SET = auto()
    HAR = auto() # for/for-each (har ek = each one)
    CASE = auto()  # for switch-case
    DEFAULT = auto()  # for switch default
    
    # Delimiters
    KHOLO = auto()  # {
    BANDO = auto()  # }
    BRACKET_KHOLO = auto()  # [
    BRACKET_BANDO = auto()  # ]
    PAREN_KHOLO = auto()  # (
    PAREN_BANDO = auto()  # )
    SEMICOLON = auto()  # ;
    COMMA = auto()  # ,
    DOT = auto()  # .
    COLON = auto()  # :
    ARROW = auto()  # ->
    QUESTION = auto()  # ?
    ELLIPSIS = auto()  # ... (for variadic)
    AT = auto()  # @ (for decorators)
    
    # Special
    IDENTIFIER = auto()
    EOF = auto()

@dataclass
class Token:
    type: TokenType
    value: Any
    line: int
    column: int
