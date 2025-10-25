# Functions in Codesi

Complete guide to functions in Codesi Programming Language.

## 📋 Table of Contents

- [Basic Functions](#basic-functions)
- [Parameters](#parameters)
- [Return Values](#return-values)
- [Default Parameters](#default-parameters)
- [Variadic Parameters](#variadic-parameters)
- [Lambda Functions](#lambda-functions)
- [Higher-Order Functions](#higher-order-functions)
- [Closures](#closures)
- [Recursion](#recursion)
- [Best Practices](#best-practices)

---

## 🔧 Basic Functions

### Function Declaration

```codesi
karya function_name(parameters) {
    // function body
}
```

### Simple Function

```codesi
karya greet() {
    likho("Hello, World!")
}

greet()  // Call the function
```

### Function with Parameters

```codesi
karya greet_person(naam) {
    likho("Hello,", naam, "!")
}

greet_person("Rishaank")  // Hello, Rishaank!
greet_person("Priya")     // Hello, Priya!
```

---

## 📥 Parameters

### Single Parameter

```codesi
karya square(x) {
    result = x * x
    likho(result)
}

square(5)   // 25
square(10)  // 100
```

### Multiple Parameters

```codesi
karya add(a, b) {
    result = a + b
    likho("Sum:", result)
}

add(5, 3)    // Sum: 8
add(10, 20)  // Sum: 30
```

### Parameter Order Matters

```codesi
karya divide(a, b) {
    likho(a, "/", b, "=", a / b)
}

divide(10, 2)  // 10 / 2 = 5.0
divide(2, 10)  // 2 / 10 = 0.2
```

---

## 📤 Return Values

### Returning Values

```codesi
karya add(a, b) {
    vapas a + b
}

result = add(5, 3)
likho(result)  // 8

// Use in expressions
total = add(10, 20) + add(5, 5)
likho(total)  // 40
```

### Multiple Return Statements

```codesi
karya get_grade(marks) {
    agar (marks >= 90) {
        vapas "A+"
    } ya_phir (marks >= 80) {
        vapas "A"
    } ya_phir (marks >= 70) {
        vapas "B"
    } ya_phir (marks >= 60) {
        vapas "C"
    } nahi_to {
        vapas "F"
    }
}

likho(get_grade(95))  // A+
likho(get_grade(75))  // B
```

### Returning Complex Values

```codesi
// Return array
karya get_stats(numbers) {
    total = 0
    har num mein numbers {
        total = total + num
    }
    avg = total / numbers.lambai()
    
    vapas [total, avg, numbers.lambai()]
}

stats = get_stats([10, 20, 30, 40, 50])
likho("Total:", stats[0])    // 150
likho("Average:", stats[1])   // 30
likho("Count:", stats[2])     // 5

// Return object
karya create_user(naam, email) {
    vapas {
        naam: naam,
        email: email,
        created_at: time_now(),
        is_active: sach
    }
}

user = create_user("Rishaank", "rishaank@codesi.dev")
likho(user.naam)   // Rishaank
likho(user.email)  // rishaank@codesi.dev
```

---

## ⚙️ Default Parameters

### Basic Default Values

```codesi
karya greet(naam = "Guest") {
    likho("Hello,", naam, "!")
}

greet("Rishaank")  // Hello, Rishaank!
greet()            // Hello, Guest!
```

### Multiple Defaults

```codesi
karya create_user(naam, role = "member", status = "active") {
    likho("Creating user:", naam)
    likho("Role:", role)
    likho("Status:", status)
}

create_user("Raj")                    // Uses both defaults
create_user("Priya", "admin")         // Uses status default
create_user("Amit", "moderator", "pending")  // No defaults
```

### Mix Required and Default

```codesi
karya calculate_price(base_price, tax = 0.18, discount = 0) {
    after_tax = base_price + (base_price * tax)
    final_price = after_tax - discount
    vapas final_price
}

likho(calculate_price(100))              // 118.0
likho(calculate_price(100, 0.20))        // 120.0
likho(calculate_price(100, 0.18, 20))    // 98.0
```

---

## 📦 Variadic Parameters

Accept unlimited arguments using `...`

### Basic Variadic

```codesi
karya sum(...numbers) {
    total = 0
    har num mein numbers {
        total = total + num
    }
    vapas total
}

likho(sum(1, 2, 3))           // 6
likho(sum(10, 20, 30, 40))    // 100
likho(sum(5))                  // 5
```

### Mix Regular and Variadic

```codesi
karya log(level, ...messages) {
    likho("[", level, "]")
    har msg mein messages {
        likho("-", msg)
    }
}

log("INFO", "Server started")
log("ERROR", "Connection failed", "Retrying...", "Failed again")
```

### Variadic with Operations

```codesi
karya multiply_all(...numbers) {
    agar (numbers.lambai() == 0) {
        vapas 0
    }
    
    result = 1
    har num mein numbers {
        result = result * num
    }
    vapas result
}

likho(multiply_all(2, 3, 4))      // 24
likho(multiply_all(5, 5))         // 25
```

---

## 🎯 Lambda Functions

Anonymous functions with arrow syntax.

### Basic Lambda

```codesi
// Assign to variable
square = lambda(x) -> x * x

likho(square(5))   // 25
likho(square(10))  // 100
```

### Lambda with Multiple Parameters

```codesi
add = lambda(a, b) -> a + b
multiply = lambda(a, b) -> a * b

likho(add(5, 3))       // 8
likho(multiply(4, 5))  // 20
```

### Lambda in Array Methods

```codesi
numbers = [1, 2, 3, 4, 5]

// Map
doubled = numbers.map(lambda(x) -> x * 2)
likho(doubled)  // [2, 4, 6, 8, 10]

// Filter
even = numbers.filter(lambda(x) -> x % 2 == 0)
likho(even)  // [2, 4]

// Reduce
sum = numbers.reduce(lambda(acc, x) -> acc + x, 0)
likho(sum)  // 15
```

### Multi-Line Lambda

```codesi
process = lambda(x) -> {
    temp = x * 2
    temp = temp + 10
    vapas temp
}

likho(process(5))   // 20
likho(process(10))  // 30
```

---

## 🎭 Higher-Order Functions

Functions that accept or return other functions.

### Function as Parameter

```codesi
karya apply_operation(a, b, operation) {
    vapas operation(a, b)
}

// Pass different operations
result1 = apply_operation(10, 5, lambda(x, y) -> x + y)
likho(result1)  // 15

result2 = apply_operation(10, 5, lambda(x, y) -> x * y)
likho(result2)  // 50

// Named function as parameter
karya divide_func(a, b) {
    vapas a / b
}

result3 = apply_operation(10, 5, divide_func)
likho(result3)  // 2.0
```

### Function Returning Function

```codesi
karya multiplier(factor) {
    vapas lambda(x) -> x * factor
}

double = multiplier(2)
triple = multiplier(3)
times_ten = multiplier(10)

likho(double(5))      // 10
likho(triple(5))      // 15
likho(times_ten(5))   // 50
```

### Array Processing

```codesi
karya process_array(arr, processor) {
    result = []
    har item mein arr {
        result.push(processor(item))
    }
    vapas result
}

numbers = [1, 2, 3, 4, 5]

// Square all
squared = process_array(numbers, lambda(x) -> x * x)
likho(squared)  // [1, 4, 9, 16, 25]

// Add 10 to all
added = process_array(numbers, lambda(x) -> x + 10)
likho(added)  // [11, 12, 13, 14, 15]
```

### Custom Filters

```codesi
karya custom_filter(arr, condition) {
    result = []
    har item mein arr {
        agar (condition(item)) {
            result.push(item)
        }
    }
    vapas result
}

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

// Get even numbers
even = custom_filter(numbers, lambda(x) -> x % 2 == 0)
likho(even)  // [2, 4, 6, 8, 10]

// Numbers greater than 5
big = custom_filter(numbers, lambda(x) -> x > 5)
likho(big)  // [6, 7, 8, 9, 10]
```

---

## 🔐 Closures

Functions that remember variables from their creation scope.

### Basic Closure

```codesi
karya counter() {
    count = 0
    
    vapas lambda() -> {
        count = count + 1
        vapas count
    }
}

counter1 = counter()
likho(counter1())  // 1
likho(counter1())  // 2
likho(counter1())  // 3

counter2 = counter()  // New counter
likho(counter2())  // 1
likho(counter2())  // 2
```

### Closure with Parameters

```codesi
karya make_adder(x) {
    vapas lambda(y) -> x + y
}

add5 = make_adder(5)
add10 = make_adder(10)

likho(add5(3))   // 8
likho(add10(3))  // 13
```

### Private Variables

```codesi
karya create_bank_account(initial_balance) {
    balance = initial_balance
    
    vapas {
        deposit: lambda(amount) -> {
            balance = balance + amount
            vapas balance
        },
        withdraw: lambda(amount) -> {
            agar (amount > balance) {
                vapas "Insufficient funds"
            }
            balance = balance - amount
            vapas balance
        },
        get_balance: lambda() -> balance
    }
}

account = create_bank_account(1000)
likho(account.get_balance())      // 1000
likho(account.deposit(500))       // 1500
likho(account.withdraw(200))      // 1300
likho(account.get_balance())      // 1300
```

---

## 🔄 Recursion

Functions that call themselves.

### Simple Recursion

```codesi
karya countdown(n) {
    agar (n <= 0) {
        likho("Blast off!")
        vapas
    }
    
    likho(n)
    countdown(n - 1)
}

countdown(5)
// Output: 5 4 3 2 1 Blast off!
```

### Factorial

```codesi
karya factorial(n) {
    agar (n <= 1) {
        vapas 1
    }
    vapas n * factorial(n - 1)
}

likho(factorial(5))  // 120
likho(factorial(7))  // 5040
```

### Fibonacci

```codesi
karya fibonacci(n) {
    agar (n <= 1) {
        vapas n
    }
    vapas fibonacci(n - 1) + fibonacci(n - 2)
}

// Generate sequence
har i se 0 tak 10 {
    likho("Fib(", i, ") =", fibonacci(i))
}
```

### Sum of Array (Recursive)

```codesi
karya sum_array(arr, index = 0) {
    agar (index >= arr.lambai()) {
        vapas 0
    }
    vapas arr[index] + sum_array(arr, index + 1)
}

numbers = [1, 2, 3, 4, 5]
likho(sum_array(numbers))  // 15
```

### Tree Traversal

```codesi
karya sum_tree(node) {
    agar (node == khaali) {
        vapas 0
    }
    
    total = node.value
    
    agar (node.left != khaali) {
        total = total + sum_tree(node.left)
    }
    
    agar (node.right != khaali) {
        total = total + sum_tree(node.right)
    }
    
    vapas total
}

// Create tree
tree = {
    value: 10,
    left: {
        value: 5,
        left: khaali,
        right: khaali
    },
    right: {
        value: 15,
        left: khaali,
        right: khaali
    }
}

likho(sum_tree(tree))  // 30
```

---

## 🎨 Type Annotations

Optional type hints for parameters and return values.

### Parameter Types

```codesi
karya greet(naam: string) {
    likho("Hello,", naam)
}

karya add(a: int, b: int) {
    vapas a + b
}
```

### Return Type Annotations

```codesi
karya get_name() -> string {
    vapas "Rishaank"
}

karya calculate(a: int, b: int) -> int {
    vapas a + b
}

karya get_user() -> object {
    vapas {naam: "Raj", umra: 25}
}
```

### Full Annotations

```codesi
karya process_data(data: array, threshold: int) -> array {
    result = []
    har item mein data {
        agar (item > threshold) {
            result.push(item)
        }
    }
    vapas result
}
```

---

## 💡 Best Practices

### 1. Descriptive Names

```codesi
// ✅ Good
karya calculate_total_price(items, tax_rate) {
    // ...
}

// ❌ Bad
karya calc(x, y) {
    // ...
}
```

### 2. Single Responsibility

```codesi
// ✅ Good - each function does one thing
karya get_user_by_id(id) {
    vapas database.find_user(id)
}

karya validate_user(user) {
    vapas user != khaali aur user.is_active == sach
}

karya send_welcome_email(user) {
    email.send(user.email, "Welcome!")
}

// ❌ Bad - does too many things
karya process_user(id) {
    user = database.find_user(id)
    agar (user != khaali aur user.is_active) {
        email.send(user.email, "Welcome!")
        log.write("User processed")
        update_stats()
    }
}
```

### 3. Use Default Parameters

```codesi
// ✅ Good
karya create_user(naam, role = "member", status = "active") {
    // ...
}

// ❌ Bad - too many function versions
karya create_user_basic(naam) {
    // ...
}

karya create_user_with_role(naam, role) {
    // ...
}
```

### 4. Keep Functions Small

```codesi
// ✅ Good - small, focused functions
karya validate_email(email) {
    vapas email.included_hai("@")
}

karya validate_password(password) {
    vapas password.lambai() >= 8
}

karya validate_user_input(email, password) {
    agar (!validate_email(email)) {
        vapas "Invalid email"
    }
    agar (!validate_password(password)) {
        vapas "Weak password"
    }
    vapas "Valid"
}
```

### 5. Avoid Side Effects

```codesi
// ✅ Good - pure function
karya add(a, b) {
    vapas a + b
}

// ❌ Bad - modifies external state
global_count = 0

karya add_and_count(a, b) {
    global_count = global_count + 1  // Side effect!
    vapas a + b
}
```

### 6. Return Early

```codesi
// ✅ Good - early returns
karya process_age(age) {
    agar (age < 0) vapas "Invalid"
    agar (age < 13) vapas "Child"
    agar (age < 20) vapas "Teen"
    vapas "Adult"
}

// ❌ Bad - nested ifs
karya process_age(age) {
    agar (age >= 0) {
        agar (age < 13) {
            vapas "Child"
        } nahi_to {
            agar (age < 20) {
                vapas "Teen"
            } nahi_to {
                vapas "Adult"
            }
        }
    } nahi_to {
        vapas "Invalid"
    }
}
```

---

## 🚨 Common Mistakes

### 1. Missing Return

```codesi
// ❌ Wrong - no return
karya add(a, b) {
    result = a + b
    // Missing: vapas result
}

// ✅ Correct
karya add(a, b) {
    vapas a + b
}
```

### 2. Wrong Parameter Order

```codesi
// ❌ Confusing
karya divide(divisor, dividend) {
    vapas dividend / divisor
}

// ✅ Clear
karya divide(dividend, divisor) {
    vapas dividend / divisor
}
```

### 3. Not Handling Edge Cases

```codesi
// ❌ Missing validation
karya divide(a, b) {
    vapas a / b  // Error if b is 0!
}

// ✅ With validation
karya divide(a, b) {
    agar (b == 0) {
        throw {message: "Cannot divide by zero"}
    }
    vapas a / b
}
```

---

## 🎯 Advanced Patterns

### Memoization

```codesi
karya create_memoized_fibonacci() {
    cache = {}
    
    karya fib(n) {
        agar (cache.hai_kya(string_bnao(n))) {
            vapas cache[string_bnao(n)]
        }
        
        agar (n <= 1) {
            vapas n
        }
        
        result = fib(n - 1) + fib(n - 2)
        cache[string_bnao(n)] = result
        vapas result
    }
    
    vapas fib
}

fast_fib = create_memoized_fibonacci()
likho(fast_fib(40))  // Much faster!
```

### Currying

```codesi
karya curry_add(a) {
    vapas lambda(b) -> {
        vapas lambda(c) -> a + b + c
    }
}

add5 = curry_add(5)
add5and10 = add5(10)
result = add5and10(3)
likho(result)  // 18

// Or chain it
likho(curry_add(5)(10)(3))  // 18
```

### Partial Application

```codesi
karya partial(func, ...fixed_args) {
    vapas lambda(...remaining_args) -> {
        all_args = fixed_args
        har arg mein remaining_args {
            all_args.push(arg)
        }
        vapas func(...all_args)
    }
}

karya multiply_three(a, b, c) {
    vapas a * b * c
}

multiply_by_2_and_3 = partial(multiply_three, 2, 3)
likho(multiply_by_2_and_3(4))  // 24
```

---

## 📚 Summary

### Function Types

| Type | Syntax | Use Case |
|------|--------|----------|
| Named | `karya naam() {}` | Reusable logic |
| Lambda | `lambda(x) -> x * 2` | Inline operations |
| Method | `karya method() {}` | Class behavior |
| Static | `static karya func() {}` | Utility functions |

### Key Concepts

1. **Parameters**: Input to functions
2. **Return Values**: Output from functions
3. **Default Parameters**: Optional arguments
4. **Variadic**: Unlimited arguments
5. **Lambda**: Anonymous functions
6. **Higher-Order**: Functions as values
7. **Closures**: Remember outer scope
8. **Recursion**: Self-calling functions

### Quick Reference

```codesi
// Basic
karya greet(naam) {
    likho("Hello", naam)
}

// With return
karya add(a, b) {
    vapas a + b
}

// Default parameters
karya create(naam = "Guest") {
    vapas {naam: naam}
}

// Variadic
karya sum(...nums) {
    total = 0
    har n mein nums { total += n }
    vapas total
}

// Lambda
square = lambda(x) -> x * x

// Higher-order
karya apply(f, x) {
    vapas f(x)
}
```

---

**Next**: [Complete Basics Guide](COMPLETE_BASICS.md)