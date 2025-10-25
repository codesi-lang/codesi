# Changelog

All notable changes to the Codesi Programming Language will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.0.1] 

### 🎉 Initial Release

The first production-ready release of Codesi Programming Language!

#### ✨ Added

**Core Language Features**
- Complete Hinglish syntax implementation
- Full lexer and parser system
- AST-based interpreter
- Support for all basic data types (integers, floats, strings, booleans, null)
- Dynamic typing system
- Variable scoping with scope stack

**Control Flow**
- If-else-elif statements
- While loops
- Do-while loops
- For loops (multiple syntax variants)
- ForEach loops with `har ... mein` syntax
- Break and continue statements
- Switch-case statements with pattern matching
- Ternary operators

**Functions**
- Function definitions with `karya` keyword
- Return statements with `vapas`
- Default parameters
- Variadic parameters (`...args`)
- Type annotations for parameters
- Lambda functions with arrow syntax
- Function closures
- Recursive functions

**Object-Oriented Programming**
- Class definitions with `class` keyword
- Constructors with `banao` keyword
- Instance methods
- Static methods
- Inheritance with `extends`
- Method overriding
- `ye` keyword for self-reference
- `super` keyword for parent access
- Object instantiation with `new`

**Data Structures**
- Arrays with comprehensive methods:
  - `push()`, `pop()`, `shift()`, `unshift()`
  - `map()`, `filter()`, `reduce()`
  - `join()`, `slice()`, `reverse()`, `sort()`
- Object literals with key-value pairs
- Nested data structures support
- Index access for arrays and objects
- Member access with dot notation
- Index and member assignment

**Built-in Functions**

*Input/Output*
- `likho()` - Print output
- `input_lo()` - String input
- `int_lo()` - Integer input
- `float_lo()` - Float input

*Math Operations*
- `math_absolute()` - Absolute value
- `math_square()` - Square root
- `math_power()` - Power function
- `math_random()` - Random numbers
- `math_niche()` - Floor function
- `math_upar()` - Ceil function
- `math_gol()` - Rounding
- Trigonometric functions (sin, cos, tan)
- Logarithmic functions (log, exp)

*Type Checking*
- `prakar()` / `type_of()` - Get type
- `string_hai()` - Check if string
- `array_hai()` - Check if array
- `int_hai()` - Check if integer
- `float_hai()` - Check if float
- `bool_hai()` - Check if boolean
- `obj_hai()` - Check if object

*Type Conversion*
- `string_bnao()` - Convert to string
- `int_bnao()` - Convert to integer
- `float_bnao()` - Convert to float
- `bool_bnao()` - Convert to boolean

*Utility Functions*
- `lambai()` - Get length
- `range()` - Create number ranges
- `repeatkr()` - Repeat strings

*File Operations*
- `file_padho()` - Read file
- `file_likho()` - Write file
- `file_append()` - Append to file
- `file_hai()` - Check file exists
- `file_delete()` - Delete file
- `file_copy()` - Copy file
- `file_move()` - Move file
- `file_size()` - Get file size
- `dir_banao()` - Create directory
- `dir_list()` - List directory contents

*JSON Operations*
- `json_parse()` - Parse JSON string
- `json_stringify()` - Convert to JSON

*Time Operations*
- `time_now()` - Current timestamp
- `time_sleep()` - Sleep/pause execution

**String Methods**
- `lambai()` - Length
- `bada_karo()` - Uppercase
- `chota_karo()` - Lowercase
- `saaf_karo()` - Trim whitespace
- `todo()` - Split string
- `badlo()` - Replace first occurrence
- `sab_badlo()` - Replace all occurrences
- `included_hai()` - Check if substring exists
- `start_hota_hai()` - Check prefix
- `end_hota_hai()` - Check suffix

**Error Handling**
- Try-catch-finally blocks
- Throw statements
- Custom error messages
- Exception propagation
- Smart error messages in Hinglish

**World-First Features**

*🪄 JAADU Auto-Correction System*
- Automatic typo detection in function names
- Context-aware suggestions
- Intelligent word matching (60%+ similarity)
- Personalized error hints
- Enable with `--jaadu` flag
- Respects REPL commands (no false corrections)

*🧠 Samjho Code Explainer*
- `samjhao_on()` - Enable explanation mode
- `samjhao_off()` - Disable explanations
- `samjhao()` - View collected explanations
- Explains assignments, operations, conditions
- Tracks if-elif-else logic
- Loop iteration tracking
- Function call tracking
- Return value explanations
- No AI/ML models required!

