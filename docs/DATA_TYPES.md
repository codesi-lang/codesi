# Data Types in Codesi

Complete guide to all data types in Codesi Programming Language.

## 📋 Table of Contents

- [Overview](#overview)
- [Numbers](#numbers)
- [Strings](#strings)
- [Booleans](#booleans)
- [Null](#null)
- [Arrays](#arrays)
- [Objects](#objects)
- [Functions](#functions)
- [Type Conversion](#type-conversion)
- [Type Checking](#type-checking)

---

## 🌟 Overview

Codesi is **dynamically typed** - variables can hold any type of value and can change types during execution.

```codesi
x = 10          // Integer
x = "hello"     // Now string
x = [1, 2, 3]   // Now array
x = sach        // Now boolean
```

### Supported Data Types

1. **Numbers** (Integer, Float)
2. **Strings** (Text)
3. **Booleans** (`sach`, `jhooth`)
4. **Null** (`khaali`)
5. **Arrays** (Lists)
6. **Objects** (Key-value pairs)
7. **Functions** (First-class functions)

---

## 🔢 Numbers

### Integers

Whole numbers without decimal points.

```codesi
age = 15
count = 100
negative = -50
zero = 0
large = 1000000
```

**Range**: Python's unlimited integer precision

### Floats (Decimals)

Numbers with decimal points.

```codesi
height = 5.8
pi = 3.14159
temperature = -2.5
small = 0.0001
```

**Precision**: 64-bit floating point (IEEE 754)

### Number Operations

```codesi
// Arithmetic
a = 10 + 5      // 15
b = 10 - 5      // 5
c = 10 * 5      // 50
d = 10 / 5      // 2.0 (always returns float)
e = 10 % 3      // 1 (remainder)
f = 2 ** 8      // 256 (power)

// Mixed int/float operations
result = 10 + 5.5    // 15.5 (promoted to float)
result = 10 / 3      // 3.333... (float division)
```

### Special Values

```codesi
// Infinity (through operations)
inf = 1.0 / 0.0  // Error: Division by zero

// NaN (Not a Number)
// Codesi throws errors instead of NaN
```

### Number Methods

```codesi
// Convert to integer
x = int_bnao(3.14)      // 3
x = int_bnao("42")      // 42

// Convert to float
y = float_bnao(5)       // 5.0
y = float_bnao("3.14")  // 3.14

// Math functions
abs_val = math_absolute(-10)     // 10
sqrt_val = math_square(16)       // 4.0
power = math_power(2, 10)        // 1024
rounded = math_gol(3.7)          // 4
```

---

## 📝 Strings

Text data enclosed in quotes (single or double).

### String Creation

```codesi
// Single quotes
naam = 'Rishaank'
message = 'Hello World'

// Double quotes
greeting = "Namaste"
text = "Hello, Codesi!"

// Both are equivalent
str1 = "hello"
str2 = 'hello'
// str1 == str2 → sach
```

### Escape Sequences

```codesi
// Newline
text = "Line 1\nLine 2"

// Tab
text = "Col1\tCol2\tCol3"

// Quotes in strings
text = "He said \"Hello\""
text = 'It\'s working'

// Backslash
path = "C:\\Users\\Rishaank"

// All escape sequences:
text = "Newline: \n"
text = "Tab: \t"
text = "Carriage return: \r"
text = "Backspace: \b"
text = "Form feed: \f"
text = "Vertical tab: \v"
text = "Backslash: \\"
text = "Null: \0"
```

### String Operations

```codesi
// Concatenation
full_name = "Rishaank" + " " + "Gupta"
greeting = "Hello " + naam

// Repetition
stars = "*" * 5              // "*****"
separator = "-" * 20

// Length
len = "hello".lambai()       // 5

// Indexing
text = "hello"
first = text[0]              // "h"
last = text[4]               // "o"

// Negative indexing
last = text[-1]              // "o"
second_last = text[-2]       // "l"
```

### String Methods

```codesi
text = "  Hello World  "

// Case conversion
upper = text.bada_karo()         // "  HELLO WORLD  "
lower = text.chota_karo()        // "  hello world  "

// Trimming
clean = text.saaf_karo()         // "Hello World"

// Splitting
words = "a,b,c".todo(",")        // ["a", "b", "c"]
words = "hello world".todo()     // ["hello", "world"]

// Replacing
new_text = text.badlo("World", "Codesi")
all_replaced = text.sab_badlo("l", "L")

// Checking
has_hello = text.included_hai("Hello")      // sach
starts = text.start_hota_hai("Hello")       // jhooth (whitespace)
ends = text.end_hota_hai("World")           // jhooth (whitespace)
```

### String Comparison

```codesi
"hello" == "hello"     // sach
"hello" != "world"     // sach
"apple" < "banana"     // sach (alphabetical)
"a" < "b"             // sach
```

### Multi-line Strings

```codesi
// Use \n for newlines
poem = "Roses are red\nViolets are blue\nCoding is fun\nCodesi is too!"
likho(poem)
```

---

## ✅ Booleans

Truth values: `sach` (true) and `jhooth` (false).

### Boolean Values

```codesi
is_adult = sach
is_minor = jhooth
has_access = sach
is_complete = jhooth
```

### Boolean Operations

```codesi
// Logical AND
sach aur sach     // sach
sach aur jhooth   // jhooth
jhooth aur jhooth // jhooth

// Logical OR
sach ya sach      // sach
sach ya jhooth    // sach
jhooth ya jhooth  // jhooth

// Logical NOT
nahi sach         // jhooth
nahi jhooth       // sach
```

### Comparison Results

```codesi
10 > 5            // sach
10 < 5            // jhooth
10 == 10          // sach
10 != 5           // sach
```

### Truthy and Falsy Values

```codesi
// Falsy values (evaluate to jhooth)
bool_bnao(0)         // jhooth
bool_bnao("")        // jhooth
bool_bnao(khaali)    // jhooth
bool_bnao([])        // jhooth (empty array)
bool_bnao({})        // jhooth (empty object)

// Truthy values (evaluate to sach)
bool_bnao(1)         // sach
bool_bnao("text")    // sach
bool_bnao([1])       // sach
bool_bnao({a: 1})    // sach
```

### Boolean in Conditions

```codesi
is_logged_in = sach

agar (is_logged_in) {
    likho("Welcome!")
}

// Complex conditions
agar ((age >= 18) aur (has_id == sach)) {
    likho("Access granted")
}
```

---

## ⭕ Null

Represents absence of value: `khaali`.

### Usage

```codesi
// Uninitialized value
result = khaali

// Function with no return
karya do_something() {
    likho("Done")
    // No return statement
}
x = do_something()  // x is khaali

// Optional value
user_data = khaali
agar (logged_in) {
    user_data = {naam: "Raj"}
}
```

### Checking for Null

```codesi
value = khaali

agar (value == khaali) {
    likho("No value")
}

// Type check
likho(prakar(value))  // "khaali"
```

---

## 📦 Arrays

Ordered collections of values (like lists).

### Array Creation

```codesi
// Empty array
arr = []

// With elements
numbers = [1, 2, 3, 4, 5]
names = ["Raj", "Priya", "Amit"]

// Mixed types
mixed = [1, "hello", sach, 3.14, khaali]

// Nested arrays
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```

### Array Access

```codesi
arr = [10, 20, 30, 40, 50]

// Indexing (0-based)
first = arr[0]      // 10
third = arr[2]      // 30

// Negative indexing
last = arr[-1]      // 50
second_last = arr[-2]  // 40

// Modify elements
arr[1] = 25
likho(arr)  // [10, 25, 30, 40, 50]
```

### Array Methods

```codesi
arr = [1, 2, 3]

// Add elements
arr.push(4)         // [1, 2, 3, 4]
arr.unshift(0)      // [0, 1, 2, 3, 4]

// Remove elements
last = arr.pop()    // last = 4, arr = [0, 1, 2, 3]
first = arr.shift() // first = 0, arr = [1, 2, 3]

// Length
len = arr.lambai()  // 3

// Transform
doubled = arr.map(lambda(x) -> x * 2)
even = arr.filter(lambda(x) -> x % 2 == 0)

// Join
text = arr.join(", ")  // "1, 2, 3"

// Slice
subset = arr.slice(1, 3)  // [2, 3]

// Reverse
arr.reverse()  // [3, 2, 1]

// Sort
arr.sort()     // [1, 2, 3]
```

### Array Iteration

```codesi
fruits = ["Apple", "Banana", "Orange"]

// ForEach loop
har fruit mein fruits {
    likho(fruit)
}

// With index (using traditional for)
har i se 0 tak fruits.lambai() {
    likho(i, ":", fruits[i])
}
```

### Nested Arrays

```codesi
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

// Access nested elements
likho(matrix[0][1])  // 2
likho(matrix[1][2])  // 6

// Modify nested
matrix[0][0] = 10
```

---

## 🗂️ Objects

Key-value pairs (like dictionaries/maps).

### Object Creation

```codesi
// Empty object
obj = {}

// With properties
person = {
    naam: "Rishaank",
    umra: 15,
    city: "India"
}

// Nested objects
student = {
    naam: "Raj",
    marks: {
        math: 95,
        science: 88,
        english: 92
    },
    hobbies: ["coding", "gaming"]
}
```

### Object Access

```codesi
person = {naam: "Raj", umra: 25}

// Dot notation
naam = person.naam      // "Raj"
umra = person.umra      // 25

// Bracket notation
naam = person["naam"]   // "Raj"
key = "umra"
umra = person[key]      // 25
```

### Modify Objects

```codesi
person = {naam: "Raj"}

// Add property
person.umra = 25
person["city"] = "Mumbai"

// Modify property
person.umra = 26

// Delete property (set to khaali)
person.city = khaali
```

### Object Methods

```codesi
person = {naam: "Raj", umra: 25, city: "Mumbai"}

// Get keys
keys = person.keys()      // ["naam", "umra", "city"]

// Get values
values = person.values()  // ["Raj", 25, "Mumbai"]

// Get items
items = person.items()    // [["naam", "Raj"], ...]

// Check key
has_name = person.hai_kya("naam")  // sach
```

### Iterate Objects

```codesi
person = {naam: "Raj", umra: 25, city: "Mumbai"}

har key mein person {
    likho(key, ":", person[key])
}
// Output:
// naam : Raj
// umra : 25
// city : Mumbai
```

---

## 🔄 Type Conversion

Codesi performs automatic type conversion in certain situations, but you can also do explicit conversions.

### Automatic Conversion

```codesi
// String + Number (automatic conversion)
result = "Hello " + 25        // "Hello 25"
result = "Value: " + 3.14     // "Value: 3.14"

// Boolean in conditions (automatic)
x = 10
agar (x) {  // Non-zero numbers are truthy
    likho("x is truthy")
}
```

### Explicit Conversion

```codesi
// To String
text = string_bnao(123)       // "123"
text = string_bnao(3.14)      // "3.14"
text = string_bnao(sach)      // "sach"

// To Integer
num = int_bnao("123")         // 123
num = int_bnao(3.14)          // 3
num = int_bnao("42")          // 42

// To Float
num = float_bnao("3.14")      // 3.14
num = float_bnao(5)           // 5.0
num = float_bnao("42")        // 42.0

// To Boolean
bool_bnao(1)                  // sach
bool_bnao(0)                  // jhooth
bool_bnao("text")             // sach
bool_bnao("")                 // jhooth
```

---

## 🔍 Type Checking

Check what type a value is using `prakar()` or `type_of()`:

```codesi
likho(prakar(10))             // "Integer"
likho(prakar(3.14))           // "Float/Decimal"
likho(prakar("hello"))        // "shabd"
likho(prakar([1, 2]))         // "array"
likho(prakar({a: 1}))         // "object"
likho(prakar(sach))           // "sach_jhooth"
likho(prakar(khaali))         // "khaali"

// Type checking functions
agar (string_hai(value)) {
    likho("It's a string!")
}

agar (array_hai(data)) {
    likho("It's an array!")
}

agar (int_hai(num)) {
    likho("It's an integer!")
}
```

---

## 📊 Type Comparison Table

| Codesi Type | Python Equivalent | Example |
|-------------|-------------------|---------|
| Integer | int | `10`, `-5`, `0` |
| Float/Decimal | float | `3.14`, `-2.5` |
| shabd (String) | str | `"hello"`, `'world'` |
| sach (Boolean) | True | `sach` |
| jhooth (Boolean) | False | `jhooth` |
| khaali (Null) | None | `khaali` |
| array | list | `[1, 2, 3]` |
| object | dict | `{naam: "Raj"}` |
| Function | function | `karya func() {}` |

---

## 💡 Best Practices

### 1. Use Appropriate Types

```codesi
// ✅ Good - Clear types
age = 15                    // Integer for age
price = 99.99               // Float for money
naam = "Rishaank"           // String for text
is_active = sach            // Boolean for flags

// ❌ Avoid mixing types unnecessarily
age = "15"                  // String for age (confusing)
```

### 2. Explicit Type Conversion

```codesi
// ✅ Good - Explicit conversion
user_input = input_lo("Enter number: ")
number = int_bnao(user_input)

// ❌ Risky - Assuming type
result = user_input + 10    // Error if not a number
```

### 3. Check Types Before Operations

```codesi
// ✅ Good - Type checking
karya process(value) {
    agar (string_hai(value)) {
        vapas value.bada_karo()
    } ya_phir (int_hai(value)) {
        vapas value * 2
    } nahi_to {
        vapas khaali
    }
}
```

### 4. Use khaali for Optional Values

```codesi
// ✅ Good - Clear intent
result = khaali

agar (found) {
    result = "Found it!"
}

agar (result != khaali) {
    likho(result)
}
```

---

## 🚨 Common Type Errors

### Error 1: Type Mismatch in Operations

```codesi
// ❌ Wrong
result = "hello" - 5        // Can't subtract from string

// ✅ Correct
result = "hello" + string_bnao(5)  // "hello5"
```

### Error 2: Division by Zero

```codesi
// ❌ Wrong
result = 10 / 0             // Error!

// ✅ Correct
agar (divisor != 0) {
    result = 10 / divisor
} nahi_to {
    likho("Cannot divide by zero")
}
```

### Error 3: Array Index Out of Bounds

```codesi
// ❌ Wrong
arr = [1, 2, 3]
value = arr[10]             // Error!

// ✅ Correct
agar (index < arr.lambai()) {
    value = arr[index]
} nahi_to {
    likho("Invalid index")
}
```

---

## 📚 Summary

Codesi supports **7 main data types**:

1. **Numbers** (Integer, Float)
2. **Strings** (Text with quotes)
3. **Booleans** (`sach`, `jhooth`)
4. **Null** (`khaali`)
5. **Arrays** (Ordered lists)
6. **Objects** (Key-value pairs)
7. **Functions** (First-class functions)

**Key Features:**
- ✅ Dynamic typing (variables can change types)
- ✅ Automatic type conversion for strings + numbers
- ✅ Rich type checking functions
- ✅ Intuitive Hinglish keywords
- ✅ Full support for nested structures

---

**Next**: [Control Flow Guide](CONTROL_FLOW.md)
