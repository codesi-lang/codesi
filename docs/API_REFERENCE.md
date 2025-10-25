# API Reference - Quick Lookup

Complete alphabetical reference for Codesi Programming Language.

## 📋 Quick Navigation

- [Keywords](#keywords)
- [Operators](#operators)
- [Built-in Functions](#built-in-functions)
- [Data Types](#data-types)
- [Array Methods](#array-methods)
- [String Methods](#string-methods)
- [Object Methods](#object-methods)
- [Special Features](#special-features)

---

## 🔤 Keywords

| Keyword | Purpose | Example |
|---------|---------|---------|
| `agar` | If statement | `agar (x > 5) { }` |
| `aur` | Logical AND | `(a aur b)` |
| `banao` | Constructor | `banao(naam) { }` |
| `break` | Exit loop | `break` |
| `case` | Switch case | `x ke case mein { }` |
| `catch` | Catch error | `catch (e) { }` |
| `class` | Define class | `class Person { }` |
| `const` | Constant | `const PI = 3.14` |
| `continue` | Skip iteration | `continue` |
| `default` | Default case | `default -> likho("...")` |
| `extends` | Inheritance | `class Dog extends Animal` |
| `finally` | Finally block | `finally { }` |
| `har` | For/ForEach | `har i se 1 tak 10 { }` |
| `jabtak` | While loop | `jabtak (x < 10) { }` |
| `jhooth` | False | `is_valid = jhooth` |
| `karo` | Do-while | `karo { } jabtak (...)` |
| `karya` | Function | `karya naam() { }` |
| `ke` | Possessive | `har i ke liye` |
| `khaali` | Null/None | `value = khaali` |
| `lambda` | Lambda function | `lambda(x) -> x * 2` |
| `liye` | For (in loops) | `ke liye` |
| `mein` | In (loops) | `har x mein arr` |
| `nahi` | Logical NOT | `nahi condition` |
| `nahi_to` | Else | `nahi_to { }` |
| `new` | Create instance | `new Person()` |
| `sach` | True | `is_valid = sach` |
| `se` | From (loops) | `har i se 0` |
| `static` | Static method | `static karya func() { }` |
| `super` | Parent class | `super.banao()` |
| `tak` | To (loops) | `se 0 tak 10` |
| `throw` | Throw error | `throw {message: "..."}` |
| `try` | Try block | `try { }` |
| `vapas` | Return | `vapas result` |
| `ya` | Logical OR | `(a ya b)` |
| `ya_phir` | Else if | `ya_phir (x < 5) { }` |
| `ye` | This/Self | `ye.naam = "Raj"` |

---

## ➕ Operators

### Arithmetic Operators

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `10 + 5` | `15` |
| `-` | Subtraction | `10 - 5` | `5` |
| `*` | Multiplication | `10 * 5` | `50` |
| `/` | Division | `10 / 5` | `2.0` |
| `%` | Modulo | `10 % 3` | `1` |
| `**` | Power | `2 ** 3` | `8` |

### Comparison Operators

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `==` | Equal to | `5 == 5` | `sach` |
| `!=` | Not equal | `5 != 3` | `sach` |
| `<` | Less than | `3 < 5` | `sach` |
| `>` | Greater than | `5 > 3` | `sach` |
| `<=` | Less or equal | `5 <= 5` | `sach` |
| `>=` | Greater or equal | `5 >= 5` | `sach` |

### Logical Operators

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `aur` | AND | `sach aur sach` | `sach` |
| `ya` | OR | `sach ya jhooth` | `sach` |
| `nahi` | NOT | `nahi sach` | `jhooth` |

### Assignment Operators

| Operator | Name | Example | Equivalent |
|----------|------|---------|------------|
| `=` | Assign | `x = 10` | - |
| `+=` | Add assign | `x += 5` | `x = x + 5` |
| `-=` | Subtract assign | `x -= 5` | `x = x - 5` |
| `*=` | Multiply assign | `x *= 5` | `x = x * 5` |
| `/=` | Divide assign | `x /= 5` | `x = x / 5` |

### Other Operators

| Operator | Name | Example |
|----------|------|---------|
| `? :` | Ternary | `(x > 5) ? "Big" : "Small"` |
| `[]` | Index access | `arr[0]`, `obj["key"]` |
| `.` | Member access | `obj.naam`, `arr.length` |
| `()` | Function call | `func(arg1, arg2)` |

---

## 🔧 Built-in Functions

### Input/Output

| Function | Purpose | Example |
|----------|---------|---------|
| `likho(...values)` | Print output | `likho("Hello", naam)` |
| `input_lo(prompt)` | String input | `naam = input_lo("Name: ")` |
| `int_lo(prompt)` | Integer input | `age = int_lo("Age: ")` |
| `float_lo(prompt)` | Float input | `price = float_lo("Price: ")` |

### Math Functions

| Function | Purpose | Example |
|----------|---------|---------|
| `math_absolute(n)` | Absolute value | `math_absolute(-10)` → `10` |
| `math_square(n)` | Square root | `math_square(16)` → `4.0` |
| `math_power(base, exp)` | Power | `math_power(2, 3)` → `8` |
| `math_random(min, max)` | Random int | `math_random(1, 10)` |
| `math_niche(n)` | Floor | `math_niche(4.7)` → `4` |
| `math_upar(n)` | Ceiling | `math_upar(4.2)` → `5` |
| `math_gol(n, decimals)` | Round | `math_gol(4.567, 2)` → `4.57` |
| `math_sin(n)` | Sine | `math_sin(pi/2)` → `1.0` |
| `math_cos(n)` | Cosine | `math_cos(0)` → `1.0` |
| `math_tan(n)` | Tangent | `math_tan(pi/4)` |
| `math_log(n)` | Natural log | `math_log(2.71828)` |
| `math_exp(n)` | Exponential | `math_exp(1)` → `2.71828` |

### Type Functions

| Function | Purpose | Example |
|----------|---------|---------|
| `prakar(value)` | Get type | `prakar(10)` → `"Integer"` |
| `type_of(value)` | Get type | `type_of("hi")` → `"shabd"` |
| `string_hai(v)` | Is string? | `string_hai("hi")` → `sach` |
| `array_hai(v)` | Is array? | `array_hai([1,2])` → `sach` |
| `int_hai(v)` | Is integer? | `int_hai(10)` → `sach` |
| `float_hai(v)` | Is float? | `float_hai(3.14)` → `sach` |
| `bool_hai(v)` | Is boolean? | `bool_hai(sach)` → `sach` |
| `obj_hai(v)` | Is object? | `obj_hai({a:1})` → `sach` |

### Type Conversion

| Function | Purpose | Example |
|----------|---------|---------|
| `string_bnao(v)` | To string | `string_bnao(123)` → `"123"` |
| `int_bnao(v)` | To integer | `int_bnao("123")` → `123` |
| `float_bnao(v)` | To float | `float_bnao("3.14")` → `3.14` |
| `bool_bnao(v)` | To boolean | `bool_bnao(1)` → `sach` |

### Utility Functions

| Function | Purpose | Example |
|----------|---------|---------|
| `lambai(v)` | Length | `lambai("hello")` → `5` |
| `range(start, end)` | Number range | `range(0, 5)` → `[0,1,2,3,4]` |
| `repeatkr(s, n)` | Repeat string | `repeatkr("*", 5)` → `"*****"` |

### File Operations

| Function | Purpose | Example |
|----------|---------|---------|
| `file_padho(path)` | Read file | `content = file_padho("data.txt")` |
| `file_likho(path, content)` | Write file | `file_likho("out.txt", "Hello")` |
| `file_append(path, content)` | Append file | `file_append("log.txt", "Entry")` |
| `file_hai(path)` | File exists? | `file_hai("data.txt")` → `sach` |
| `file_delete(path)` | Delete file | `file_delete("temp.txt")` |
| `file_copy(src, dst)` | Copy file | `file_copy("a.txt", "b.txt")` |
| `file_move(src, dst)` | Move file | `file_move("old.txt", "new.txt")` |
| `file_size(path)` | File size | `file_size("data.txt")` → `1024` |
| `dir_banao(path)` | Create dir | `dir_banao("output")` |
| `dir_list(path)` | List dir | `dir_list(".")` → `[...]` |

### JSON Operations

| Function | Purpose | Example |
|----------|---------|---------|
| `json_parse(str)` | Parse JSON | `json_parse('{"a":1}')` |
| `json_stringify(obj)` | To JSON | `json_stringify({a:1})` |

### Time Functions

| Function | Purpose | Example |
|----------|---------|---------|
| `time_now()` | Current time | `time_now()` → `1234567890.0` |
| `time_sleep(seconds)` | Sleep/pause | `time_sleep(2)` |

---

## 📦 Data Types

### Numbers

```codesi
// Integer
age = 15
count = -10

// Float
price = 99.99
pi = 3.14159
```

### Strings

```codesi
// Creation
naam = "Rishaank"
message = 'Hello'

// Escape sequences
text = "Line 1\nLine 2"
path = "C:\\Users\\Name"
```

### Booleans

```codesi
is_valid = sach      // True
is_active = jhooth   // False
```

### Null

```codesi
value = khaali  // None/Null
```

### Arrays

```codesi
// Creation
arr = []
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", sach]

// Access
first = arr[0]
last = arr[-1]

// Modify
arr[0] = 10
```

### Objects

```codesi
// Creation
obj = {}
person = {
    naam: "Raj",
    umra: 25,
    city: "Mumbai"
}

// Access
naam = person.naam
umra = person["umra"]

// Modify
person.email = "raj@example.com"
```

---

## 📊 Array Methods

| Method | Purpose | Example |
|--------|---------|---------|
| `push(item)` | Add to end | `arr.push(4)` |
| `pop()` | Remove from end | `last = arr.pop()` |
| `shift()` | Remove from start | `first = arr.shift()` |
| `unshift(item)` | Add to start | `arr.unshift(0)` |
| `lambai()` | Get length | `len = arr.lambai()` |
| `map(func)` | Transform | `doubled = arr.map(lambda(x) -> x*2)` |
| `filter(func)` | Filter | `even = arr.filter(lambda(x) -> x%2==0)` |
| `reduce(func, init)` | Reduce | `sum = arr.reduce(lambda(a,x) -> a+x, 0)` |
| `join(sep)` | Join to string | `text = arr.join(", ")` |
| `slice(start, end)` | Extract portion | `subset = arr.slice(1, 4)` |
| `reverse()` | Reverse array | `arr.reverse()` |
| `sort()` | Sort array | `arr.sort()` |

**Hinglish Aliases:**
- `dalo` = `push`
- `nikalo` = `pop`
- `pehla_nikalo` = `shift`
- `pehle_dalo` = `unshift`
- `badlo` = `map`
- `chuno` = `filter`
- `jodo` = `join`
- `cutkr` = `slice`
- `ulta` = `reverse`
- `arrange` = `sort`

---

## 📝 String Methods

| Method | Purpose | Example |
|--------|---------|---------|
| `lambai()` | Length | `"hello".lambai()` → `5` |
| `bada_karo()` | Uppercase | `"hello".bada_karo()` → `"HELLO"` |
| `chota_karo()` | Lowercase | `"HELLO".chota_karo()` → `"hello"` |
| `saaf_karo()` | Trim whitespace | `"  hi  ".saaf_karo()` → `"hi"` |
| `todo(sep)` | Split | `"a,b,c".todo(",")` → `["a","b","c"]` |
| `badlo(old, new)` | Replace first | `"hello".badlo("l", "L")` → `"heLlo"` |
| `sab_badlo(old, new)` | Replace all | `"hello".sab_badlo("l", "L")` → `"heLLo"` |
| `included_hai(sub)` | Contains? | `"hello".included_hai("ell")` → `sach` |
| `start_hota_hai(pre)` | Starts with? | `"hello".start_hota_hai("he")` → `sach` |
| `end_hota_hai(suf)` | Ends with? | `"hello".end_hota_hai("lo")` → `sach` |

---

## 🗂️ Object Methods

| Method | Purpose | Example |
|--------|---------|---------|
| `keys()` | Get keys | `obj.keys()` → `["naam", "umra"]` |
| `values()` | Get values | `obj.values()` → `["Raj", 25]` |
| `items()` | Get key-value pairs | `obj.items()` → `[["naam","Raj"]]` |
| `hai_kya(key)` | Has key? | `obj.hai_kya("naam")` → `sach` |

---

## 🌟 Special Features

### JAADU (Auto-Correction)

```bash
# Enable JAADU mode
python codesi_production.py --jaadu

# Or in file
python codesi_production.py script.cds --jaadu
```

**Features:**
- Auto-corrects typos in function names
- 60%+ similarity matching
- Suggests corrections in default mode

### Samjho (Code Explainer)

| Function | Purpose | Example |
|----------|---------|---------|
| `samjhao_on()` | Enable explainer | `samjhao_on()` |
| `samjhao_off()` | Disable explainer | `samjhao_off()` |
| `samjhao()` | Show explanations | `samjhao()` |

**Explains:**
- Variable assignments
- Operations
- Conditions
- Loops
- Function calls

### Time Machine (Time-Travel Debugger)

| Function | Purpose | Example |
|----------|---------|---------|
| `time_machine_on(max)` | Enable | `time_machine_on()` |
| `time_machine_off()` | Disable | `time_machine_off()` |
| `time_machine_status()` | Check status | `time_machine_status()` |
| `peeche(steps)` | Go back | `peeche()` or `peeche(3)` |
| `aage(steps)` | Go forward | `aage()` or `aage(2)` |
| `timeline()` | View history | `timeline()` |

**Features:**
- Records execution snapshots
- Restores variable states
- Configurable snapshot limit (default: 100)
- Deep copy support for arrays/objects

---

## 📖 Syntax Quick Reference

### Variables

```codesi
// Declaration
naam = "Rishaank"
age = 15

// Constants
const PI = 3.14159
```

### If-Else

```codesi
// Simple if
agar (condition) {
    // code
}

// If-else
agar (condition) {
    // code
} nahi_to {
    // code
}

// If-elif-else
agar (condition1) {
    // code
} ya_phir (condition2) {
    // code
} nahi_to {
    // code
}

// Ternary
result = (condition) ? value1 : value2
```

### Loops

```codesi
// For loop
har i se 0 tak 5 {
    likho(i)
}

// For loop (with parens)
har i ke liye (0 se 5 tak) {
    likho(i)
}

// ForEach
har item mein array {
    likho(item)
}

// While
jabtak (condition) {
    // code
}

// Do-While
karo {
    // code
} jabtak (condition)
```

### Functions

```codesi
// Basic function
karya naam(param1, param2) {
    // code
    vapas result
}

// Default parameters
karya naam(param = default_value) {
    // code
}

// Variadic parameters
karya naam(...params) {
    // code
}

// Lambda
func = lambda(x) -> x * 2
```

### Classes

```codesi
// Basic class
class ClassName {
    banao(param1, param2) {
        ye.property = param1
    }
    
    karya method() {
        // code
    }
}

// Inheritance
class Child extends Parent {
    banao(param) {
        super.banao(param)
    }
}

// Static method
class ClassName {
    static karya method() {
        // code
    }
}

// Create instance
obj = new ClassName(args)
```

### Switch-Case

```codesi
variable ke case mein {
    value1 -> statement
    value2 -> statement
    default -> statement
}
```

### Error Handling

```codesi
// Try-catch
try {
    // code
} catch (e) {
    likho("Error:", e.message)
}

// Try-catch-finally
try {
    // code
} catch (e) {
    // error handling
} finally {
    // cleanup
}

// Throw
throw {message: "Error message"}
```

---

## 🎨 Code Examples

### Hello World

```codesi
likho("Namaste Duniya!")
```

### Variables and Output

```codesi
naam = "Rishaank"
umra = 15
likho("Mera naam", naam, "hai")
likho("Main", umra, "saal ka hun")
```

### If-Else

```codesi
age = 20
agar (age >= 18) {
    likho("Adult")
} nahi_to {
    likho("Minor")
}
```

### Loop

```codesi
har i se 1 tak 6 {
    likho("Number:", i)
}
```

### Function

```codesi
karya add(a, b) {
    vapas a + b
}

result = add(5, 3)
likho(result)  // 8
```

### Array Operations

```codesi
arr = [1, 2, 3, 4, 5]
doubled = arr.map(lambda(x) -> x * 2)
likho(doubled)  // [2, 4, 6, 8, 10]
```

### Class

```codesi
class Person {
    banao(naam, umra) {
        ye.naam = naam
        ye.umra = umra
    }
    
    karya introduce() {
        likho("Main", ye.naam, "hun")
    }
}

person = new Person("Raj", 25)
person.introduce()
```

---

## 🔍 REPL Commands

| Command | Purpose |
|---------|---------|
| `help()` | Show help |
| `vars()` | List all variables |
| `history()` | Show command history |
| `clear()` | Clear screen |
| `exit()` | Exit REPL |
| `quit()` | Exit REPL |
| `!!` | Repeat last command |
| `!n` | Repeat command #n |

---

## 📊 Operator Precedence (Highest to Lowest)

1. `()` - Parentheses
2. `**` - Power
3. `*`, `/`, `%` - Multiplication, Division, Modulo
4. `+`, `-` - Addition, Subtraction
5. `<`, `>`, `<=`, `>=` - Comparison
6. `==`, `!=` - Equality
7. `nahi` - Logical NOT
8. `aur` - Logical AND
9. `ya` - Logical OR
10. `? :` - Ternary
11. `=`, `+=`, `-=`, etc. - Assignment

---

## 🎯 Common Patterns

### Input Validation

```codesi
age = int_lo("Enter age: ")
agar (age < 0 ya age > 150) {
    likho("Invalid age")
}
```

### Array Iteration

```codesi
har item mein array {
    likho(item)
}
```

### Error Handling

```codesi
try {
    result = risky_operation()
} catch (e) {
    likho("Error:", e.message)
}
```

### File Read/Write

```codesi
// Read
content = file_padho("data.txt")

// Write
file_likho("output.txt", "Hello")
```

### Type Checking

```codesi
agar (string_hai(value)) {
    likho("It's a string")
}
```

---

## 📝 Naming Conventions

### Variables & Functions
- Use snake_case: `student_name`, `calculate_total`
- Descriptive names: `total_marks` not `tm`

### Classes
- Use PascalCase: `StudentRecord`, `BankAccount`

### Constants
- Use UPPER_CASE: `MAX_SIZE`, `PI`

### Private/Internal
- Prefix with underscore: `_internal_function`

---

## 🚀 Performance Tips

1. **Disable features when not needed:**
   ```codesi
   samjhao_off()
   time_machine_off()
   ```

2. **Use iterative instead of recursive (when possible):**
   ```codesi
   // Faster
   karya fibonacci_iterative(n) { ... }
   
   // Slower
   karya fibonacci_recursive(n) { ... }
   ```

3. **Avoid large Time Machine limits:**
   ```codesi
   time_machine_on(50)  // Instead of 1000
   ```

4. **Use appropriate data structures:**
   ```codesi
   // For lookup: Use objects (O(1))
   // For ordered data: Use arrays
   ```

---

## 🔗 See Also

- [Complete Syntax Guide](SYNTAX_GUIDE.md)
- [Built-in Functions](BUILTIN_FUNCTIONS.md)
- [Data Types](DATA_TYPES.md)
- [Advanced Features](ADVANCED_FEATURES.md)
- [Troubleshooting](TROUBLESHOOTING.md)

---

## 💡 Quick Tips

- **Comments:** Use `//` for single-line comments
- **Multi-line:** Braces `{}` auto-detect in REPL
- **Semicolons:** Optional but recommended
- **Case-sensitive:** `naam` ≠ `Naam`
- **Hinglish:** Mix Hindi and English naturally
- **JAADU:** Enable with `--jaadu` flag for auto-correction

---

**Bookmark this page for quick reference! 📌**