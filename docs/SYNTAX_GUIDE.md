# Codesi Syntax Guide

Complete reference for Codesi programming language syntax.

## 📋 Table of Contents

- [Comments](#comments)
- [Variables](#variables)
- [Data Types](#data-types)
- [Operators](#operators)
- [Control Flow](#control-flow)
- [Loops](#loops)
- [Functions](#functions)
- [Classes](#classes)
- [Error Handling](#error-handling)
- [Advanced Syntax](#advanced-syntax)

---

## 💬 Comments

```codesi
// Single-line comment

// Multi-line comments (use multiple //)
// Line 1
// Line 2
// Line 3
```

**Note**: Block comments (/* */) are not supported yet.

---

## 📦 Variables

### Declaration and Assignment

```codesi
// Simple assignment
naam = "Rishaank"
umra = 15
height = 5.8
is_student = sach

// Multiple assignments
x = 10
y = 20
z = 30

// Constants (cannot be reassigned)
const PI = 3.14159
const MAX_SIZE = 100
```

### Variable Naming Rules

```codesi
// ✅ Valid names
naam
first_name
age2
_private
student_marks

// ❌ Invalid names
2name        // Cannot start with number
first-name   // No hyphens
my name      // No spaces
```

### Compound Assignment

```codesi
x = 10

x += 5    // x = x + 5  → 15
x -= 3    // x = x - 3  → 12
x *= 2    // x = x * 2  → 24
x /= 4    // x = x / 4  → 6
```

---

## 🎯 Data Types

### Numbers

```codesi
// Integers
age = 15
count = 100
negative = -50

// Floats
height = 5.8
pi = 3.14159
temperature = -2.5
```

### Strings

```codesi
// Single quotes
naam = 'Rishaank'

// Double quotes
message = "Hello World"

// Escape sequences
text = "Line 1\nLine 2"
path = "C:\\Users\\Rishaank"
quote = "He said \"Hello\""

// All escape sequences:
// \n - newline
// \t - tab
// \r - carriage return
// \b - backspace
// \f - form feed
// \v - vertical tab
// \\ - backslash
// \' - single quote
// \" - double quote
// \0 - null character
```

### Booleans

```codesi
is_adult = sach      // true
is_minor = jhooth    // false
has_access = sach
is_complete = jhooth
```

### Null/None

```codesi
value = khaali       // null/none
result = khaali
```

### Arrays

```codesi
// Empty array
arr = []

// With elements
numbers = [1, 2, 3, 4, 5]
names = ["Raj", "Priya", "Amit"]
mixed = [1, "hello", sach, 3.14]

// Nested arrays
matrix = [[1, 2], [3, 4], [5, 6]]
```

### Objects

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
        science: 88
    }
}
```

---

## ➕ Operators

### Arithmetic Operators

```codesi
a = 10
b = 3

result = a + b    // Addition: 13
result = a - b    // Subtraction: 7
result = a * b    // Multiplication: 30
result = a / b    // Division: 3.333...
result = a % b    // Modulo: 1
result = a ** b   // Power: 1000
```

### Comparison Operators

```codesi
x = 10
y = 20

x == y    // Equal to: jhooth
x != y    // Not equal: sach
x < y     // Less than: sach
x > y     // Greater than: jhooth
x <= y    // Less than or equal: sach
x >= y    // Greater than or equal: jhooth
```

### Logical Operators

```codesi
a = sach
b = jhooth

a aur b   // AND: jhooth
a ya b    // OR: sach
nahi a    // NOT: jhooth

// Complex expressions
(x > 5) aur (y < 10)
(age >= 18) ya (has_permission == sach)
nahi (is_blocked)
```

### Ternary Operator

```codesi
// condition ? true_value : false_value
status = (age >= 18) ? "Adult" : "Minor"
max = (a > b) ? a : b
result = (score >= 40) ? "Pass" : "Fail"
```

---

## 🔀 Control Flow

### If Statement

```codesi
// Simple if
agar (condition) {
    // code
}

// If-else
agar (age >= 18) {
    likho("Adult")
} nahi_to {
    likho("Minor")
}

// Single line (no braces)
agar (x > 5) likho("Big")
```

### If-Elif-Else

```codesi
marks = 85

agar (marks >= 90) {
    likho("A+ Grade")
} ya_phir (marks >= 80) {
    likho("A Grade")
} ya_phir (marks >= 70) {
    likho("B Grade")
} ya_phir (marks >= 60) {
    likho("C Grade")
} nahi_to {
    likho("Fail")
}
```

### Nested If

```codesi
agar (age >= 18) {
    agar (has_license == sach) {
        likho("Can drive")
    } nahi_to {
        likho("Need license")
    }
} nahi_to {
    likho("Too young to drive")
}
```

### Switch-Case

```codesi
day = 3

day ke case mein {
    1 -> likho("Monday")
    2 -> likho("Tuesday")
    3 -> likho("Wednesday")
    4 -> likho("Thursday")
    5 -> likho("Friday")
    default -> likho("Weekend")
}

// With multiple statements
grade ke case mein {
    "A" -> {
        likho("Excellent!")
        score = 90
    }
    "B" -> {
        likho("Good!")
        score = 80
    }
    default -> {
        likho("Need improvement")
        score = 50
    }
}
```

---

## 🔁 Loops

### For Loop - Multiple Syntaxes

```codesi
// Syntax 1: Simple range
har i se 0 tak 5 {
    likho(i)  // 0, 1, 2, 3, 4
}

// Syntax 2: With parentheses
har i ke liye (0 se 5 tak) {
    likho(i)
}

// Syntax 3: Starting from 1
har i se 1 tak 6 {
    likho(i)  // 1, 2, 3, 4, 5
}

// With variables
start = 1
end = 10
har i se start tak end {
    likho(i)
}
```

### ForEach Loop - Multiple Syntaxes

```codesi
fruits = ["Apple", "Banana", "Orange"]

// Syntax 1: Direct
har fruit mein fruits {
    likho(fruit)
}

// Syntax 2: With 'ke liye'
har fruit ke liye fruits mein {
    likho(fruit)
}

// With array methods
numbers = [1, 2, 3, 4, 5]
har num mein numbers {
    likho(num * 2)
}

// With objects (iterates keys)
person = {naam: "Raj", umra: 25}
har key mein person {
    likho(key, ":", person[key])
}
```

### While Loop

```codesi
// Basic while
count = 0
jabtak (count < 5) {
    likho(count)
    count = count + 1
}

// Infinite loop with break
jabtak (sach) {
    input = input_lo("Enter 'exit' to quit: ")
    agar (input == "exit") {
        break
    }
    likho("You entered:", input)
}
```

### Do-While Loop

```codesi
// Execute at least once
count = 0
karo {
    likho(count)
    count = count + 1
} jabtak (count < 5)

// Menu example
karo {
    likho("1. Option 1")
    likho("2. Option 2")
    likho("3. Exit")
    choice = int_lo("Choose: ")
} jabtak (choice != 3)
```

### Break and Continue

```codesi
// Break - exit loop
har i se 1 tak 11 {
    agar (i == 5) {
        break  // Stop at 5
    }
    likho(i)
}

// Continue - skip iteration
har i se 1 tak 11 {
    agar (i % 2 == 0) {
        continue  // Skip even numbers
    }
    likho(i)  // Only odd numbers
}
```

### Nested Loops

```codesi
// Multiplication table
har i se 1 tak 6 {
    har j se 1 tak 6 {
        likho(i, "x", j, "=", i * j)
    }
    likho("---")
}

// Pattern printing
har i se 1 tak 6 {
    row = ""
    har j se 1 tak i + 1 {
        row = row + "*"
    }
    likho(row)
}
```

---

## 🔧 Functions

### Basic Function

```codesi
// Simple function
karya greet() {
    likho("Hello!")
}

greet()  // Call function

// With parameters
karya greet(naam) {
    likho("Hello", naam)
}

greet("Rishaank")
```

### Return Statement

```codesi
// Return value
karya add(a, b) {
    vapas a + b
}

result = add(5, 3)
likho(result)  // 8

// Multiple returns
karya get_grade(marks) {
    agar (marks >= 90) {
        vapas "A+"
    } ya_phir (marks >= 80) {
        vapas "A"
    } nahi_to {
        vapas "B"
    }
}
```

### Default Parameters

```codesi
karya greet(naam = "Guest") {
    likho("Hello", naam)
}

greet()           // Hello Guest
greet("Rishaank") // Hello Rishaank

// Multiple defaults
karya create_user(naam, umra = 18, city = "Mumbai") {
    likho(naam, umra, city)
}

create_user("Raj")              // Raj 18 Mumbai
create_user("Priya", 25)        // Priya 25 Mumbai
create_user("Amit", 30, "Delhi") // Amit 30 Delhi
```

### Variadic Parameters

```codesi
// Accept any number of arguments
karya sum(...numbers) {
    total = 0
    har num mein numbers {
        total += num
    }
    vapas total
}

likho(sum(1, 2, 3))        // 6
likho(sum(10, 20, 30, 40)) // 100

// Mix regular and variadic
karya log(level, ...messages) {
    likho("[", level, "]")
    har msg mein messages {
        likho(msg)
    }
}

log("INFO", "Server started", "Port 8000")
```

### Type Annotations

```codesi
// Parameter type hints
karya calculate(a: int, b: int) -> int {
    vapas a + b
}

// Return type annotation
karya get_name() -> string {
    vapas "Rishaank"
}
```

### Lambda Functions

```codesi
// Basic lambda
square = lambda(x) -> x * x
likho(square(5))  // 25

// With array methods
numbers = [1, 2, 3, 4, 5]
doubled = numbers.map(lambda(x) -> x * 2)
likho(doubled)  // [2, 4, 6, 8, 10]

// Multi-line lambda
process = lambda(x) -> {
    result = x * 2
    result = result + 10
    vapas result
}
```

---

## 🏗️ Classes

### Basic Class

```codesi
class Person {
    // Constructor
    banao(naam, umra) {
        ye.naam = naam
        ye.umra = umra
    }
    
    // Method
    karya introduce() {
        likho("Mera naam", ye.naam, "hai")
    }
}

// Create instance
person = new Person("Rishaank", 15)
person.introduce()
```

### Inheritance

```codesi
// Parent class
class Animal {
    banao(naam) {
        ye.naam = naam
    }
    
    karya speak() {
        likho(ye.naam, "makes a sound")
    }
}

// Child class
class Dog extends Animal {
    banao(naam, breed) {
        super.banao(naam)  // Call parent constructor
        ye.breed = breed
    }
    
    karya speak() {
        likho(ye.naam, "barks!")
    }
    
    karya get_breed() {
        vapas ye.breed
    }
}

dog = new Dog("Tommy", "Labrador")
dog.speak()      // Tommy barks!
likho(dog.get_breed())  // Labrador
```

### Static Methods

```codesi
class MathHelper {
    static karya add(a, b) {
        vapas a + b
    }
    
    static karya multiply(a, b) {
        vapas a * b
    }
}

// Call without creating instance
result = MathHelper.add(5, 3)
likho(result)  // 8
```

### Properties

```codesi
class Student {
    banao(naam, roll) {
        ye.naam = naam
        ye.roll = roll
        ye.marks = {}
    }
    
    karya add_marks(subject, marks) {
        ye.marks[subject] = marks
    }
    
    karya get_average() {
        total = 0
        count = 0
        har subject mein ye.marks {
            total += ye.marks[subject]
            count += 1
        }
        vapas total / count
    }
}
```

---

## ⚠️ Error Handling

### Try-Catch

```codesi
try {
    result = 10 / 0
} catch (e) {
    likho("Error:", e.message)
}
```

### Try-Catch-Finally

```codesi
try {
    file_content = file_padho("data.txt")
    likho(file_content)
} catch (e) {
    likho("Error reading file:", e.message)
} finally {
    likho("Cleanup complete")
}
```

### Throw Statement

```codesi
karya divide(a, b) {
    agar (b == 0) {
        throw {message: "Cannot divide by zero"}
    }
    vapas a / b
}

try {
    result = divide(10, 0)
} catch (e) {
    likho("Caught:", e.message)
}
```

---

## 🎨 Advanced Syntax

### Array/Object Destructuring (via methods)

```codesi
// Array access
arr = [1, 2, 3]
first = arr[0]
second = arr[1]

// Object access
person = {naam: "Raj", umra: 25}
naam = person.naam
umra = person.umra
```

### Method Chaining

```codesi
text = "  Hello World  "
result = text.saaf_karo().chota_karo().badlo("world", "codesi")
likho(result)  // "hello codesi"

// Array chaining
numbers = [1, 2, 3, 4, 5]
result = numbers.map(lambda(x) -> x * 2).filter(lambda(x) -> x > 5)
likho(result)  // [6, 8, 10]
```

### Index and Member Assignment

```codesi
// Array index assignment
arr = [1, 2, 3]
arr[1] = 10
likho(arr)  // [1, 10, 3]

// Object member assignment
obj = {naam: "Raj"}
obj.umra = 25
obj["city"] = "Mumbai"
likho(obj)  // {naam: "Raj", umra: 25, city: "Mumbai"}
```

### Semicolons (Optional)

```codesi
// With semicolons
x = 10;
y = 20;
likho(x + y);

// Without semicolons (preferred)
x = 10
y = 20
likho(x + y)
```

---

## 📝 Style Guidelines

### Naming Conventions

```codesi
// Variables: snake_case
student_name = "Raj"
total_marks = 100

// Functions: snake_case
karya calculate_average() { }

// Classes: PascalCase
class StudentRecord { }

// Constants: UPPER_CASE
const MAX_SIZE = 100
const PI = 3.14159
```

### Spacing

```codesi
// ✅ Good spacing
x = 10 + 20
agar (x > 5) {
    likho(x)
}

// ❌ Poor spacing
x=10+20
agar(x>5){
    likho(x)
}
```

### Indentation

```codesi
// Use 4 spaces per level
karya example() {
    agar (condition) {
        har i se 0 tak 5 {
            likho(i)
        }
    }
}
```

---

**Next**: [Built-in Functions](BUILTIN_FUNCTIONS.md)