# Examples Index

Complete catalog of all Codesi code examples organized by difficulty and topic.

## 📋 Table of Contents

- [Beginner Examples](#beginner-examples)
- [Intermediate Examples](#intermediate-examples)
- [Advanced Examples](#advanced-examples)
- [Project Examples](#project-examples)
- [Feature Demonstrations](#feature-demonstrations)
- [Algorithm Examples](#algorithm-examples)

---

## 🌱 Beginner Examples

Perfect for first-time programmers and those new to Codesi.

### 1. Hello World
**File:** `examples/hello_world.cds`  
**Difficulty:** ⭐ Beginner  
**Time:** 2 minutes  
**Topics:** Output, Comments, Variables

**What you'll learn:**
- How to print output with `likho()`
- Using comments
- Basic string output
- Multiple languages in output

**Run:**
```bash
python codesi_production.py examples/hello_world.cds
```

---

### 2. Calculator
**File:** `examples/calculator.cds`  
**Difficulty:** ⭐ Beginner  
**Time:** 10 minutes  
**Topics:** Variables, Operators, Input, If-else

**What you'll learn:**
- Getting user input (`float_lo`, `int_lo`)
- Arithmetic operations
- If-else conditions
- Division by zero checking

**Run:**
```bash
python codesi_production.py examples/calculator.cds
```

**Key concepts:**
- `float_lo()` for decimal input
- All arithmetic operators (+, -, *, /, %, **)
- Conditional logic for validation

---

### 3. Variables Practice
**Topics:** Variables, Data types, Type checking

**Sample code:**
```codesi
// Create variables
naam = "Rishaank"
umra = 15
height = 5.8
is_student = sach

// Display
likho("Name:", naam)
likho("Age:", umra)
likho("Type:", prakar(naam))
```

**Learn:**
- Variable declaration
- Different data types
- Type checking with `prakar()`

---

### 4. If-Else Practice
**Topics:** Conditions, Comparison operators

**Sample code:**
```codesi
marks = 85

agar (marks >= 90) {
    likho("A+ Grade")
} ya_phir (marks >= 80) {
    likho("A Grade")
} ya_phir (marks >= 70) {
    likho("B Grade")
} nahi_to {
    likho("Need improvement")
}
```

**Learn:**
- If-elif-else chains
- Multiple conditions
- Grade calculation logic

---

### 5. Loop Practice
**Topics:** For loops, While loops

**Sample code:**
```codesi
// For loop
har i se 1 tak 6 {
    likho("Number:", i)
}

// While loop
count = 1
jabtak (count <= 5) {
    likho(count)
    count = count + 1
}
```

**Learn:**
- `har` loop syntax
- `jabtak` (while) loops
- Loop counters

---

## 🌿 Intermediate Examples

For those comfortable with basics, ready for more complex concepts.

### 6. Fibonacci Sequence
**File:** `examples/fibonacci.cds`  
**Difficulty:** ⭐⭐ Intermediate  
**Time:** 15 minutes  
**Topics:** Functions, Recursion, Iteration, Arrays

**What you'll learn:**
- Recursive functions
- Iterative algorithms
- Performance comparison
- Array operations

**Run:**
```bash
python codesi_production.py examples/fibonacci.cds
```

**Key concepts:**
- Two approaches: recursive vs iterative
- Function return values
- Loop optimization
- Array building

---

### 7. Array Operations
**Topics:** Arrays, Array methods, Iteration

**Sample code:**
```codesi
// Create array
numbers = [1, 2, 3, 4, 5]

// Operations
numbers.push(6)
doubled = numbers.map(lambda(x) -> x * 2)
even = numbers.filter(lambda(x) -> x % 2 == 0)

// Display
har num mein numbers {
    likho(num)
}
```

**Learn:**
- Array creation and manipulation
- Array methods (push, map, filter)
- Lambda functions
- ForEach loops

---

### 8. Object Operations
**Topics:** Objects, Properties, Methods

**Sample code:**
```codesi
person = {
    naam: "Raj",
    umra: 25,
    city: "Mumbai"
}

// Access
likho(person.naam)
likho(person["umra"])

// Modify
person.email = "raj@example.com"

// Iterate
har key mein person {
    likho(key, ":", person[key])
}
```

**Learn:**
- Object creation
- Property access (dot and bracket notation)
- Adding/modifying properties
- Object iteration

---

### 9. File Operations
**Topics:** File I/O, Error handling

**Sample code:**
```codesi
// Write file
file_likho("output.txt", "Hello Codesi!")

// Read file
try {
    content = file_padho("output.txt")
    likho(content)
} catch (e) {
    likho("Error:", e.message)
}

// Check existence
agar (file_hai("output.txt")) {
    likho("File exists")
}
```

**Learn:**
- Writing to files
- Reading files
- Error handling with try-catch
- File existence checking

---

### 10. Error Handling
**Topics:** Try-catch-finally, Throw

**Sample code:**
```codesi
karya divide(a, b) {
    agar (b == 0) {
        throw {message: "Division by zero"}
    }
    vapas a / b
}

try {
    result = divide(10, 0)
} catch (e) {
    likho("Error:", e.message)
} finally {
    likho("Cleanup complete")
}
```

**Learn:**
- Try-catch-finally blocks
- Throwing custom errors
- Error propagation
- Cleanup code

---

## 🌳 Advanced Examples

Complex applications showcasing advanced features.

### 11. OOP Example
**File:** `examples/oop_example.cds`  
**Difficulty:** ⭐⭐⭐ Advanced  
**Time:** 20 minutes  
**Topics:** Classes, Inheritance, Objects, Methods

**What you'll learn:**
- Class definition
- Constructors
- Inheritance with `extends`
- Method overriding
- Parent class access with `super`

**Run:**
```bash
python codesi_production.py examples/oop_example.cds
```

**Key concepts:**
- Person base class
- Student and Teacher child classes
- `banao` constructor
- `ye` keyword for self-reference
- Multiple objects from same class

---

### 12. Recursion Examples
**Topics:** Recursive functions, Base cases

**Sample code:**
```codesi
// Factorial
karya factorial(n) {
    agar (n <= 1) vapas 1
    vapas n * factorial(n - 1)
}

// Binary search
karya binary_search(arr, target, left, right) {
    agar (left > right) vapas -1
    
    mid = math_niche((left + right) / 2)
    
    agar (arr[mid] == target) vapas mid
    agar (arr[mid] > target) {
        vapas binary_search(arr, target, left, mid - 1)
    }
    vapas binary_search(arr, target, mid + 1, right)
}
```

**Learn:**
- Recursive thinking
- Base cases
- Recursive calls
- Algorithm implementation

---

### 13. Design Patterns
**Topics:** Singleton, Factory patterns

**Sample code:**
```codesi
// Singleton
class Database {
    static instance = khaali
    
    static karya get_instance() {
        agar (Database.instance == khaali) {
            Database.instance = new Database()
        }
        vapas Database.instance
    }
}

// Usage
db1 = Database.get_instance()
db2 = Database.get_instance()
// db1 and db2 are same instance!
```

**Learn:**
- Static methods
- Design pattern implementation
- Class-level variables
- Singleton pattern

---

## 🎯 Project Examples

Complete applications demonstrating real-world usage.

### 14. Number Guessing Game
**File:** `examples/game_number_guessing.cds`  
**Difficulty:** ⭐⭐ Intermediate  
**Time:** 15 minutes  
**Topics:** Functions, Loops, Input, Random, Conditionals

**What you'll learn:**
- Game logic implementation
- Random number generation
- User input validation
- Win/lose conditions
- Attempt tracking

**Run:**
```bash
python codesi_production.py examples/game_number_guessing.cds
```

**Features:**
- Random target generation
- Limited attempts
- Hints (too high/low)
- Score tracking
- Play again option

---

### 15. Todo List (File-based)
**Topics:** File I/O, Arrays, Functions

**Sample code:**
```codesi
karya save_todos(todos) {
    text = ""
    har todo mein todos {
        text = text + todo + "\n"
    }
    file_likho("todos.txt", text)
}

karya load_todos() {
    agar (!file_hai("todos.txt")) {
        vapas []
    }
    content = file_padho("todos.txt")
    vapas content.todo("\n")
}

karya add_todo(todos, task) {
    todos.push(task)
    save_todos(todos)
}
```

**Learn:**
- Persistent data storage
- File-based data management
- CRUD operations
- Application state

---

### 16. Contact Book
**Topics:** Objects, Arrays, JSON, File I/O

**Complete application** with:
- Add contacts
- Search contacts
- List all contacts
- JSON storage
- Error handling

**Learn:**
- Complex data structures
- JSON serialization
- Search algorithms
- Data persistence

---

### 17. Student Management System
**Topics:** Classes, Arrays, Objects, File I/O

**Features:**
- Add students
- Record marks
- Calculate averages
- Generate reports
- Save/load data

**Learn:**
- Application architecture
- Data modeling with classes
- Report generation
- File-based database

---

### 18. E-Commerce System
**Topics:** OOP, Design patterns, Complex logic

**Complete system** with:
- Product catalog
- Shopping cart
- Order processing
- User management
- Inventory tracking

**Learn:**
- Large application structure
- Multiple classes interaction
- Business logic implementation
- Real-world scenarios

---

## 🌟 Feature Demonstrations

Examples showcasing Codesi's unique features.

### 19. Time Machine Demo
**File:** `examples/time_machine_demo.cds`  
**Difficulty:** ⭐⭐ Intermediate  
**Time:** 10 minutes  
**Topics:** Time Machine, Debugging, State management

**What you'll learn:**
- Enabling Time Machine
- Taking snapshots
- Time travel (peeche/aage)
- Viewing timeline
- Variable restoration

**Run:**
```bash
python codesi_production.py examples/time_machine_demo.cds
```

**Interactive features:**
```codesi
time_machine_on()

x = 5
x = x * 2
x = x + 3

// In REPL:
peeche()     // Go back
aage()       // Go forward
timeline()   // View history
```

---

### 20. Samjho (Explain) Demo
**Topics:** Code explanation, Learning tool

**Sample code:**
```codesi
samjhao_on()  // Enable explainer

x = 10
y = 20
sum = x + y

agar (sum > 25) {
    likho("Large sum")
}

samjhao()  // Show explanation
```

**Output:**
```
📖 Code Explanation:
1. Variable 'x' mein value 10 store ki
2. Variable 'y' mein value 20 store ki
3. 🔢 Operation: 10 + 20 = 30
4. Variable 'sum' mein value 30 store ki
5. 🔀 If condition check: (sum > 25) → sach
```

---

### 21. JAADU Demo
**Topics:** Auto-correction, Typo fixing

**Run with JAADU:**
```bash
python codesi_production.py script.cds --jaadu
```

**Example with typos:**
```codesi
likho("Hello")   // Typo: likho
```

**JAADU fixes:**
```
🪄 JAADU: 'likho' → 'likho'
Hello
```

---

## 📐 Algorithm Examples

Classic algorithms implemented in Codesi.

### 22. Sorting Algorithms
**Topics:** Algorithms, Arrays, Performance

**Bubble Sort:**
```codesi
karya bubble_sort(arr) {
    n = arr.lambai()
    har i se 0 tak n {
        har j se 0 tak n - i - 1 {
            agar (arr[j] > arr[j + 1]) {
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            }
        }
    }
    vapas arr
}
```

**Learn:**
- Sorting logic
- Nested loops
- Array manipulation
- Algorithm complexity

---

### 23. Search Algorithms
**Topics:** Binary search, Linear search

**Binary Search:**
```codesi
karya binary_search(arr, target) {
    left = 0
    right = arr.lambai() - 1
    
    jabtak (left <= right) {
        mid = math_niche((left + right) / 2)
        
        agar (arr[mid] == target) {
            vapas mid
        } ya_phir (arr[mid] < target) {
            left = mid + 1
        } nahi_to {
            right = mid - 1
        }
    }
    vapas -1
}
```

---

### 24. Data Structures
**Topics:** Stack, Queue, Linked List

**Stack Implementation:**
```codesi
class Stack {
    banao() {
        ye.items = []
    }
    
    karya push(item) {
        ye.items.push(item)
    }
    
    karya pop() {
        agar (ye.is_empty()) {
            vapas khaali
        }
        vapas ye.items.pop()
    }
    
    karya is_empty() {
        vapas ye.items.lambai() == 0
    }
}
```

---

## 📊 Learning Paths

### Path 1: Complete Beginner (Week 1)
1. Hello World
2. Variables Practice
3. Calculator
4. If-Else Practice
5. Loop Practice
6. Simple Functions

**Goal:** Understand basics, write simple programs

---

### Path 2: Intermediate Developer (Week 2)
1. Fibonacci (both approaches)
2. Array Operations
3. Object Operations
4. File Operations
5. Error Handling
6. Todo List Project

**Goal:** Work with data structures, handle errors

---

### Path 3: Advanced Developer (Week 3)
1. OOP Example
2. Recursion Examples
3. Design Patterns
4. Student Management System
5. E-Commerce System
6. Algorithm Implementations

**Goal:** Build complex applications, use OOP

---

## 🎯 By Topic

### Variables & Data Types
- Hello World
- Variables Practice
- Calculator

### Control Flow
- If-Else Practice
- Loop Practice
- Switch-Case examples

### Functions
- Calculator
- Fibonacci
- Recursion Examples

### Arrays
- Array Operations
- Sorting Algorithms
- Search Algorithms

### Objects
- Object Operations
- Contact Book
- Student Management

### OOP
- OOP Example
- E-Commerce System
- Design Patterns

### File I/O
- File Operations
- Todo List
- Contact Book

### Error Handling
- Error Handling Practice
- File Operations
- All Projects

### Special Features
- Time Machine Demo
- Samjho Demo
- JAADU Demo

---

## 🚀 Running Examples

### Single File
```bash
python codesi_production.py examples/hello_world.cds
```

### With JAADU
```bash
python codesi_production.py examples/calculator.cds --jaadu
```

### With Debug
```bash
python codesi_production.py examples/fibonacci.cds --debug
```

### In REPL
```bash
python codesi_production.py

codesi:1> import_karo("examples/hello_world.cds")
```

---

## 💡 Tips for Learning

1. **Start Simple**: Begin with Hello World, progress gradually
2. **Type Everything**: Don't copy-paste, type to learn
3. **Experiment**: Modify examples, see what happens
4. **Use Features**: Try Samjho and Time Machine while learning
5. **Build Projects**: Apply concepts in your own projects
6. **Read Code**: Study example code before running
7. **Debug**: Use JAADU mode while learning

---

## 📝 Contributing Examples

Want to add your example? Follow these steps:

1. **Create** a `.cds` file in `examples/`
2. **Add comments** explaining the code
3. **Test** thoroughly
4. **Update** this index
5. **Submit** a pull request

**Example template:**
```codesi
// Title: Your Example Name
// Author: Your Name
// Difficulty: Beginner/Intermediate/Advanced
// Topics: Topic1, Topic2, Topic3

// Description of what this example demonstrates

// Your code here
```

---

## 🔗 Related Documentation

- [Quick Start Guide](QUICKSTART.md) - Get started quickly
- [Complete Basics](COMPLETE_BASICS.md) - Week 1 learning
- [Complete Intermediate](COMPLETE_INTERMEDIATE.md) - Week 2 learning
- [Complete Advanced](COMPLETE_ADVANCED.md) - Week 3 learning
- [API Reference](API_REFERENCE.md) - Quick lookup

---

**Happy Learning! 🎉**

All examples are tested and production-ready!