import difflib
import re

class CodesiJaadu:
    """World's first context-aware programming language auto-correction"""
    
    def __init__(self):
        self.hinglish_keywords = {
            'likho', 'dikhao', 'batao', 'sunao', 'pucho', 'lo',
            'agar', 'nahi_to', 'ya_phir', 'jabtak', 'liye', 'karo',
            'karya', 'vapas', 'break', 'continue', 'class', 'banao',
            'ye', 'super', 'extends', 'new', 'try', 'catch', 'finally',
            'throw', 'lambda', 'se', 'tak', 'mein', 'ke', 'sach', 'jhooth',
            'khaali', 'aur', 'ya', 'nahi', 'case', 'default'
        }
        
        self.common_functions = {
            'likho', 'sunao', 'abs', 'sqrt', 'random', 'len', 'type_of',
            'to_string', 'to_number', 'to_int', 'file_padho', 'file_likho',
            'lambai', 'dohrao', 'mutlaq', 'vargmool', 'yaddrachik',
            'print', 'dikhao', 'batao', 'pucho', 'lo', 'input',
            'push', 'pop', 'shift', 'unshift', 'map', 'filter', 'reduce',
            'dalo', 'jodo', 'nikalo', 'hatao', 'chuno', 'badlo'
        }
        
        # REPL commands should NOT be corrected
        self.repl_commands = {
            'exit', 'quit', 'help', 'clear', 'vars', 'history',
            'samjhao', 'samjhao_on', 'samjhao_off', 'explain',
            'time_on', 'back', 'forward', 'timeline', 'peeche', 'aage'
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
