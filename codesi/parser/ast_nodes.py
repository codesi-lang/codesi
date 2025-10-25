from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from ..lexer.tokens import Token, TokenType

class ASTNode:
    pass

@dataclass
class Program(ASTNode):
    statements: List[ASTNode]

@dataclass
class NumberLiteral(ASTNode):
    value: Union[int, float]

@dataclass
class StringLiteral(ASTNode):
    value: str

@dataclass
class BooleanLiteral(ASTNode):
    value: bool

@dataclass
class NullLiteral(ASTNode):
    pass

@dataclass
class Identifier(ASTNode):
    name: str

@dataclass
class BinaryOp(ASTNode):
    left: ASTNode
    operator: TokenType
    right: ASTNode

@dataclass
class UnaryOp(ASTNode):
    operator: TokenType
    operand: ASTNode

@dataclass
class Assignment(ASTNode):
    target: str
    value: ASTNode

@dataclass
class IndexAssignment(ASTNode):
    object: ASTNode
    index: ASTNode
    value: ASTNode

@dataclass
class MemberAssignment(ASTNode):
    object: ASTNode
    member: str
    value: ASTNode

@dataclass
class CompoundAssignment(ASTNode):
    target: str
    operator: TokenType
    value: ASTNode

@dataclass
class IfStatement(ASTNode):
    condition: ASTNode
    then_block: List[ASTNode]
    elif_blocks: List[tuple]
    else_block: Optional[List[ASTNode]] = None

@dataclass
class WhileLoop(ASTNode):
    condition: ASTNode
    body: List[ASTNode]

@dataclass
class DoWhileLoop(ASTNode):
    body: List[ASTNode]
    condition: ASTNode

@dataclass
class ForLoop(ASTNode):
    variable: str
    start: ASTNode
    end: ASTNode
    body: List[ASTNode]

@dataclass
class ForEachLoop(ASTNode):
    variable: str
    iterable: ASTNode
    body: List[ASTNode]

@dataclass
class FunctionDef(ASTNode):
    name: str
    parameters: List[tuple]
    body: List[ASTNode]
    return_type: Optional[str] = None

@dataclass
class FunctionCall(ASTNode):
    name: Union[str, ASTNode]
    arguments: List[ASTNode]

@dataclass
class ReturnStatement(ASTNode):
    value: Optional[ASTNode] = None

@dataclass
class BreakStatement(ASTNode):
    pass

@dataclass
class ContinueStatement(ASTNode):
    pass

@dataclass
class ArrayLiteral(ASTNode):
    elements: List[ASTNode]

@dataclass
class ObjectLiteral(ASTNode):
    properties: Dict[str, ASTNode]

@dataclass
class IndexAccess(ASTNode):
    object: ASTNode
    index: ASTNode

@dataclass
class MemberAccess(ASTNode):
    object: ASTNode
    member: str

@dataclass
class TernaryOp(ASTNode):
    condition: ASTNode
    true_value: ASTNode
    false_value: ASTNode

@dataclass
class ClassDef(ASTNode):
    name: str
    parent: Optional[str]
    methods: List[FunctionDef]
    constructor: Optional[FunctionDef] = None
    static_methods: Optional[List[FunctionDef]] = None

@dataclass
class TryCatch(ASTNode):
    try_block: List[ASTNode]
    catch_var: Optional[str]
    catch_block: List[ASTNode]
    finally_block: Optional[List[ASTNode]] = None

@dataclass
class ThrowStatement(ASTNode):
    value: ASTNode

@dataclass
class LambdaFunction(ASTNode):
    parameters: List[str]
    body: Union[ASTNode, List[ASTNode]]

@dataclass
class SwitchCase(ASTNode):
    expression: ASTNode
    cases: List[tuple]
    default_case: Optional[List[ASTNode]] = None


@dataclass
class ConstDeclaration(ASTNode):
    name: str
    value: ASTNode
