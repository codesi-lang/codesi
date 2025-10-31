import difflib
import re
from functools import lru_cache

class CodesiJaadu:
    """World's first context-aware programming language auto-correction - Enhanced Edition"""
    
    def __init__(self):
        # Separate keywords from functions (Issue #7 & #8)
        self.keywords = {
            'agar', 'nahi_to', 'ya_phir', 'jabtak', 'liye', 'karo',
            'karya', 'vapas', 'break', 'continue', 'class', 'banao',
            'ye', 'super', 'extends', 'new', 'try', 'catch', 'finally',
            'throw', 'lambda', 'se', 'tak', 'mein', 'ke', 'sach', 'jhooth',
            'khaali', 'aur', 'ya', 'nahi', 'case', 'default', 'static',
            'as', 'in', 'const', 'har'
        }
        
        # Built-in functions (Issue #4 - removed 'batao', removed 'lo')
        self.builtin_functions = {
            'likho', 'input_lo', 'float_lo', 'int_lo',
            'time_machine_status', 'time_machine_on', 'time_machine_off', 
            'peeche', 'aage', 'timeline',
            'samjhao_on', 'samjhao_off', 'samjhao',
            'import_karo',
            'math_absolute', 'math_square', 'math_power', 'math_random', 
            'math_niche', 'math_upar', 'math_gol', 'math_sin', 'math_cos', 
            'math_tan', 'math_log', 'math_exp',
            'type_of', 'prakar', 'string_hai', 'array_hai', 'int_hai', 
            'float_hai', 'bool_hai', 'obj_hai',
            'string_bnao', 'float_bnao', 'int_bnao', 'bool_bnao',
            'lambai', 'range', 'repeatkr',
            'file_padho', 'file_likho', 'file_append', 'file_hai', 
            'file_delete', 'file_copy', 'file_move', 'file_size',
            'dir_banao', 'dir_list',
            'json_stringify', 'json_parse',
            'time_now', 'time_sleep'
        }
        
        # Array methods - both English and Hindi (Issue #4)
        self.array_methods = {
            'push', 'dalo', 'pop', 'nikalo', 
            'shift', 'pehla_nikalo', 'unshift', 'pehle_dalo',
            'map', 'badlo', 'filter', 'chuno', 
            'reduce', 'combine', 'join', 'jodo',
            'slice', 'cutkr', 'reverse', 'ulta', 
            'sort', 'arrange', 'lambai', 'size'
        }
        
        # String methods (Issue #5)
        self.string_methods = {
            'lambai', 'size', 'bada_karo', 'chota_karo', 'saaf_karo',
            'todo', 'badlo', 'sab_badlo', 'included_hai',
            'start_hota_hai', 'end_hota_hai'
        }
        
        # Object/Dict methods (Issue #5)
        self.object_methods = {
            'keys', 'values', 'items', 'hai_kya'
        }
        
        # REPL commands should NOT be corrected
        self.repl_commands = {
            'exit', 'quit', 'help', 'clear', 'vars', 'history',
            'qhelp', 'credits', 'copyright', 'license'
        }
        
        # All methods combined for easy lookup
        self.all_methods = self.array_methods | self.string_methods | self.object_methods
        
        # All valid identifiers
        self.all_valid = self.keywords | self.builtin_functions | self.all_methods
        
        # Phonetic mapping for Hindi/English sounds (Issue #17)
        self.phonetic_map = {
            'ph': 'f', 'gh': 'g', 'kh': 'k', 'ch': 'c',
            'aa': 'a', 'ee': 'i', 'oo': 'u', 'ae': 'e',
            'th': 't', 'dh': 'd', 'bh': 'b'
        }
        
        # Correction cache for performance (Issue #22)
        self._correction_cache = {}
    
    def _normalize_phonetic(self, word):
        """Normalize phonetic variations (Issue #17)"""
        normalized = word.lower()
        for phonetic, simple in self.phonetic_map.items():
            normalized = normalized.replace(phonetic, simple)
        return normalized
    
    def _calculate_confidence(self, word, suggestion):
        """Calculate confidence score for suggestion (Issue #18)"""
        word_lower = word.lower()
        suggestion_lower = suggestion.lower()
        
        # Exact match (case-insensitive)
        if word_lower == suggestion_lower:
            return 100
        
        # Calculate edit distance ratio
        similarity = difflib.SequenceMatcher(None, word_lower, suggestion_lower).ratio()
        base_confidence = int(similarity * 100)
        
        # Boost for phonetic similarity (Issue #17)
        if self._normalize_phonetic(word) == self._normalize_phonetic(suggestion):
            base_confidence = min(95, base_confidence + 15)
        
        # Boost for common prefixes (user typed beginning correctly)
        if word_lower.startswith(suggestion_lower[:3]) or suggestion_lower.startswith(word_lower[:3]):
            base_confidence = min(98, base_confidence + 10)
        
        return base_confidence
    
    @lru_cache(maxsize=512)  # Performance optimization (Issue #22)
    def _get_ranked_suggestions(self, wrong_word, context='general', max_suggestions=3):
        """
        Get ranked suggestions with confidence scores (Issue #18, #19, #14)
        Context-aware correction (Issue #14)
        """
        wrong_lower = wrong_word.lower()
        
        # Check cache first (Issue #22)
        cache_key = f"{wrong_word}:{context}"
        if cache_key in self._correction_cache:
            return self._correction_cache[cache_key]
        
        # Context-aware candidate selection (Issue #14)
        if context == 'method':
            candidates = self.all_methods
        elif context == 'function':
            candidates = self.builtin_functions
        elif context == 'keyword':
            candidates = self.keywords
        else:
            candidates = self.all_valid
        
        # Multi-typo detection with lower cutoff (Issue #19)
        # Use both standard and phonetic matching
        standard_matches = difflib.get_close_matches(
            wrong_word, candidates, n=max_suggestions * 2, cutoff=0.5
        )
        
        # Phonetic matching for sound-alike words (Issue #17)
        phonetic_word = self._normalize_phonetic(wrong_word)
        phonetic_matches = []
        for candidate in candidates:
            if self._normalize_phonetic(candidate) == phonetic_word:
                if candidate not in standard_matches:
                    phonetic_matches.append(candidate)
        
        # Combine and rank by confidence
        all_matches = standard_matches + phonetic_matches
        ranked = []
        
        for match in all_matches:
            confidence = self._calculate_confidence(wrong_word, match)
            if confidence >= 60:  # Threshold
                ranked.append({
                    'word': match,
                    'confidence': confidence,
                    'method': 'phonetic' if match in phonetic_matches else 'standard'
                })
        
        # Sort by confidence (descending)
        ranked.sort(key=lambda x: x['confidence'], reverse=True)
        result = ranked[:max_suggestions]
        
        # Cache result (Issue #22)
        self._correction_cache[cache_key] = result
        return result
    
    def suggest_correction(self, wrong_word, context='general'):
        """
        Find closest match for typo with context awareness (Issue #14)
        Returns best match or None
        """
        # Don't correct REPL commands
        if wrong_word.lower() in self.repl_commands:
            return None
        
        # Case-insensitive check (Issue #12)
        wrong_lower = wrong_word.lower()
        
        # Check if it's already valid (any case)
        for valid_word in self.all_valid:
            if valid_word.lower() == wrong_lower:
                return None  # Already correct
        
        suggestions = self._get_ranked_suggestions(wrong_word, context, max_suggestions=1)
        
        if suggestions and suggestions[0]['confidence'] >= 60:
            return suggestions[0]['word']
        return None
    
    def suggest_with_confidence(self, wrong_word, context='general', max_suggestions=3):
        """
        Get multiple suggestions with confidence scores (Issue #18)
        For IDE integration and user choice
        """
        if wrong_word.lower() in self.repl_commands:
            return []
        
        return self._get_ranked_suggestions(wrong_word, context, max_suggestions)
    
    def _detect_context(self, code, position):
        """
        Detect context at position for syntax-aware correction (Issue #24, #14)
        Returns: 'method', 'function', 'keyword', or 'general'
        """
        # Check if after a dot (method call) - Issue #23
        before = code[:position].rstrip()
        if before.endswith('.'):
            return 'method'
        
        # Check if followed by parenthesis (function call)
        after = code[position:].lstrip()
        if after.startswith('('):
            return 'function'
        
        # Check if in keyword position (beginning of statement, after {, etc.)
        if not before or before[-1] in '{};':
            return 'keyword'
        
        return 'general'
    
    def _is_inside_string(self, code, position):
        """Check if position is inside a string literal"""
        # Count quotes before position
        before = code[:position]
        double_quotes = before.count('"') - before.count('\\"')
        single_quotes = before.count("'") - before.count("\\'")
        
        # Odd number means we're inside a string
        return (double_quotes % 2 == 1) or (single_quotes % 2 == 1)
    
    def _extract_identifiers(self, code):
        """
        Extract all identifiers with context (Issue #24, #23)
        Returns list of (identifier, context, position)
        """
        identifiers = []
        
        # Method calls (after dot) - Issue #23
        # Pattern: something.method()
        for match in re.finditer(r'\.([a-zA-Z_][a-zA-Z0-9_]*)\s*\(', code):
            # Skip if inside string
            if self._is_inside_string(code, match.start()):
                continue
            identifiers.append({
                'word': match.group(1),
                'context': 'method',
                'position': match.start(1),
                'full_match': match.group(0)
            })
        
        # Function calls (not after dot) - Issue #11
        # Pattern: function() but not .function()
        for match in re.finditer(r'(?<![.\w])([a-zA-Z_][a-zA-Z0-9_]*)\s*\(', code):
            # Skip if inside string
            if self._is_inside_string(code, match.start()):
                continue
            # Skip if this is actually a method (after dot)
            if match.start() > 0 and code[match.start() - 1] == '.':
                continue
            identifiers.append({
                'word': match.group(1),
                'context': 'function',
                'position': match.start(1),
                'full_match': match.group(0)
            })
        
        # Keywords at statement beginnings (Issue #11)
        for match in re.finditer(r'(?:^|[{};]\s*)([a-zA-Z_][a-zA-Z0-9_]*)', code, re.MULTILINE):
            # Skip if inside string
            if self._is_inside_string(code, match.start()):
                continue
            word = match.group(1)
            # Only if it might be a keyword
            if word.lower() in {'agar', 'jabtak', 'karya', 'class', 'har', 'vapas', 'try', 'throw'}:
                identifiers.append({
                    'word': word,
                    'context': 'keyword',
                    'position': match.start(1),
                    'full_match': match.group(0)
                })
        
        return identifiers
    
    def auto_fix_code(self, code):
        """
        Automatically fix common typos in code (Enhanced version)
        Handles: method chains, context-awareness, case-insensitivity (Issues #23, #24, #12, #10)
        """
        # Skip REPL special commands
        stripped = code.strip()
        if stripped.startswith('!') or stripped.startswith('.'):
            return code, []
        
        # Check if it's just a REPL command
        first_word = stripped.split('(')[0].split()[0] if stripped else ''
        if first_word.lower() in self.repl_commands:
            return code, []
        
        # Extract all identifiers with context (Issue #24, #23)
        identifiers = self._extract_identifiers(code)
        
        fixes = []
        fixed_code = code
        
        for item in identifiers:
            word = item['word']
            context = item['context']
            
            # Skip if already valid (case-insensitive check) - Issue #12
            if any(word.lower() == valid.lower() for valid in self.all_valid):
                continue
            
            # Skip REPL commands
            if word.lower() in self.repl_commands:
                continue
            
            # Get context-aware suggestion (Issue #14)
            suggestion = self.suggest_correction(word, context)
            
            if suggestion and suggestion != word:
                fixes.append((word, suggestion, context))
        
        # Apply fixes with proper escaping (Issue #10)
        # Process in reverse order to maintain positions
        for word, suggestion, context in reversed(fixes):
            # Use re.escape to handle special regex characters (Issue #10)
            escaped_word = re.escape(word)
            
            if context == 'method':
                # Replace .method( with .suggestion(
                pattern = r'\.' + escaped_word + r'\s*\('
                replacement = '.' + suggestion + '('
            else:
                # Replace word( with suggestion( (with word boundaries)
                pattern = r'(?<!\w)' + escaped_word + r'\s*\('
                replacement = suggestion + '('
            
            fixed_code = re.sub(pattern, replacement, fixed_code)
        
        # Return unique fixes (word, suggestion) tuples
        unique_fixes = []
        seen = set()
        for word, suggestion, context in fixes:
            if (word, suggestion) not in seen:
                unique_fixes.append((word, suggestion))
                seen.add((word, suggestion))
        
        return fixed_code, unique_fixes
    
    def clear_cache(self):
        """Clear correction cache (Issue #22)"""
        self._correction_cache.clear()
        self._get_ranked_suggestions.cache_clear()

jaadu_system = CodesiJaadu()
