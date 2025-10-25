from typing import Any, Dict, List, Optional, Union
import os, json, math, time, random, shutil, difflib
from ..lexer.tokens import TokenType
from ..parser.ast_nodes import *
from ..exceptions import *
from .runtime import CodesiFunction, CodesiClass, CodesiObject
from .builtins import get_builtins
from ..features.jaadu import jaadu_system
from ..features.samjho import samjho_system
from ..features.timemachine import time_machine
from ..exceptions import CodesiError, ReturnException, BreakException, ContinueException

class CodesiInterpreter:
    def __init__(self, jaadu_mode=False):
        self.global_scope = {}
        self.current_scope = self.global_scope
        self.scope_stack = [self.global_scope]
        self.const_vars = set()
        self.jaadu_mode = jaadu_mode  
        self.setup_builtins()
    
    def setup_builtins(self):
        """Initialize all built-in functions"""
        from .builtins import get_builtins
        self.global_scope.update(get_builtins(self))

    def _time_travel_back(self, steps=1):
        """Time travel backwards"""
        snapshot_index = time_machine.go_back(steps)
        if isinstance(snapshot_index, str):
            print(snapshot_index)
            return None
        
        snap = time_machine.get_snapshot(snapshot_index)
        if not snap:
            return None
        
        
        builtin_names = set()
        for name, value in self.global_scope.items():
            if callable(value):
                builtin_names.add(name)
        
        
        to_delete = [k for k in self.current_scope.keys() if k not in builtin_names]
        for k in to_delete:
            del self.current_scope[k]
        
        
        for key, value in snap['variables'].items():
            if isinstance(value, list):
                self.current_scope[key] = value.copy()  
            elif isinstance(value, dict):
                self.current_scope[key] = value.copy()  
            else:
                self.current_scope[key] = value
        
        print(time_machine._show_snapshot(snapshot_index))
        return None

    def _time_travel_forward(self, steps=1):
        """Time travel forwards"""
        snapshot_index = time_machine.go_forward(steps)
        if isinstance(snapshot_index, str):
            print(snapshot_index)
            return None
        
        snap = time_machine.get_snapshot(snapshot_index)
        if not snap:
            return None
        
       
        builtin_names = set()
        for name, value in self.global_scope.items():
            if callable(value):
                builtin_names.add(name)
        
        
        to_delete = [k for k in self.current_scope.keys() if k not in builtin_names]
        for k in to_delete:
            del self.current_scope[k]
        
       
        for key, value in snap['variables'].items():
            if isinstance(value, list):
                self.current_scope[key] = value.copy()  
            elif isinstance(value, dict):
                self.current_scope[key] = value.copy()  
            else:
                self.current_scope[key] = value
        
        print(time_machine._show_snapshot(snapshot_index))
        return None

    def get_type_name(self, value):
        """Get type name of a value"""
        if isinstance(value, bool):
            return 'sach_jhooth'
        elif isinstance(value, (int)):
            return 'Integer'
        elif isinstance(value, (float)):
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
    
    def to_string(self, value):
        """Convert value to string representation"""
        if isinstance(value, bool):
            return 'sach' if value else 'jhooth'
        elif value is None:
            return 'khaali'
        elif isinstance(value, list):
            return '[' + ', '.join(self.to_string(v) for v in value) + ']'
        elif isinstance(value, dict):
            items = [f'{k}: {self.to_string(v)}' for k, v in value.items()]
            return '{' + ', '.join(items) + '}'
        return str(value)
    
    def push_scope(self, new_scope=None):
        """Push a new scope onto the stack"""
        if new_scope is None:
            new_scope = {}
        self.scope_stack.append(new_scope)
        self.current_scope = new_scope
    
    def pop_scope(self):
        """Pop the current scope from the stack"""
        self.scope_stack.pop()
        self.current_scope = self.scope_stack[-1]
    
    def get_variable(self, name):
        """Get variable value, searching up the scope chain"""
        for scope in reversed(self.scope_stack):
            if name in scope:
                return scope[name]
        
        # JAADU: Suggest similar variable
        all_vars = set()
        for scope in self.scope_stack:
            all_vars.update(scope.keys())
        
        suggestion = difflib.get_close_matches(name, all_vars, n=1, cutoff=0.6)
        if suggestion:
            raise CodesiError(
                f"Variable '{name}' define nahi hai",
                f"Kya aapka matlab '{suggestion[0]}' tha?"
            )
        else:
            raise CodesiError(f"Variable '{name}' define nahi hai")
    
    def set_variable(self, name, value):
        """Set variable in current scope"""
        self.current_scope[name] = value
    
    def interpret(self, ast: Program):
        """Interpret the AST"""
        try:
            for statement in ast.statements:
                self.visit(statement)
        except ReturnException:
            pass
    
    def visit(self, node):
        """Visit an AST node"""
        method_name = f'visit_{node.__class__.__name__}'
        method = getattr(self, method_name, None)
        if method is None:
            raise CodesiError(f"{node.__class__.__name__} ke liye koi visit method nahi mila.")
        return method(node)
    
    def visit_Program(self, node):
        for statement in node.statements:
            self.visit(statement)
    
    def visit_NumberLiteral(self, node):
        return node.value
    
    def visit_StringLiteral(self, node):
        return node.value
    
    def visit_BooleanLiteral(self, node):
        return node.value
    
    def visit_NullLiteral(self, node):
        return None
    
    def visit_Identifier(self, node):
        return self.get_variable(node.name)

    def visit_BinaryOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        
        op = node.operator
        result = None

        try:
            if op == TokenType.JODA:
                result = left + right
            elif op == TokenType.GHATAO:
                result = left - right
            elif op == TokenType.GUNA:
                result = left * right
            elif op == TokenType.BHAG:
                if right == 0:
                    raise CodesiError("Zero se divide nahi kar sakte")
                result = left / right
            elif op == TokenType.MODULO:
                if right == 0:
                    raise CodesiError("Zero se modulo nahi kar sakte")
                result = left % right
            elif op == TokenType.POWER:
                result = left ** right
            elif op == TokenType.BARABAR:
                result = left == right
            elif op == TokenType.NAHI_BARABAR:
                result = left != right
            elif op == TokenType.CHOTA:
                result = left < right
            elif op == TokenType.BADA:
                result = left > right
            elif op == TokenType.CHOTA_BARABAR:
                result = left <= right
            elif op == TokenType.BADA_BARABAR:
                result = left >= right
            elif op == TokenType.AUR:
                result = left and right
            elif op == TokenType.YA:
                result = left or right
        except TypeError:
            op_map = {TokenType.JODA: '+', TokenType.GHATAO: '-', TokenType.GUNA: '*', TokenType.BHAG: '/'}
            op_symbol = op_map.get(op, "operation")
            left_type = self.get_type_name(left)
            right_type = self.get_type_name(right)
            raise CodesiError(f"'{left_type}' aur '{right_type}' ke beech '{op_symbol}' operation nahi ho sakta.")
        
       
        if samjho_system.enabled and op in [TokenType.JODA, TokenType.GHATAO, TokenType.GUNA, TokenType.BHAG, TokenType.MODULO, TokenType.POWER]:
            samjho_system.explain_operation(left, op, right, result)

        
        op_map = {
            TokenType.JODA: '+', TokenType.GHATAO: '-', TokenType.GUNA: '*',
            TokenType.BHAG: '/', TokenType.MODULO: '%', TokenType.POWER: '**'
        }
        op_symbol = op_map.get(op, str(op))
        
        
        return result 
    
    def visit_UnaryOp(self, node):
        operand = self.visit(node.operand)
        
        if node.operator == TokenType.GHATAO:
            return -operand
        elif node.operator == TokenType.NAHI:
            return not operand
    





    def visit_Assignment(self, node):
        # Check if variable is const
        if node.target in self.const_vars:
            raise CodesiError(f"const variable '{node.target}' ko dobara assign nahi kar sakte.")
        
        value = self.visit(node.value)
        self.set_variable(node.target, value)
        
        # SAMJHO: Track assignment
        samjho_system.explain_assignment(node.target, value)
        
        # TIME MACHINE: Take snapshot AFTER assignment
        time_machine.take_snapshot(self.current_scope, f"Variable '{node.target}' assigned value {value}")
        
        return value

    def visit_ConstDeclaration(self, node):
        if node.name in self.current_scope:
            raise CodesiError(f"Variable '{node.name}' pehle se hi declared hai.")
        
        value = self.visit(node.value)
        self.const_vars.add(node.name)
        self.set_variable(node.name, value)
        
        # SAMJHO: Track assignment
        samjho_system.explain_assignment(node.name, value)
        
        # TIME MACHINE: Take snapshot AFTER assignment
        time_machine.take_snapshot(self.current_scope, f"const variable '{node.name}' assigned value {value}")
        
        return value


    def visit_IndexAssignment(self, node):
        obj = self.visit(node.object)
        index = self.visit(node.index)
        value = self.visit(node.value)
        
        if isinstance(obj, (list, dict)):
            obj[index] = value
            
            # 🔧 NEW: Take snapshot for index assignment
            time_machine.take_snapshot(
                self.current_scope,
                f"Index assignment: [{index}] = {value}"
            )
            
            return value
        elif isinstance(obj, CodesiObject):
            obj.properties[index] = value
            
            # 🔧 NEW: Take snapshot
            time_machine.take_snapshot(
                self.current_scope,
                f"Object index assignment: [{index}] = {value}"
            )
            
            return value
        else:
            raise CodesiError("Index assignment sirf arrays aur objects par kaam karta hai.")

    def visit_MemberAssignment(self, node):
        obj = self.visit(node.object)
        value = self.visit(node.value)
        
        if isinstance(obj, dict):
            obj[node.member] = value
            
            # 🔧 NEW: Take snapshot for member assignment
            time_machine.take_snapshot(
                self.current_scope,
                f"Member assignment: .{node.member} = {value}"
            )
            
            return value
        elif isinstance(obj, CodesiObject):
            obj.properties[node.member] = value
            
            # 🔧 NEW: Take snapshot
            time_machine.take_snapshot(
                self.current_scope,
                f"Object member assignment: .{node.member} = {value}"
            )
            
            return value
        else:
            raise CodesiError("Member assignment sirf objects par kaam karta hai.")



  
    def visit_CompoundAssignment(self, node):
        current = self.get_variable(node.target)
        value = self.visit(node.value)
        
        if node.operator == TokenType.JODA_DEDO:
            result = current + value
        elif node.operator == TokenType.GHATAO_DEDO:
            result = current - value
        elif node.operator == TokenType.GUNA_DEDO:
            result = current * value
        elif node.operator == TokenType.BHAG_DEDO:
            result = current / value
        
        self.set_variable(node.target, result)
        return result

    def visit_IfStatement(self, node):
        condition = self.visit(node.condition)
        
        # 🔧 NEW: Explain if condition
        samjho_system.explain_if_condition(node.condition, condition)
        
        if condition:
            for stmt in node.then_block:
                self.visit(stmt)
        else:
            executed = False
            for elif_cond, elif_body in node.elif_blocks:
                elif_result = self.visit(elif_cond)
                
                samjho_system.explain_elif_condition(elif_cond, elif_result)
                
                if elif_result:
                    for stmt in elif_body:
                        self.visit(stmt)
                    executed = True
                    break
            
            if not executed and node.else_block:
                # 🔧 NEW: Explain else
                samjho_system.explain_else_block()
                for stmt in node.else_block:
                    self.visit(stmt)

    def visit_WhileLoop(self, node):
        # 🔧 NEW: Explain loop start
        samjho_system.explain_loop_start("While", node.condition)
        
        iteration = 0
        while self.visit(node.condition):
            iteration += 1
            
           
            if iteration <= 5:
                samjho_system.explain_loop_iteration("iteration", iteration)
            elif iteration == 6:
                samjho_system.explanations.append("  ↻ ... (more iterations)")
            
            try:
                for stmt in node.body:
                    self.visit(stmt)
            except BreakException:
                samjho_system.explanations.append("  🛑 Loop break encountered")
                break
            except ContinueException:
                samjho_system.explanations.append("  ⏭️  Loop continue encountered")
                continue
        
        # 🔧 NEW: Explain loop end
        samjho_system.explain_loop_end("While")

    def visit_DoWhileLoop(self, node):
        while True:
            try:
                for stmt in node.body:
                    self.visit(stmt)
            except BreakException:
                break
            except ContinueException:
                pass
            
            if not self.visit(node.condition):
                break

    def visit_SwitchCase(self, node):
        switch_value = self.visit(node.expression)
        
        matched = False
        for case_value_node, case_stmts in node.cases:
            case_value = self.visit(case_value_node)
            if switch_value == case_value:
                matched = True
                for stmt in case_stmts:
                    self.visit(stmt)
                break
        
        if not matched and node.default_case:
            for stmt in node.default_case:
                self.visit(stmt)

    def visit_ForLoop(self, node):
        start = int(self.visit(node.start))
        end = int(self.visit(node.end))
        
        for i in range(start, end):
            self.set_variable(node.variable, i)
            try:
                for stmt in node.body:
                    self.visit(stmt)
            except BreakException:
                break
            except ContinueException:
                continue

    def visit_ForEachLoop(self, node):
        iterable = self.visit(node.iterable)
        
        if not isinstance(iterable, (list, str, dict)):
            raise CodesiError("ForEach loop ke liye iterable chahiye")
        
        if isinstance(iterable, dict):
            items = list(iterable.keys())
        else:
            items = iterable
        
        for item in items:
            self.set_variable(node.variable, item)
            try:
                for stmt in node.body:
                    self.visit(stmt)
            except BreakException:
                break
            except ContinueException:
                continue

    def visit_FunctionDef(self, node):
        # 🔧 NEW: Explain function definition
        samjho_system.explain_function_definition(node.name, node.parameters)
        
        func = CodesiFunction(node.name, node.parameters, node.body, dict(self.current_scope))
        self.set_variable(node.name, func)
        return func

    def visit_FunctionCall(self, node):
        if isinstance(node.name, MemberAccess):
            obj = self.visit(node.name.object)
            method_name = node.name.member
            args = [self.visit(arg) for arg in node.arguments]
            return self._call_method(obj, method_name, args)
        elif isinstance(node.name, IndexAccess):
            obj = self.visit(node.name.object)
            args = [self.visit(arg) for arg in node.arguments]
            if callable(obj):
                return obj(*args)
            raise CodesiError("Non-function ko call nahi kiya ja sakta.")
        
        if isinstance(node.name, Identifier):
            func = self.get_variable(node.name.name)
        else:
            func = self.visit(node.name)
        
        args = [self.visit(arg) for arg in node.arguments]
        
        

        if callable(func) and not isinstance(func, CodesiFunction):
            return func(*args)
        
        return self.call_function(func, args)

    def _call_method(self, obj, method_name, args):
        if isinstance(obj, list):
            return self._array_method(obj, method_name, args)
        elif isinstance(obj, str):
            return self._string_method(obj, method_name, args)
        elif isinstance(obj, dict):
            return self._dict_method(obj, method_name, args)
        elif isinstance(obj, CodesiObject):
            if method_name in obj.properties:
                method_func = obj.properties[method_name]
                return self.call_function(method_func, args, obj)
            raise CodesiError(f"Object par method '{method_name}' nahi mila.")
            if obj.class_def and obj.class_def.parent:
                parent_class = obj.class_def.parent
                if isinstance(parent_class, str):
                    parent_class = self.get_variable(parent_class)
                if isinstance(parent_class, CodesiClass):
                    for method in parent_class.methods:
                        if method.name == method_name:
                            parent_func = CodesiFunction(method.name, method.parameters, method.body, {})
                            return self.call_function(parent_func, args, obj)
            raise CodesiError(f"Method '{method_name}' nahi mila.")
        else:
            raise CodesiError(f"{self.get_type_name(obj)} par method call nahi kiya ja sakta.")


    def _array_method(self, arr, method_name, args):
        """Array methods with snapshot support"""
        
        if method_name in ['push', 'dalo']:
            arr.append(args[0] if args else None)
            
           
            time_machine.take_snapshot(
                self.current_scope,
                f"Array method: {method_name}({args[0] if args else ''})"
            )
            return arr
        
        elif method_name in ['pop', 'nikalo']:
            result = arr.pop() if arr else None
            
            
            time_machine.take_snapshot(
                self.current_scope,
                f"Array method: {method_name}()"
            )
            return result
        
        elif method_name in ['shift', 'pehla_nikalo']:
            result = arr.pop(0) if arr else None
            
           
            time_machine.take_snapshot(
                self.current_scope,
                f"Array method: {method_name}()"
            )
            return result
        
        elif method_name in ['unshift', 'pehle_dalo']:
            arr.insert(0, args[0] if args else None)
            
            
            time_machine.take_snapshot(
                self.current_scope,
                f"Array method: {method_name}({args[0] if args else ''})"
            )
            return arr
        
        elif method_name in ['lambai', 'size']:
            return len(arr)  # No snapshot (read-only)
        
        elif method_name in ['map', 'badlo']:
            func = args[0] if args else None
            return [self.call_function(func, [item]) for item in arr]
            # No snapshot (creates new array)
        
        elif method_name in ['filter', 'chuno']:
            func = args[0] if args else None
            return [item for item in arr if self.call_function(func, [item])]
            # No snapshot (creates new array)
        
        elif method_name in ['join', 'jodo']:
            sep = args[0] if args else ','
            return sep.join(str(item) for item in arr)
            # No snapshot (read-only)
        
        elif method_name in ['slice', 'cutkr']:
            start = args[0] if args else 0
            end = args[1] if len(args) > 1 else len(arr)
            return arr[int(start):int(end)]
            # No snapshot (creates new array)
        
        elif method_name in ['reverse', 'ulta']:
            arr.reverse()
            
          
            time_machine.take_snapshot(
                self.current_scope,
                f"Array method: {method_name}()"
            )
            return arr
        
        elif method_name in ['sort', 'arrange']:
            arr.sort()
            
          
            time_machine.take_snapshot(
                self.current_scope,
                f"Array method: {method_name}()"
            )
            return arr
        
        elif method_name in ['reduce', 'combine']:
            if not args:
                raise CodesiError("reduce ko callback ki zarurat hai.")
            func = args[0]
            initial = args[1] if len(args) > 1 else (arr[0] if arr else None)
            start_idx = 0 if len(args) > 1 else 1
            acc = initial
            for i in range(start_idx, len(arr)):
                acc = self.call_function(func, [acc, arr[i]])
            return acc
            
        
        else:
            raise CodesiError(f"Array method '{method_name}' nahi mila.")


    
    def _string_method(self, string, method_name, args):
        if method_name in ['lambai', 'size']:
            return len(string)
        elif method_name in ['bada_karo']:
            return string.upper()
        elif method_name in ['chota_karo']:
            return string.lower()
        elif method_name in ['saaf_karo']:
            return string.strip()
        elif method_name in ['todo']:
            sep = args[0] if args else ' '
            return string.split(sep)
        elif method_name in ['badlo']:
            old = args[0] if len(args) > 0 else ''
            new = args[1] if len(args) > 1 else ''
            return string.replace(old, new, 1)
        elif method_name in ['sab_badlo']:
            old = args[0] if len(args) > 0 else ''
            new = args[1] if len(args) > 1 else ''
            return string.replace(old, new)
        elif method_name in ['included_hai']:
            return (args[0] if args else '') in string
        elif method_name in ['start_hota_hai']:
            return string.startswith(args[0] if args else '')
        elif method_name in ['end_hota_hai']:
            return string.endswith(args[0] if args else '')
        else:
            raise CodesiError(f"String method '{method_name}' nahi mila.")

    def _dict_method(self, obj, method_name, args):
        if method_name in ['keys']:
            return list(obj.keys())
        elif method_name in ['values']:
            return list(obj.values())
        elif method_name in ['items']:
            return [[k, v] for k, v in obj.items()]
        elif method_name in ['hai_kya']:
            return (args[0] if args else None) in obj
        else:
            raise CodesiError(f"Object method '{method_name}' nahi mila.")

    def call_function(self, func, args, instance=None):
        if isinstance(func, CodesiClass):
            obj = CodesiObject(func)
            
            # Step 1: Add parent class methods first
            if func.parent:
                parent_class = func.parent
                if isinstance(parent_class, str):
                    parent_class = self.get_variable(parent_class)
                if isinstance(parent_class, CodesiClass):
                    for method in parent_class.methods:
                        obj.properties[method.name] = CodesiFunction(
                            method.name, method.parameters, method.body, dict(self.current_scope)
                        )
            
            # Step 2: Add child class methods (these override parent methods)
            for method in func.methods:
                obj.properties[method.name] = CodesiFunction(
                    method.name, method.parameters, method.body, dict(self.current_scope)
                )
            
            # Step 3: Call constructor - use child's constructor, if not then parent's
            constructor_to_call = func.constructor
            if not constructor_to_call and func.parent:
                parent_class = func.parent
                if isinstance(parent_class, str):
                    parent_class = self.get_variable(parent_class)
                if isinstance(parent_class, CodesiClass):
                    constructor_to_call = parent_class.constructor
            
            # Step 4: Execute constructor
            if constructor_to_call:
                constructor_func = CodesiFunction(
                    'banao', 
                    constructor_to_call.parameters, 
                    constructor_to_call.body, 
                    dict(self.current_scope)
                )
                self.call_function(constructor_func, args, obj)
            
            return obj
        
        # Regular function call (not class instantiation)
        if not isinstance(func, CodesiFunction):
            raise CodesiError(f"Function nahi hai - {type(func).__name__} hai")
        
        new_scope = dict(func.closure)
        
        # Bind parameters
        for i, param_info in enumerate(func.params):
            if isinstance(param_info, tuple):
                param_name = param_info[0]
                default_val = param_info[2] if len(param_info) > 2 else None
                is_variadic = param_info[3] if len(param_info) > 3 else False
            else:
                param_name = param_info
                default_val = None
                is_variadic = False
            
            if is_variadic:
                new_scope[param_name] = args[i:]
                break
            elif i < len(args):
                new_scope[param_name] = args[i]
            elif default_val is not None:
                new_scope[param_name] = self.visit(default_val)
            elif is_variadic:
                new_scope[param_name] = []
        
        if instance:
            new_scope['ye'] = instance
        
        self.push_scope(new_scope)
        
        try:
            for stmt in func.body:
                self.visit(stmt)
            result = None
        except ReturnException as e:
            result = e.value
            # 🔧 NEW: Explain return
            samjho_system.explain_return(result)
        finally:
            self.pop_scope()

        # 🔧 NEW: Explain function result
        if samjho_system.enabled and isinstance(func.name, str):
            args_for_display = args if instance is None else [instance] + args
            samjho_system.explain_function_call(func.name, args_for_display, result)

        return result
    
    def visit_ReturnStatement(self, node):
        value = self.visit(node.value) if node.value else None
        raise ReturnException(value)

    def visit_BreakStatement(self, node):
        raise BreakException()

    def visit_ContinueStatement(self, node):
        raise ContinueException()

    def visit_ArrayLiteral(self, node):
        return [self.visit(elem) for elem in node.elements]

    def visit_ObjectLiteral(self, node):
        obj = {}
        for key, value_node in node.properties.items():
            obj[key] = self.visit(value_node)
        return obj

    def visit_IndexAccess(self, node):
        obj = self.visit(node.object)
        index = self.visit(node.index)
        
        if isinstance(obj, (list, str)):
            idx = int(index)
            if idx < 0:
                idx = len(obj) + idx
            if 0 <= idx < len(obj):
                return obj[idx]
            raise CodesiError(f"Index range ke bahar hai.")
        elif isinstance(obj, dict):
            return obj.get(index)
        elif isinstance(obj, CodesiObject):
            return obj.properties.get(index)
        else:
            raise CodesiError("Invalid index access hai.")

    def visit_MemberAccess(self, node):
        obj = self.visit(node.object)
        
        if isinstance(obj, dict):
            return obj.get(node.member)
        elif isinstance(obj, CodesiObject):
            return obj.properties.get(node.member)
        else:
            return obj

    def visit_TernaryOp(self, node):
        condition = self.visit(node.condition)
        if condition:
            return self.visit(node.true_value)
        else:
            return self.visit(node.false_value)

    def visit_ClassDef(self, node):
        parent = None
        if node.parent:
            parent = self.get_variable(node.parent)
        
        class_obj = CodesiClass(node.name, parent, node.methods, node.constructor)
        
        if node.static_methods:
            for static_method in node.static_methods:
                func = CodesiFunction(static_method.name, static_method.parameters, 
                                    static_method.body, dict(self.current_scope))
                if not hasattr(class_obj, 'static_methods'):
                    class_obj.static_methods = {}
                class_obj.static_methods[static_method.name] = func
        
        self.set_variable(node.name, class_obj)
        return class_obj

    def visit_TryCatch(self, node):
        try:
            for stmt in node.try_block:
                self.visit(stmt)
        except Exception as e:
            if node.catch_var:
                self.set_variable(node.catch_var, {'message': str(e)})
            for stmt in node.catch_block:
                self.visit(stmt)
        finally:
            if node.finally_block:
                for stmt in node.finally_block:
                    self.visit(stmt)

    def visit_ThrowStatement(self, node):
        value = self.visit(node.value)
        if isinstance(value, dict) and 'message' in value:
            raise CodesiError(value['message'])
        else:
            raise CodesiError(str(value))

    def visit_LambdaFunction(self, node):
        return CodesiFunction(
            '<lambda>', 
            [(p, None, None, False) for p in node.parameters],
            [ReturnStatement(node.body)] if not isinstance(node.body, list) else node.body,
            dict(self.current_scope)
        )