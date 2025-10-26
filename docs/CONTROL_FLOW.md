# Control Flow in Codesi

Complete guide to control flow statements in Codesi.

## 📋 Table of Contents

- [If-Else Statements](#if-else-statements)
- [Loops](#loops)
- [Switch-Case](#switch-case)
- [Break and Continue](#break-and-continue)
- [Ternary Operator](#ternary-operator)
- [Pattern Matching](#pattern-matching)

---

## 🔀 If-Else Statements

### Basic If Statement

```codesi
// Simple if
agar (condition) {
    // code executes if condition is sach
}

// Example
age = 20
agar (age >= 18) {
    likho("You can vote!")
}
```

**Syntax Rules**:
- Condition must be in parentheses `()`
- Braces `{}` are required for blocks
- Single statements can omit braces

---

### If-Else

```codesi
agar (condition) {
    // code if sach
} nahi_to {
    // code if jhooth
}

// Example
marks = 55
agar (marks >= 40) {
    likho("Pass")
} nahi_to {
    likho("Fail")
}
```

---

### If-Elif-Else Chain

```codesi
agar (condition1) {
    // code for condition1
} ya_phir (condition2) {
    // code for condition2
} ya_phir (condition3) {
    // code for condition3
} nahi_to {
    // code if all conditions are jhooth
}

// Example: Grade Calculator
marks = 85

agar (marks >= 90) {
    likho("A+ Grade")
} ya_phir (marks >= 80) {
    likho("A Grade")
} ya_phir (marks >= 70) {
    likho("B Grade")
} ya_phir (marks >= 60) {
    likho("C Grade")
} ya_phir (marks >= 40) {
    likho("D Grade")
} nahi_to {
    likho("Fail")
}
```

**Multiple elif blocks** are supported!

---

### Single-Line If (No Braces)

```codesi
// Single statement
agar (x > 5) likho("Big number")

// With else
agar (x > 5) likho("Big") nahi_to likho("Small")
```

**Note**: This works but braces are recommended for clarity.

---

### Nested If Statements

```codesi
agar (age >= 18) {
    agar (has_license == sach) {
        likho("Can drive")
    } nahi_to {
        likho("Get a license first")
    }
} nahi_to {
    likho("Too young to drive")
}

// Complex nesting
agar (is_logged_in) {
    agar (is_admin) {
        likho("Admin Panel")
    } ya_phir (is_moderator) {
        likho("Moderator Panel")
    } nahi_to {
        likho("User Panel")
    }
} nahi_to {
    likho("Please login")
}
```

---

### Complex Conditions

```codesi
// AND operator
agar ((age >= 18) aur (has_id == sach)) {
    likho("Entry allowed")
}

// OR operator
agar ((is_student == sach) ya (is_teacher == sach)) {
    likho("Educational discount available")
}

// NOT operator
agar (nahi is_blocked) {
    likho("Access granted")
}

// Combined
agar (((age >= 18) aur (has_ticket == sach)) ya (is_vip == sach)) {
    likho("Welcome!")
}
```

---

## 🔁 Loops

Codesi supports **multiple loop syntaxes** for flexibility!

---

### For Loop - Syntax Variant 1

Simple range syntax:

```codesi
har i se 0 tak 5 {
    likho(i)  // 0, 1, 2, 3, 4
}

// From 1 to 10
har i se 1 tak 11 {
    likho(i)  // 1, 2, 3, ..., 10
}
```

**Key Points**:
- `se` = from (inclusive)
- `tak` = to (exclusive)
- No parentheses needed

---

### For Loop - Syntax Variant 2

With parentheses and `ke liye`:

```codesi
har i ke liye (0 se 5 tak) {
    likho(i)  // 0, 1, 2, 3, 4
}

// More examples
har num ke liye (10 se 20 tak) {
    likho(num)
}
```

**Key Points**:
- Uses `ke liye` (for)
- Parentheses required
- Same range logic

---

### For Loop - With Variables

```codesi
start = 1
end = 10

har i se start tak end {
    likho("Number:", i)
}

// Dynamic ranges
n = int_lo("Enter limit: ")
har i se 1 tak n + 1 {
    likho(i)
}
```

---

### ForEach Loop - Syntax Variant 1

Direct iteration:

```codesi
fruits = ["Apple", "Banana", "Orange"]

har fruit mein fruits {
    likho(fruit)
}

// With numbers
numbers = [10, 20, 30, 40]
har num mein numbers {
    likho(num)
}
```

**Key Points**:
- `mein` = in
- Iterates over array elements
- No index access

---

### ForEach Loop - Syntax Variant 2

With `ke liye`:

```codesi
fruits = ["Apple", "Banana", "Orange"]

har fruit ke liye fruits mein {
    likho(fruit)
}
```

**Both syntaxes are equivalent!**

---

### ForEach with Objects

Iterates over keys:

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

### ForEach with Strings

Iterates over characters:

```codesi
text = "hello"

har char mein text {
    likho(char)
}
// Output: h e l l o (each on new line)
```

---

### While Loop

Execute while condition is true:

```codesi
count = 0
jabtak (count < 5) {
    likho(count)
    count = count + 1
}
// Output: 0 1 2 3 4

// Input validation example
password = ""
jabtak (password != "secret") {
    password = input_lo("Enter password: ")
}
likho("Access granted!")
```

**Key Points**:
- `jabtak` = while
- Condition in parentheses
- Check before execution

---

### Do-While Loop

Execute at least once, then check condition:

```codesi
count = 0
karo {
    likho(count)
    count = count + 1
} jabtak (count < 5)

// Menu example
karo {
    likho("1. Play")
    likho("2. Settings")
    likho("3. Exit")
    choice = int_lo("Choose: ")
    
    agar (choice == 1) {
        likho("Starting game...")
    }
} jabtak (choice != 3)
```

**Key Points**:
- `karo` = do
- Executes before checking
- Guaranteed at least one execution

---

### Infinite Loops

```codesi
// Infinite while
jabtak (sach) {
    input = input_lo("Command: ")
    agar (input == "exit") {
        break
    }
    likho("Processing:", input)
}

// Infinite for (large range)
har i se 0 tak 999999 {
    agar (some_condition) {
        break
    }
}
```

---

### Nested Loops

```codesi
// Multiplication table
har i se 1 tak 11 {
    har j se 1 tak 11 {
        likho(i, "x", j, "=", i * j)
    }
    likho("---")
}

// Pattern printing
har row se 1 tak 6 {
    line = ""
    har col se 1 tak row + 1 {
        line = line + "* "
    }
    likho(line)
}
// Output:
// * 
// * * 
// * * * 
// * * * * 
// * * * * * 
```

---

### Loop with Array Methods

```codesi
numbers = [1, 2, 3, 4, 5]

// Using forEach
har num mein numbers {
    likho(num * 2)
}

// Using map
doubled = numbers.map(lambda(x) -> x * 2)
likho(doubled)

// Using filter
even = numbers.filter(lambda(x) -> x % 2 == 0)
likho(even)
```

---

## 🎯 Switch-Case

Pattern matching with multiple cases:

```codesi
variable ke case mein {
    value1 -> statement
    value2 -> statement
    default -> statement
}
```

### Basic Switch

```codesi
day = 3

day ke case mein {
    1 -> likho("Monday")
    2 -> likho("Tuesday")
    3 -> likho("Wednesday")
    4 -> likho("Thursday")
    5 -> likho("Friday")
    6 -> likho("Saturday")
    7 -> likho("Sunday")
    default -> likho("Invalid day")
}
```

---

### Switch with Multiple Statements

```codesi
grade = "A"

grade ke case mein {
    "A" -> {
        likho("Excellent!")
        score = 95
        likho("Score:", score)
    }
    "B" -> {
        likho("Good!")
        score = 85
    }
    "C" -> {
        likho("Average")
        score = 75
    }
    default -> {
        likho("Need improvement")
        score = 50
    }
}
```

---

### Switch with String Values

```codesi
command = "start"

command ke case mein {
    "start" -> likho("Starting system...")
    "stop" -> likho("Stopping system...")
    "restart" -> likho("Restarting...")
    "status" -> likho("System is running")
    default -> likho("Unknown command")
}
```

---

### Switch with Numbers

```codesi
status_code = 404

status_code ke case mein {
    200 -> likho("OK")
    201 -> likho("Created")
    400 -> likho("Bad Request")
    401 -> likho("Unauthorized")
    404 -> likho("Not Found")
    500 -> likho("Server Error")
    default -> likho("Unknown status")
}
```

---

## 🛑 Break and Continue

### Break Statement

Exit loop immediately:

```codesi
// Exit when found
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

har num mein numbers {
    agar (num == 5) {
        likho("Found 5!")
        break
    }
    likho(num)
}
// Output: 1 2 3 4 Found 5!

// Search example
names = ["Raj", "Priya", "Amit", "Neha"]
search = "Amit"
found = jhooth

har naam mein names {
    agar (naam == search) {
        likho("Found:", naam)
        found = sach
        break
    }
}

agar (!found) {
    likho("Not found")
}
```

---

### Continue Statement

Skip current iteration:

```codesi
// Skip even numbers
har i se 1 tak 11 {
    agar (i % 2 == 0) {
        continue  // Skip even
    }
    likho(i)  // Only odd numbers
}
// Output: 1 3 5 7 9

// Skip specific values
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

har num mein numbers {
    agar (num == 5 ya num == 7) {
        continue  // Skip 5 and 7
    }
    likho(num)
}
```

---

### Break in Nested Loops

```codesi
// Break only inner loop
har i se 1 tak 4 {
    likho("Outer:", i)
    har j se 1 tak 6 {
        agar (j == 3) {
            break  // Breaks inner loop only
        }
        likho("  Inner:", j)
    }
}

// Find in 2D array
matrix = [[1, 2], [3, 4], [5, 6]]
target = 4
found = jhooth

har row mein matrix {
    har val mein row {
        agar (val == target) {
            likho("Found at position")
            found = sach
            break
        }
    }
    agar (found) {
        break  // Break outer loop too
    }
}
```

---

## ❓ Ternary Operator

Inline conditional expression:

```codesi
result = condition ? true_value : false_value
```

### Basic Ternary

```codesi
age = 20
status = (age >= 18) ? "Adult" : "Minor"
likho(status)  // "Adult"

// With numbers
x = 10
y = 20
max = (x > y) ? x : y
likho("Max:", max)  // 20
```

---

### Nested Ternary

```codesi
marks = 85
grade = (marks >= 90) ? "A+" :
        (marks >= 80) ? "A" :
        (marks >= 70) ? "B" :
        (marks >= 60) ? "C" : "Fail"

likho("Grade:", grade)  // "A"
```

---

### Ternary with Function Calls

```codesi
is_valid = sach
message = is_valid ? get_success_msg() : get_error_msg()

// Inline operations
discount = (is_member == sach) ? price * 0.9 : price
```

---

## 🎯 Pattern Matching Techniques

### Guard Clauses

```codesi
karya process_age(age) {
    // Early returns for validation
    agar (age < 0) {
        vapas "Invalid age"
    }
    
    agar (age < 13) {
        vapas "Child"
    }
    
    agar (age < 20) {
        vapas "Teenager"
    }
    
    agar (age < 60) {
        vapas "Adult"
    }
    
    vapas "Senior"
}
```

---

### Type-Based Branching

```codesi
karya process(value) {
    agar (string_hai(value)) {
        likho("Processing string:", value.bada_karo())
    } ya_phir (int_hai(value)) {
        likho("Processing number:", value * 2)
    } ya_phir (array_hai(value)) {
        likho("Processing array of length:", value.lambai())
    } nahi_to {
        likho("Unknown type")
    }
}
```

---

## 💡 Best Practices

### 1. Use Appropriate Loop Type

```codesi
// ✅ Good - for known iterations
har i se 0 tak 10 {
    likho(i)
}

// ✅ Good - for collections
har item mein collection {
    process(item)
}

// ✅ Good - for unknown iterations
jabtak (condition) {
    // do something
}
```

---

### 2. Avoid Deep Nesting

```codesi
// ❌ Bad - too nested
agar (a) {
    agar (b) {
        agar (c) {
            agar (d) {
                // code
            }
        }
    }
}

// ✅ Good - early returns
karya check() {
    agar (!a) vapas
    agar (!b) vapas
    agar (!c) vapas
    agar (!d) vapas
    // code
}

// ✅ Good - combine conditions
agar (a aur b aur c aur d) {
    // code
}
```

---

### 3. Use Switch for Multiple Values

```codesi
// ❌ Bad - long if-elif chain
agar (x == 1) {
    action1()
} ya_phir (x == 2) {
    action2()
} ya_phir (x == 3) {
    action3()
}

// ✅ Good - switch
x ke case mein {
    1 -> action1()
    2 -> action2()
    3 -> action3()
}
```

---

### 4. Break Infinite Loops

```codesi
// ✅ Always have exit condition
jabtak (sach) {
    input = input_lo("Command: ")
    agar (input == "exit") {
        break  // Important!
    }
    process(input)
}
```

---

## 🚨 Common Mistakes

### 1. Missing Parentheses

```codesi
// ❌ Error
agar x > 5 {
    likho("Big")
}

// ✅ Correct
agar (x > 5) {
    likho("Big")
}
```

---

### 2. Assignment vs Comparison

```codesi
// ❌ Wrong - assignment
agar (x = 5) {
    // This assigns 5 to x!
}

// ✅ Correct - comparison
agar (x == 5) {
    // This compares
}
```

---

### 3. Forgetting Break in Loops

```codesi
// ❌ Infinite loop
jabtak (sach) {
    likho("Forever")
    // No break!
}

// ✅ Proper exit
jabtak (sach) {
    agar (done) {
        break
    }
}
```

---

## 📚 Summary

### Control Flow Statements

| Statement | Keyword | Purpose |
|-----------|---------|---------|
| If | `agar` | Conditional execution |
| Else | `nahi_to` | Alternative path |
| Elif | `ya_phir` | Multiple conditions |
| While | `jabtak` | Condition-based loop |
| Do-While | `karo ... jabtak` | Execute-then-check loop |
| For | `har ... se ... tak` | Range-based loop |
| ForEach | `har ... mein` | Collection iteration |
| Switch | `... ke case mein` | Pattern matching |
| Break | `break` | Exit loop |
| Continue | `continue` | Skip iteration |
| Ternary | `? :` | Inline condition |

---

**Next**: [Functions Guide](FUNCTIONS.md)
