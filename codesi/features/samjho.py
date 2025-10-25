from ..lexer.tokens import TokenType
from ..parser.ast_nodes import (
    Identifier, NumberLiteral, StringLiteral, BooleanLiteral, BinaryOp, UnaryOp
)


class CodesiSamjho:
    """World's first built-in code explainer - No AI needed!"""
    
    def __init__(self):
        self.enabled = False
        self.explanations = []
        self.last_operation = None
    
    def enable(self):
        self.enabled = True
        self.explanations = []
    
    def disable(self):
        self.enabled = False

    def clear(self):
        self.explanations = []
        self.last_operation = None
    
    def _format_value(self, value):  
        """Format value for display"""
        if isinstance(value, str):
            return f"'{value}'"
        elif isinstance(value, list):
            return f"[{', '.join(str(v) for v in value)}]"
        elif isinstance(value, dict):
            items = ', '.join(f"{k}: {v}" for k, v in value.items())
            return f"{{{items}}}"
        elif isinstance(value, bool):
            return 'sach' if value else 'jhooth'
        elif value is None:
            return 'khaali'
        return str(value)
    
    def explain_assignment(self, var_name, value, expression_str=""):
        if not self.enabled:
            return
            
        if expression_str:
            self.explanations.append(
                f"Variable '{var_name}' mein expression ka result store kiya: {expression_str} = {value}"
            )
        else:
            self.explanations.append(
                f"Variable '{var_name}' mein value {self._format_value(value)} store ki"
            )
    
    def explain_operation(self, left, op, right, result):
        if not self.enabled:
            return
            
        op_map = {
            TokenType.JODA: "+",
            TokenType.GHATAO: "-",
            TokenType.GUNA: "*",
            TokenType.BHAG: "/",
            TokenType.MODULO: "%",
            TokenType.POWER: "**",
            TokenType.BARABAR: "==",
            TokenType.NAHI_BARABAR: "!=",
            TokenType.CHOTA: "<",
            TokenType.BADA: ">",
            TokenType.CHOTA_BARABAR: "<=",
            TokenType.BADA_BARABAR: ">=",
            TokenType.AUR: "and",
            TokenType.YA: "or"
        }
        
        op_str = op_map.get(op, str(op))
        self.explanations.append(f"🔢 Operation: {left} {op_str} {right} = {result}")
        self.last_operation = (left, op_str, right, result)
    
    def explain_condition(self, condition, result):
        if not self.enabled:
            return
            
        self.explanations.append(f"Condition: {condition} is {result}")
        
    def get_explanation(self):
        if not self.explanations:
            return "Koi explanation nahi hai. Pehle code chalao!"
        
        output = "\nCode Explanation:\n" + "="*60 + "\n"
        for i, exp in enumerate(self.explanations, 1):
            output += f"{i}. {exp}\n"
        output += "="*60
        return output

    def explain_if_condition(self, condition_node, result):
        """Explain if condition evaluation"""
        if not self.enabled:
            return
        result_text = "sach" if result else "jhooth"
       
        condition_str = self._ast_to_string(condition_node)
        self.explanations.append(f"If condition check: ({condition_str}) → {result_text}")

    def explain_elif_condition(self, condition_node, result):
        """Explain elif condition"""
        if not self.enabled:
            return
        result_text = "sach (executed)" if result else "jhooth (skipped)"
       
        condition_str = self._ast_to_string(condition_node)
        self.explanations.append(f"Elif condition: ({condition_str}) → {result_text}")

    def explain_else_block(self):
        """Explain else block execution"""
        if not self.enabled:
            return
        self.explanations.append(f"Else block execute hogya (pichle saare conditions jhooth the)")

    def explain_loop_start(self, loop_type, condition_node):
        """Explain loop start"""
        if not self.enabled:
            return
       
        if condition_node:
            condition_str = self._ast_to_string(condition_node)
            self.explanations.append(f"{loop_type} loop started: condition ({condition_str})")
        else:
            self.explanations.append(f"{loop_type} loop started")

    def explain_loop_iteration(self, var_name, value):
        """Explain loop iteration"""
        if not self.enabled:
            return
        self.explanations.append(f"  ↻ Loop iteration: {var_name} = {self._format_value(value)}")

    def explain_loop_end(self, loop_type):
        """Explain loop end"""
        if not self.enabled:
            return
        self.explanations.append(f"✓ {loop_type} loop completed")

    def explain_function_definition(self, func_name, params):
        """Explain function definition"""
        if not self.enabled:
            return
        param_str = ", ".join(p[0] if isinstance(p, tuple) else p for p in params)
        self.explanations.append(f"Function '{func_name}({param_str})' defined")

    def explain_function_call(self, func_name, args, result=None):
        """Explain function call"""
        if not self.enabled:
            return
        args_str = ", ".join(self._format_value(arg) for arg in args)
        if result is not None:
            self.explanations.append(f"Function call: {func_name}({args_str}) → returned {self._format_value(result)}")
        else:
            self.explanations.append(f"Function call: {func_name}({args_str}) (no return)")

    def explain_return(self, value):
        """Explain return statement"""
        if not self.enabled:
            return
        self.explanations.append(f"Return: {self._format_value(value)}")

    def explain_array_operation(self, operation, details):
        """Explain array operations"""
        if not self.enabled:
            return
        self.explanations.append(f"Array operation: {operation} - {details}")

    def _ast_to_string(self, node):
        """Convert AST node to readable string"""
        if isinstance(node, Identifier):
            return node.name
        elif isinstance(node, NumberLiteral):
            return str(node.value)
        elif isinstance(node, StringLiteral):
            return f"'{node.value}'"
        elif isinstance(node, BooleanLiteral):
            return 'sach' if node.value else 'jhooth'
        elif isinstance(node, BinaryOp):
            op_map = {
                TokenType.JODA: "+",
                TokenType.GHATAO: "-",
                TokenType.GUNA: "*",
                TokenType.BHAG: "/",
                TokenType.MODULO: "%",
                TokenType.POWER: "**",
                TokenType.BARABAR: "==",
                TokenType.NAHI_BARABAR: "!=",
                TokenType.CHOTA: "<",
                TokenType.BADA: ">",
                TokenType.CHOTA_BARABAR: "<=",
                TokenType.BADA_BARABAR: ">=",
                TokenType.AUR: "aur",
                TokenType.YA: "ya"
            }
            left_str = self._ast_to_string(node.left)
            right_str = self._ast_to_string(node.right)
            op_str = op_map.get(node.operator, str(node.operator))
            return f"{left_str} {op_str} {right_str}"
        elif isinstance(node, UnaryOp):
            if node.operator == TokenType.NAHI:
                return f"nahi {self._ast_to_string(node.operand)}"
            elif node.operator == TokenType.GHATAO:
                return f"-{self._ast_to_string(node.operand)}"
        else:
           
            return str(node)

    def explain_object_operation(self, operation, details):
        """Explain object operations"""
        if not self.enabled:
            return
        self.explanations.append(f"Object operation: {operation} - {details}")


samjho_system = CodesiSamjho()
