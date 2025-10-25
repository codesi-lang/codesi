# Built-in Functions Reference

Complete reference for all Codesi built-in functions.

## 📋 Table of Contents

- [Input/Output](#inputoutput)
- [Math Functions](#math-functions)
- [Type Functions](#type-functions)
- [Type Conversion](#type-conversion)
- [String Methods](#string-methods)
- [Array Methods](#array-methods)
- [Object Methods](#object-methods)
- [File Operations](#file-operations)
- [JSON Operations](#json-operations)
- [Time Functions](#time-functions)
- [Special Features](#special-features)

---

## 📤 Input/Output

### likho(...values)
Print values to console.

```codesi
likho("Hello World")
likho("Name:", naam, "Age:", umra)
likho(x, y, z)
```

**Parameters**: Any number of values  
**Returns**: `khaali` (None)

---

### input_lo(prompt)
Get string input from user.

```codesi
naam = input_lo("Aapka naam: ")
message = input_lo()  // No prompt
```

**Parameters**: 
- `prompt` (optional): String to display
**Returns**: String entered by user

---

### int_lo(prompt)
Get integer input from user.

```codesi
umra = int_lo("Aapki umra: ")
number = int_lo("Enter number: ")
```

**Parameters**: 
- `prompt` (optional): String to display
**Returns**: Integer value
**Throws**: Error if input is not a valid integer

---

### float_lo(prompt)
Get float/decimal input from user.

```codesi
height = float_lo("Height in meters: ")
price = float_lo("Enter price: ")
```

**Parameters**: 
- `prompt` (optional): String to display
**Returns**: Float value
**Throws**: Error if input is not a valid number

---

## 🔢 Math Functions

### math_absolute(number)
Get absolute value.

```codesi
likho(math_absolute(-10))   // 10
likho(math_absolute(5))     // 5
```

**Parameters**: Number  
**Returns**: Absolute value (always positive)

---

### math_square(number)
Get square root.

```codesi
likho(math_square(16))    // 4.0
likho(math_square(25))    // 5.0
likho(math_square(2))     // 1.414...
```

**Parameters**: Non-negative number  
**Returns**: Square root  
**Throws**: Error if negative number

---

### math_power(base, exponent)
Calculate power.

```codesi
likho(math_power(2, 3))    // 8
likho(math_power(5, 2))    // 25
likho(math_power(10, 0))   // 1
```

**Parameters**: 
- `base`: Base number
- `exponent`: Power to raise to
**Returns**: Result of base^exponent

---

### math_random(min, max)
Generate random integer.

```codesi
dice = math_random(1, 6)           // 1 to 6
lottery = math_random(1, 100)      // 1 to 100
coin = math_random(0, 1)           // 0 or 1
```

**Parameters**: 
- `min`: Minimum value (inclusive)
- `max`: Maximum value (inclusive)
**Returns**: Random integer between min and max

---

### math_niche(number)
Floor function (round down).

```codesi
likho(math_niche(4.7))    // 4
likho(math_niche(4.2))    // 4
likho(math_niche(-2.7))   // -3
```

**Parameters**: Number  
**Returns**: Largest integer ≤ number

---

### math_upar(number)
Ceiling function (round up).

```codesi
likho(math_upar(4.2))     // 5
likho(math_upar(4.7))     // 5
likho(math_upar(-2.3))    // -2
```

**Parameters**: Number  
**Returns**: Smallest integer ≥ number

---

### math_gol(number, decimals)
Round to specified decimal places.

```codesi
likho(math_gol(4.567))      // 5
likho(math_gol(4.567, 2))   // 4.57
likho(math_gol(4.567, 1))   // 4.6
```

**Parameters**: 
- `number`: Number to round
- `decimals` (optional): Decimal places (default: 0)
**Returns**: Rounded number

---

### Trigonometric Functions

```codesi
// Sine, Cosine, Tangent
math_sin(angle_in_radians)
math_cos(angle_in_radians)
math_tan(angle_in_radians)

// Example
pi = 3.14159
likho(math_sin(pi / 2))     // 1.0
likho(math_cos(0))          // 1.0
```

---

### Logarithmic Functions

```codesi
// Natural logarithm (base e)
math_log(number)

// Exponential (e^x)
math_exp(number)

// Examples
likho(math_log(2.71828))    // ≈ 1.0
likho(math_exp(1))          // ≈ 2.71828
```

---

## 🏷️ Type Functions

### prakar(value) / type_of(value)
Get type of value.

```codesi
likho(prakar(10))           // "Integer"
likho(prakar(3.14))         // "Float/Decimal"
likho(prakar("hello"))      // "shabd"
likho(prakar([1, 2]))       // "array"
likho(prakar({a: 1}))       // "object"
likho(prakar(sach))         // "sach_jhooth"
likho(prakar(khaali))       // "khaali"
```

**Parameters**: Any value  
**Returns**: String representing type

---

### Type Check Functions

```codesi
// Check if value is specific type
string_hai(value)    // Is string?
array_hai(value)     // Is array?
int_hai(value)       // Is integer?
float_hai(value)     // Is float?
bool_hai(value)      // Is boolean?
obj_hai(value)       // Is object?

// Examples
agar (string_hai(naam)) {
    likho("It's a string!")
}

agar (array_hai(data)) {
    likho("It's an array!")
}
```

**Parameters**: Any value  
**Returns**: `sach` or `jhooth`

---

## 🔄 Type Conversion

### string_bnao(value)
Convert to string.

```codesi
text = string_bnao(123)       // "123"
text = string_bnao(3.14)      // "3.14"
text = string_bnao(sach)      // "sach"
text = string_bnao([1, 2])    // "[1, 2]"
```

**Parameters**: Any value  
**Returns**: String representation

---

### int_bnao(value)
Convert to integer.

```codesi
num = int_bnao("123")      // 123
num = int_bnao(3.14)       // 3
num = int_bnao(3.99)       // 3
num = int_bnao("45.67")    // 45 (parses as float first)
```

**Parameters**: String or number  
**Returns**: Integer value  
**Throws**: Error if conversion fails

---

### float_bnao(value)
Convert to float.

```codesi
num = float_bnao("3.14")     // 3.14
num = float_bnao(5)          // 5.0
num = float_bnao("42")       // 42.0
```

**Parameters**: String or number  
**Returns**: Float value  
**Throws**: Error if conversion fails

---

### bool_bnao(value)
Convert to boolean.

```codesi
likho(bool_bnao(1))          // sach
likho(bool_bnao(0))          // jhooth
likho(bool_bnao("text"))     // sach
likho(bool_bnao(""))         // jhooth
```

**Parameters**: Any value  
**Returns**: `sach` or `jhooth`

---

## 📝 String Methods

### text.lambai() / text.size()
Get string length.

```codesi
text = "Hello"
likho(text.lambai())    // 5
```

**Returns**: Integer length

---

### text.bada_karo()
Convert to uppercase.

```codesi
text = "hello world"
likho(text.bada_karo())    // "HELLO WORLD"
```

**Returns**: Uppercase string

---

### text.chota_karo()
Convert to lowercase.

```codesi
text = "HELLO WORLD"
likho(text.chota_karo())    // "hello world"
```

**Returns**: Lowercase string

---

### text.saaf_karo()
Remove leading/trailing whitespace.

```codesi
text = "  hello  "
likho(text.saaf_karo())    // "hello"
```

**Returns**: Trimmed string

---

### text.todo(separator)
Split string into array.

```codesi
text = "apple,banana,orange"
fruits = text.todo(",")
likho(fruits)    // ["apple", "banana", "orange"]

// Default separator is space
words = "hello world".todo()
likho(words)     // ["hello", "world"]
```

**Parameters**: Separator string (optional)  
**Returns**: Array of strings

---

### text.badlo(old, new)
Replace first occurrence.

```codesi
text = "hello world world"
result = text.badlo("world", "codesi")
likho(result)    // "hello codesi world"
```

**Parameters**: 
- `old`: String to find
- `new`: Replacement string
**Returns**: Modified string

---

### text.sab_badlo(old, new)
Replace all occurrences.

```codesi
text = "hello world world"
result = text.sab_badlo("world", "codesi")
likho(result)    // "hello codesi codesi"
```

**Parameters**: 
- `old`: String to find
- `new`: Replacement string
**Returns**: Modified string

---

### text.included_hai(substring)
Check if substring exists.

```codesi
text = "hello world"
likho(text.included_hai("world"))    // sach
likho(text.included_hai("xyz"))      // jhooth
```

**Parameters**: Substring to search  
**Returns**: `sach` or `jhooth`

---

### text.start_hota_hai(prefix)
Check if starts with prefix.

```codesi
text = "hello world"
likho(text.start_hota_hai("hello"))  // sach
likho(text.start_hota_hai("world"))  // jhooth
```

**Parameters**: Prefix string  
**Returns**: `sach` or `jhooth`

---

### text.end_hota_hai(suffix)
Check if ends with suffix.

```codesi
text = "hello world"
likho(text.end_hota_hai("world"))    // sach
likho(text.end_hota_hai("hello"))    // jhooth
```

**Parameters**: Suffix string  
**Returns**: `sach` or `jhooth`

---

## 📦 Array Methods

### arr.push(element) / arr.dalo(element)
Add element to end.

```codesi
arr = [1, 2, 3]
arr.push(4)
likho(arr)    // [1, 2, 3, 4]
```

**Parameters**: Element to add  
**Returns**: Modified array

---

### arr.pop() / arr.nikalo()
Remove and return last element.

```codesi
arr = [1, 2, 3]
last = arr.pop()
likho(last)    // 3
likho(arr)     // [1, 2]
```

**Returns**: Removed element

---

### arr.shift() / arr.pehla_nikalo()
Remove and return first element.

```codesi
arr = [1, 2, 3]
first = arr.shift()
likho(first)    // 1
likho(arr)      // [2, 3]
```

**Returns**: Removed element

---

### arr.unshift(element) / arr.pehle_dalo(element)
Add element to beginning.

```codesi
arr = [2, 3, 4]
arr.unshift(1)
likho(arr)    // [1, 2, 3, 4]
```

**Parameters**: Element to add  
**Returns**: Modified array

---

### arr.lambai() / arr.size()
Get array length.

```codesi
arr = [1, 2, 3, 4, 5]
likho(arr.lambai())    // 5
```

**Returns**: Integer length

---

### arr.map(function) / arr.badlo(function)
Transform each element.

```codesi
numbers = [1, 2, 3, 4, 5]
doubled = numbers.map(lambda(x) -> x * 2)
likho(doubled)    // [2, 4, 6, 8, 10]

// With named function
karya square(x) {
    vapas x * x
}
squared = numbers.map(square)
likho(squared)    // [1, 4, 9, 16, 25]
```

**Parameters**: Function to apply to each element  
**Returns**: New array with transformed elements

---

### arr.filter(function) / arr.chuno(function)
Filter elements based on condition.

```codesi
numbers = [1, 2, 3, 4, 5, 6]
even = numbers.filter(lambda(x) -> x % 2 == 0)
likho(even)    // [2, 4, 6]

// Complex filtering
students = [
    {naam: "Raj", marks: 85},
    {naam: "Priya", marks: 92},
    {naam: "Amit", marks: 78}
]
toppers = students.filter(lambda(s) -> s.marks >= 90)
```

**Parameters**: Function returning boolean  
**Returns**: New array with filtered elements

---

### arr.reduce(function, initial) / arr.combine(function, initial)
Reduce array to single value.

```codesi
numbers = [1, 2, 3, 4, 5]

// Sum all numbers
sum = numbers.reduce(lambda(acc, x) -> acc + x, 0)
likho(sum)    // 15

// Product
product = numbers.reduce(lambda(acc, x) -> acc * x, 1)
likho(product)    // 120

// Without initial value (uses first element)
sum = numbers.reduce(lambda(acc, x) -> acc + x)
likho(sum)    // 15
```

**Parameters**: 
- `function`: Accumulator function (acc, current)
- `initial` (optional): Starting value
**Returns**: Final accumulated value

---

### arr.join(separator) / arr.jodo(separator)
Join array elements into string.

```codesi
arr = ["apple", "banana", "orange"]
text = arr.join(", ")
likho(text)    // "apple, banana, orange"

// Default separator is comma
numbers = [1, 2, 3]
likho(numbers.join())    // "1,2,3"
```

**Parameters**: Separator string (default: ",")  
**Returns**: Joined string

---

### arr.slice(start, end) / arr.cutkr(start, end)
Extract portion of array.

```codesi
arr = [1, 2, 3, 4, 5]
subset = arr.slice(1, 4)
likho(subset)    // [2, 3, 4]

// From index to end
end_part = arr.slice(2)
likho(end_part)    // [3, 4, 5]
```

**Parameters**: 
- `start`: Starting index
- `end` (optional): Ending index (exclusive)
**Returns**: New array (doesn't modify original)

---

### arr.reverse() / arr.ulta()
Reverse array in place.

```codesi
arr = [1, 2, 3, 4, 5]
arr.reverse()
likho(arr)    // [5, 4, 3, 2, 1]
```

**Returns**: Reversed array (modifies original)

---

### arr.sort() / arr.arrange()
Sort array in place.

```codesi
arr = [5, 2, 8, 1, 9]
arr.sort()
likho(arr)    // [1, 2, 5, 8, 9]

// Strings
names = ["Raj", "Amit", "Priya"]
names.sort()
likho(names)    // ["Amit", "Priya", "Raj"]
```

**Returns**: Sorted array (modifies original)

---

## 🗂️ Object Methods

### obj.keys()
Get all keys as array.

```codesi
person = {naam: "Raj", umra: 25, city: "Mumbai"}
keys = person.keys()
likho(keys)    // ["naam", "umra", "city"]
```

**Returns**: Array of keys

---

### obj.values()
Get all values as array.

```codesi
person = {naam: "Raj", umra: 25, city: "Mumbai"}
values = person.values()
likho(values)    // ["Raj", 25, "Mumbai"]
```

**Returns**: Array of values

---

### obj.items()
Get key-value pairs as array of arrays.

```codesi
person = {naam: "Raj", umra: 25}
items = person.items()
likho(items)    // [["naam", "Raj"], ["umra", 25]]

// Iterate over items
har item mein items {
    likho(item[0], ":", item[1])
}
```

**Returns**: Array of [key, value] pairs

---

### obj.hai_kya(key)
Check if key exists.

```codesi
person = {naam: "Raj", umra: 25}
likho(person.hai_kya("naam"))     // sach
likho(person.hai_kya("city"))     // jhooth
```

**Parameters**: Key to check  
**Returns**: `sach` or `jhooth`

---

## 📁 File Operations

### file_padho(path)
Read file contents.

```codesi
content = file_padho("data.txt")
likho(content)

// Error handling
try {
    content = file_padho("missing.txt")
} catch (e) {
    likho("Error:", e.message)
}
```

**Parameters**: File path (string)  
**Returns**: File contents as string  
**Throws**: Error if file not found

---

### file_likho(path, content)
Write to file (overwrites existing).

```codesi
file_likho("output.txt", "Hello World")
file_likho("data.txt", "Line 1\nLine 2\nLine 3")

// Write array/object (converts to string)
data = [1, 2, 3]
file_likho("numbers.txt", string_bnao(data))
```

**Parameters**: 
- `path`: File path
- `content`: Content to write
**Returns**: `sach` on success  
**Throws**: Error on failure

---

### file_append(path, content)
Append to file.

```codesi
file_append("log.txt", "New log entry\n")
file_append("data.txt", "Additional line")
```

**Parameters**: 
- `path`: File path
- `content`: Content to append
**Returns**: `sach` on success  
**Throws**: Error on failure

---

### file_hai(path)
Check if file exists.

```codesi
agar (file_hai("config.txt")) {
    content = file_padho("config.txt")
} nahi_to {
    likho("File not found")
}
```

**Parameters**: File path  
**Returns**: `sach` or `jhooth`

---

### file_delete(path)
Delete file.

```codesi
agar (file_hai("temp.txt")) {
    file_delete("temp.txt")
    likho("File deleted")
}
```

**Parameters**: File path  
**Throws**: Error if file doesn't exist

---

### file_copy(source, destination)
Copy file.

```codesi
file_copy("original.txt", "backup.txt")
```

**Parameters**: 
- `source`: Source file path
- `destination`: Destination file path
**Throws**: Error on failure

---

### file_move(source, destination)
Move/rename file.

```codesi
file_move("old_name.txt", "new_name.txt")
```

**Parameters**: 
- `source`: Source file path
- `destination`: Destination file path
**Throws**: Error on failure

---

### file_size(path)
Get file size in bytes.

```codesi
size = file_size("data.txt")
likho("File size:", size, "bytes")
```

**Parameters**: File path  
**Returns**: Size in bytes  
**Throws**: Error if file doesn't exist

---

### dir_banao(path)
Create directory.

```codesi
dir_banao("output")
dir_banao("data/processed")
```

**Parameters**: Directory path  
**Throws**: Error on failure

---

### dir_list(path)
List directory contents.

```codesi
files = dir_list(".")
har file mein files {
    likho(file)
}

// Specific directory
files = dir_list("data")
```

**Parameters**: Directory path (default: ".")  
**Returns**: Array of file/folder names

---

## 📋 JSON Operations

### json_parse(json_string)
Parse JSON string to object/array.

```codesi
json_text = '{"naam": "Raj", "umra": 25}'
data = json_parse(json_text)
likho(data.naam)    // "Raj"

// Array
json_arr = '[1, 2, 3, 4, 5]'
numbers = json_parse(json_arr)
likho(numbers[0])   // 1
```

**Parameters**: JSON string  
**Returns**: Parsed object or array  
**Throws**: Error if invalid JSON

---

### json_stringify(value)
Convert value to JSON string.

```codesi
person = {naam: "Raj", umra: 25, city: "Mumbai"}
json_text = json_stringify(person)
likho(json_text)
// {"naam": "Raj", "umra": 25, "city": "Mumbai"}

// Save to file
file_likho("person.json", json_stringify(person))
```

**Parameters**: Any value (object, array, etc.)  
**Returns**: JSON string

---

## ⏰ Time Functions

### time_now()
Get current timestamp.

```codesi
timestamp = time_now()
likho(timestamp)    // Unix timestamp (seconds since 1970)

// Measure execution time
start = time_now()
// ... some code ...
end = time_now()
duration = end - start
likho("Time taken:", duration, "seconds")
```

**Returns**: Float (seconds since epoch)

---

### time_sleep(seconds)
Pause execution.

```codesi
likho("Starting...")
time_sleep(2)    // Wait 2 seconds
likho("Done!")

// Countdown
har i se 5 tak 0 {
    likho(i)
    time_sleep(1)
}
likho("Blast off!")
```

**Parameters**: Seconds to sleep (can be decimal)  
**Returns**: `khaali`

---

## 🎯 Utility Functions

### lambai(value)
Get length of string/array.

```codesi
likho(lambai("hello"))      // 5
likho(lambai([1, 2, 3]))    // 3
```

**Parameters**: String or array  
**Returns**: Length

---

### range(start, end)
Create array of numbers.

```codesi
// Single argument (0 to n)
nums = range(5)
likho(nums)    // [0, 1, 2, 3, 4]

// Two arguments (start to end)
nums = range(5, 10)
likho(nums)    // [5, 6, 7, 8, 9]

// Use in loops
har i mein range(1, 6) {
    likho(i)   // 1, 2, 3, 4, 5
}
```

**Parameters**: 
- `start`: Start value (or end if only one arg)
- `end` (optional): End value (exclusive)
**Returns**: Array of integers

---

### repeatkr(string, count)
Repeat string.

```codesi
likho(repeatkr("*", 5))        // "*****"
likho(repeatkr("Ha", 3))       // "HaHaHa"
line = repeatkr("-", 50)
```

**Parameters**: 
- `string`: String to repeat
- `count`: Number of repetitions
**Returns**: Repeated string

---

## 🌟 Special Features

### samjhao_on()
Enable code explanation mode.

```codesi
samjhao_on()
// Now every operation will be explained
x = 10
y = 20
result = x + y
```

**Returns**: Success message

---

### samjhao_off()
Disable code explanation mode.

```codesi
samjhao_off()
```

**Returns**: Success message

---

### samjhao()
Display collected explanations.

```codesi
samjhao_on()
x = 10
y = 20
result = x + y
samjhao()  // Shows detailed explanation
```

**Returns**: Formatted explanation text

---

### time_machine_on(max)
Enable time-travel debugging.

```codesi
time_machine_on()        // Default: 100 snapshots
time_machine_on(500)     // Custom limit

x = 5
x = x * 2
x = x + 3
```

**Parameters**: 
- `max` (optional): Max snapshots (default: 100)
**Returns**: Success message

---

### time_machine_off()
Disable time machine.

```codesi
time_machine_off()
```

**Returns**: Success message

---

### time_machine_status()
Check time machine status.

```codesi
time_machine_status()
// Shows: ON/OFF, snapshots count, current step
```

**Returns**: Status information

---

### peeche(steps)
Go back in execution history.

```codesi
x = 5
x = 10
x = 15
peeche()     // Go back to x = 10
peeche(2)    // Go back 2 steps to x = 5
```

**Parameters**: 
- `steps` (optional): Number of steps (default: 1)
**Returns**: Snapshot information

**Note**: Only works in REPL with time machine enabled

---

### aage(steps)
Go forward in execution history.

```codesi
aage()      // Go forward 1 step
aage(2)     // Go forward 2 steps
```

**Parameters**: 
- `steps` (optional): Number of steps (default: 1)
**Returns**: Snapshot information

**Note**: Only works in REPL with time machine enabled

---

### timeline()
View complete execution timeline.

```codesi
timeline()
// Shows all snapshots with step numbers
```

**Returns**: Complete timeline display

---

### import_karo(filepath)
Import another Codesi file.

```codesi
// Import and execute another file
import_karo("utils.cds")

// Now you can use functions from utils.cds
```

**Parameters**: File path to import  
**Returns**: `sach` on success  
**Throws**: Error if file not found

---

## 📊 Function Categories Summary

### I/O (4 functions)
- `likho`, `input_lo`, `int_lo`, `float_lo`

### Math (12 functions)
- `math_absolute`, `math_square`, `math_power`, `math_random`
- `math_niche`, `math_upar`, `math_gol`
- `math_sin`, `math_cos`, `math_tan`
- `math_log`, `math_exp`

### Type Operations (11 functions)
- `prakar/type_of`
- `string_hai`, `array_hai`, `int_hai`, `float_hai`, `bool_hai`, `obj_hai`
- `string_bnao`, `int_bnao`, `float_bnao`, `bool_bnao`

### String Methods (9 methods)
- `lambai`, `bada_karo`, `chota_karo`, `saaf_karo`
- `todo`, `badlo`, `sab_badlo`
- `included_hai`, `start_hota_hai`, `end_hota_hai`

### Array Methods (12 methods)
- `push`, `pop`, `shift`, `unshift`
- `lambai`, `map`, `filter`, `reduce`
- `join`, `slice`, `reverse`, `sort`

### Object Methods (4 methods)
- `keys`, `values`, `items`, `hai_kya`

### File Operations (9 functions)
- `file_padho`, `file_likho`, `file_append`
- `file_hai`, `file_delete`, `file_copy`, `file_move`, `file_size`
- `dir_banao`, `dir_list`

### JSON (2 functions)
- `json_parse`, `json_stringify`

### Time (2 functions)
- `time_now`, `time_sleep`

### Special Features (8 functions)
- `samjhao_on`, `samjhao_off`, `samjhao`
- `time_machine_on`, `time_machine_off`, `time_machine_status`
- `peeche`, `aage`, `timeline`

### Utilities (3 functions)
- `lambai`, `range`, `repeatkr`

### Import (1 function)
- `import_karo`

---

**Total: 70+ Built-in Functions!**

---

**Next**: [Control Flow Guide](CONTROL_FLOW.md)