*⏰ Time Machine Debugger*
- `time_machine_on(max=100)` - Activate with snapshot limit
- `time_machine_off()` - Deactivate
- `time_machine_status()` - Check status
- `peeche(steps)` - Travel backward
- `aage(steps)` - Travel forward
- `timeline()` - View complete execution history
- Automatic snapshot creation
- Variable state restoration
- Deep copy support for arrays/objects
- Configurable snapshot limits

**REPL (Interactive Mode)**
- Multi-line input support (auto-detect `{}`)
- Command history (`!!` for last, `!n` for specific)
- `help()` - Show help
- `vars()` - List all variables
- `history()` - View command history
- `clear()` - Clear screen
- `exit()` / `quit()` - Exit REPL
- JAADU mode support in REPL
- Smart error recovery
- Variable persistence across commands
- Professional prompt design

**Operators**
- Arithmetic: `+`, `-`, `*`, `/`, `%`, `**` (power)
- Comparison: `==`, `!=`, `<`, `>`, `<=`, `>=`
- Logical: `aur` (and), `ya` (or), `nahi` (not)
- Assignment: `=`
- Compound assignment: `+=`, `-=`, `*=`, `/=`

**Keywords**
- Control: `agar`, `nahi_to`, `ya_phir`, `jabtak`, `karo`, `har`
- Functions: `karya`, `vapas`, `lambda`
- OOP: `class`, `banao`, `ye`, `super`, `extends`, `static`, `new`
- Error handling: `try`, `catch`, `finally`, `throw`
- Values: `sach`, `jhooth`, `khaali`
- Logic: `aur`, `ya`, `nahi`
- Loops: `se`, `tak`, `mein`, `ke`, `liye`
- Switch: `case`, `default`
- Others: `break`, `continue`, `const`

**Command-Line Interface**
- `python codesi_production.py` - Start REPL
- `python codesi_production.py file.cds` - Run file
- `--jaadu` flag - Enable auto-correction
- `--debug` / `-d` - Debug mode (tokens + AST)
- `--help` / `-h` - Show help
- `--version` / `-v` - Show version

**Documentation**
- Comprehensive README.md
- Installation guide
- Quick start guide
- Complete syntax reference
- Built-in functions documentation
- Multiple learning paths (Basics → Intermediate → Advanced)
- Example programs

**Code Quality**
- Single-file architecture (~2,500 lines)
- Zero external dependencies
- Clean code structure with dataclasses
- Type hints throughout
- Comprehensive error handling
- Production-ready exception system

**Performance**
- Efficient lexer with O(n) tokenization
- Optimized parser with recursive descent
- Scope stack for fast variable lookup
- Deep copy optimization for Time Machine
- Snapshot limit management

#### 🐛 Fixed
- Index assignment for arrays and objects
- Member assignment for object properties
- Proper error messages for invalid assignments
- Float conversion handling for strings
- Array method snapshot tracking
- Escape sequence handling in strings
- Expression validation in assignments

#### 🔒 Security
- Input sanitization for file operations
- Safe eval (no Python eval() used)
- Controlled scope access
- Error message sanitization

#### ⚡ Performance
- Optimized token matching
- Efficient scope chain traversal
- Smart snapshot management with limits
- Minimal memory footprint

---

## Version History Overview

| Version | Release Date | Highlights |
|---------|--------------|------------|
| 0.0.1 | 2025-10-XX | 🎉 Initial production release |

---

## Migration Guides

### From Pre-release to 0.0.1
No migration needed - this is the first stable release!

---

## Contributors

### v0.0.1
- **Rishaank Gupta** ([@rishaankgupta](https://github.com/theLostB)) - Founder and Lead Developer
  - Complete language design and implementation
  - World-first features: JAADU, Samjho, Time Machine
  - Documentation and examples
  - Built entirely on mobile phone at age 15

---

## Release Notes Format

Each release follows this structure:
- **Added**: New features
- **Changed**: Changes to existing functionality
- **Deprecated**: Soon-to-be removed features
- **Removed**: Removed features
- **Fixed**: Bug fixes
- **Security**: Security improvements

---

## Support

For questions about specific versions:
- Check the [Documentation](docs/)
- Open an [Issue](https://github.com/codesi-lang)
- Join our community discussions

---

**Note**: This changelog follows [Semantic Versioning](https://semver.org/):
- **Major** (X.0.0): Breaking changes
- **Minor** (0.X.0): New features, backward compatible
- **Patch** (0.0.X): Bug fixes, backward compatible