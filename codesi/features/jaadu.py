import difflib
import re

class CodesiJaadu:
    """World's first context-aware programming language auto-correction"""
    
    def __init__(self):
        self.hinglish_keywords = {
            'likho','time_machine_status', 'time_machine_on', 'time_machine_off', 'peeche', 'aage', 'timeline', 'samjhao_on', 'samjhao_off', 'samjhao','input_lo', 'float_lo', 'int_lo', 'batao', 'karya', 'static','import_karo','as', 'in' 'lo',
            'agar', 'nahi_to', 'ya_phir', 'jabtak', 'liye', 'karo',
            'karya', 'vapas', 'break', 'continue', 'class', 'banao',
            'ye', 'super', 'extends', 'new', 'try', 'catch', 'finally',
            'throw', 'lambda', 'se', 'tak', 'mein', 'ke', 'sach', 'jhooth',
            'khaali', 'aur', 'ya', 'nahi', 'case', 'default'
        }
        
        self.common_functions = {
            'push', 'pop', 'shift', 'unshift', 'map', 'filter', 'reduce', 'dalo', 'jodo', 'nikalo', 'hatao', 'badlo', 'math_absolute', 'math_square', 'math_power', 'math_random', 'math_upar', 'math_gol', 'math_sin', 'math_cos', 'math_tan', 'math_log', 'math_exp', 'type_of', 'prakar', 'string_hai', 'array_hai', 'int_hai', 'float_hai', 'bool_hai', 'obj_hai', 'string_bnao', 'float_bnao', 'int_bnao', 'bool_bnao', 'lambai', 'range', 'repeatkr', 'file_padho', 'file_likho', 'file_append', 'file_hai', 'file_delete', 'file_copy', 'file_move', 'file_size', 'dir_banao', 'dir_list', 'json_stringify', 'json_parse', 'time_now', 'time_sleep', 'exit', 'quit', 'help', 'clear', 'vars', 'history',
            'qhelp', 'credits', 'copyright', 'quit'
        }
        
        # REPL commands should NOT be corrected
        self.repl_commands = {
            'exit', 'quit', 'help', 'clear', 'vars', 'history',
            'qhelp', 'credits', 'copyright', 'quit'
        }
        
        self.all_valid = self.hinglish_keywords | self.common_functions
    
    def suggest_correction(self, wrong_word):
        """Find closest match for typo"""
        
        if wrong_word in self.repl_commands:
            return None
        
        matches = difflib.get_close_matches(wrong_word, self.all_valid, n=1, cutoff=0.6)
        if matches:
            return matches[0]
        return None
    
    def auto_fix_code(self, code):
        """Automatically fix common typos in code"""
       
        stripped = code.strip()
        if stripped.startswith('!') or stripped.startswith('.'):
            return code, []
        
       
        first_word = stripped.split('(')[0].split()[0] if stripped else ''
        if first_word in self.repl_commands:
            return code, []
        
        
        function_calls = re.findall(r'\b([a-z_]+)\s*\(', code)
        
        fixes = []
        for func_name in function_calls:
            if func_name not in self.all_valid and func_name not in self.repl_commands:
                suggestion = self.suggest_correction(func_name)
                if suggestion:
                    fixes.append((func_name, suggestion))
        
        fixed_code = code
        for wrong, correct in fixes:
            
            fixed_code = re.sub(r'\b' + wrong + r'\s*\(', correct + '(', fixed_code)
        
        return fixed_code, fixes

jaadu_system = CodesiJaadu()
