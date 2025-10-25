# 🚨 Codesi Error Handling Guide

Complete guide to understanding, preventing, and handling errors in Codesi.

## Table of Contents

1. [Understanding Errors](#understanding-errors)
2. [Common Error Types](#common-error-types)
3. [Try-Catch-Finally](#try-catch-finally)
4. [Custom Errors](#custom-errors)
5. [Debugging with SAMJHO](#debugging-with-samjho)
6. [Debugging with Time Machine](#debugging-with-time-machine)

---

## Understanding Errors

### Types of Errors in Codesi

1. **Syntax Errors** - Code structure galat hai
2. **Runtime Errors** - Code run hote time problem
3. **Logic Errors** - Code chalta hai but wrong result

### Error Message Format

```
❌ Codesi Error Type: Description in Hinglish
💡 Suggestion: Helpful hint (if available)
```

---

## Common Error Types

### 1. Syntax Errors

**Problem:** Code ka structure galat hai

#### Example 1: Missing Closing Brace

```hinglish
// ❌ Wrong
agar (x > 5) {
    likho("Big");
// Missing }

// ✅ Correct
agar (x > 5) {
    likho("Big");
}
```

**Error Message:**
```
❌ Codesi Syntax Error: Line 3 par '}' ki ummeed thi, lekin 'EOF' mil gaya.
```

#### Example 2: Missing Parenthesis

```hinglish
// ❌ Wrong
agar x > 5 {  // Missing ()
    likho("Big");
}

// ✅ Correct
agar (x > 5) {
    likho("Big");
}
```

**Error Message:**
```
❌ Codesi Syntax Error: Line 1 par '(' ki ummeed thi
```

#### Example 3: Invalid Expression Start

```hinglish
// ❌ Wrong
x = + 5;  // Invalid start

// ✅ Correct
x = 5;
// or
x = +5;  // Unary plus
```

**Error Message:**
```
❌ Codesi Syntax Error: Line 1 par '+' ka unexpected use hai. Expression ki starting mein iska use nahi ho sakta.
```

### 2. Runtime Errors

**Problem:** Code run hote time crash ho jata hai

#### Example 1: Undefined Variable

```hinglish
// ❌ Wrong
likho(naam);  // 'naam' defined nahi hai

// ✅ Correct
naam = "Raj";
likho(naam);
```

**Error Message:**
```
❌ Codesi Runtime Error: Variable 'naam' define nahi hai
💡 Suggestion: Kya aapka matlab 'name' tha? (if 'name' exists)
```

#### Example 2: Division by Zero

```hinglish
// ❌ Wrong
result = 10 / 0;

// ✅ Correct
karya safe_divide(a, b) {
    agar (b == 0) {
        throw {message: "Cannot divide by zero"};
    }
    vapas a / b;
}

try {
    result = safe_divide(10, 0);
} catch (error) {
    likho("Error:", error.message);
    result = 0;  // Default value
}
```

**Error Message:**
```
❌ Codesi Error: Zero se divide nahi kar sakte
```

#### Example 3: Array Index Out of Bounds

```hinglish
// ❌ Wrong
arr = [1, 2, 3];
value = arr[5];  // Index out of range

// ✅ Correct
arr = [1, 2, 3];
index = 2;

agar (index >= 0 aur index < arr.lambai()) {
    value = arr[index];
} nahi_to {
    likho("Invalid index");
    value = khaali;
}
```

**Error Message:**
```
❌ Codesi Error: Index range ke bahar hai
```

#### Example 4: Invalid Type Operation

```hinglish
// ❌ Wrong
result = "hello" - 5;  // Can't subtract number from string

// ✅ Correct
text = "hello";
number = 5;

// String concatenation
result = text + string_bnao(number);  // "hello5"

// Or check type first
agar (type_of(text) == "shabd" aur type_of(number) == "Integer") {
    result = text + string_bnao(number);
}
```

#### Example 5: Calling Non-Function

```hinglish
// ❌ Wrong
x = 10;
result = x();  // x is not a function

// ✅ Correct
karya calculate() {
    vapas 10 * 2;
}
result = calculate();
```

**Error Message:**
```
❌ Codesi Error: Non-function ko call nahi kiya ja sakta
```

### 3. Logic Errors

**Problem:** Code runs but gives wrong results

#### Example 1: Wrong Condition

```hinglish
// ❌ Wrong Logic
karya check_adult(age) {
    agar (age > 18) {  // Should be >= 18
        vapas sach;
    }
    vapas jhooth;
}

likho(check_adult(18));  // Returns jhooth (wrong!)

// ✅ Correct
karya check_adult(age) {
    agar (age >= 18) {
        vapas sach;
    }
    vapas jhooth;
}

likho(check_adult(18));  // Returns sach (correct!)
```

**Debug with SAMJHO:**
```hinglish
samjhao_on();

age = 18;
result = check_adult(age);

samjhao();  // See step-by-step execution
```

#### Example 2: Off-by-One Error

```hinglish
// ❌ Wrong - Misses last element
arr = [10, 20, 30, 40, 50];
sum = 0;

har i se 0 tak arr.lambai() - 1 {  // Wrong!
    sum = sum + arr[i];
}
// Sum will be 100 instead of 150

// ✅ Correct
arr = [10, 20, 30, 40, 50];
sum = 0;

har i se 0 tak arr.lambai() {
    sum = sum + arr[i];
}
// Sum will be 150 (correct!)

// ✅ Even Better - Use foreach
arr = [10, 20, 30, 40, 50];
sum = 0;

har num mein arr {
    sum = sum + num;
}
```

**Debug with Time Machine:**
```hinglish
time_machine_on();

arr = [10, 20, 30, 40, 50];
sum = 0;

har i se 0 tak arr.lambai() {
    sum = sum + arr[i];
}

timeline();  // See each iteration
peeche();    // Go back to check values
```

---

## Try-Catch-Finally

### Basic Try-Catch

```hinglish
try {
    // Code that might fail
    result = risky_operation();
    likho("Success:", result);
} catch (error) {
    // Handle error
    likho("Error occurred:", error.message);
}
```

### With Finally Block

```hinglish
file = khaali;

try {
    file = file_padho("data.txt");
    data = json_parse(file);
    likho("Data loaded");
} catch (error) {
    likho("Failed to load data:", error.message);
    data = {};  // Default value
} finally {
    likho("Cleanup done");
    // This always runs
}
```

### Nested Try-Catch

```hinglish
try {
    data = file_padho("config.json");
    
    try {
        config = json_parse(data);
        likho("Config loaded");
    } catch (parse_error) {
        likho("JSON parse failed");
        config = {default: sach};
    }
    
} catch (file_error) {
    likho("File read failed");
    config = {default: sach};
}
```

### Multiple Error Handling

```hinglish
karya process_data(filename) {
    // Check file exists
    agar (nahi file_hai(filename)) {
        throw {
            message: "File not found",
            code: "FILE_NOT_FOUND",
            file: filename
        };
    }
    
    // Try to read
    content = khaali;
    try {
        content = file_padho(filename);
    } catch (error) {
        throw {
            message: "Cannot read file",
            code: "READ_ERROR",
            original: error
        };
    }
    
    // Try to parse
    try {
        data = json_parse(content);
        vapas data;
    } catch (error) {
        throw {
            message: "Invalid JSON format",
            code: "PARSE_ERROR",
            content: content
        };
    }
}

// Usage
try {
    result = process_data("user.json");
    likho("Success:", result);
} catch (error) {
    likho("Error Code:", error.code);
    likho("Message:", error.message);
    
    // Handle specific errors
    agar (error.code == "FILE_NOT_FOUND") {
        likho("Please create the file:", error.file);
    } ya_phir (error.code == "PARSE_ERROR") {
        likho("Fix the JSON format");
    }
}
```

---

## Custom Errors

### Creating Error Objects

```hinglish
// Simple error
throw {message: "Something went wrong"};

// Detailed error
throw {
    message: "Invalid user age",
    code: "VALIDATION_ERROR",
    field: "age",
    value: -5,
    expected: "Age must be between 0 and 150"
};
```

### Custom Error Function

```hinglish
karya create_error(message, code, details) {
    vapas {
        message: message,
        code: code,
        details: details,
        timestamp: time_now()
    };
}

// Usage
agar (age < 0) {
    throw create_error(
        "Invalid age",
        "AGE_NEGATIVE",
        {value: age, min: 0, max: 150}
    );
}
```

### Validation Error Helper

```hinglish
karya validate_email(email) {
    agar (nahi email.included_hai("@")) {
        throw {
            message: "Email must contain @",
            field: "email",
            value: email
        };
    }
    
    agar (nahi email.included_hai(".")) {
        throw {
            message: "Email must contain domain",
            field: "email",
            value: email
        };
    }
    
    vapas sach;
}

// Usage with good error messages
try {
    validate_email("user@example");
} catch (error) {
    likho("Validation Failed:");
    likho("Field:", error.field);
    likho("Value:", error.value);
    likho("Reason:", error.message);
}
```

---

## Debugging with SAMJHO

### Enable Explanation Mode

```hinglish
samjhao_on();

x = 10;
y = 20;
result = x + y;

agar (result > 25) {
    likho("Big result");
}

samjhao();  // See detailed explanation
```

**Output:**
```
📖 Code Explanation:
============================================================
1. Variable 'x' mein value 10 store ki
2. Variable 'y' mein value 20 store ki
3. 🔢 Operation: 10 + 20 = 30
4. Variable 'result' mein expression ka result store kiya: 10 + 20 = 30
5. 🔀 If condition check: (result > 25) → sach
6. Big result
============================================================
```

### Debug Complex Functions

```hinglish
samjhao_on();

karya factorial(n) {
    agar (n <= 1) {
        vapas 1;
    }
    vapas n * factorial(n - 1);
}

result = factorial(5);
samjhao();
```

### Debug Loops

```hinglish
samjhao_on();

total = 0;
har i se 1 tak 6 {
    total = total + i;
}

samjhao();  // See each iteration explained
```

---

## Debugging with Time Machine

### Basic Time Travel

```hinglish
time_machine_on();

x = 10;
x = x * 2;
x = x + 5;

likho("Final:", x);  // 25

peeche();  // x becomes 20
likho("After going back:", x);

peeche();  // x becomes 10
likho("After going back again:", x);
```

### Debug Algorithm Step-by-Step

```hinglish
time_machine_on();

// Bubble sort
arr = [5, 2, 8, 1, 9];

har i se 0 tak arr.lambai() {
    har j se 0 tak arr.lambai() - 1 {
        agar (arr[j] > arr[j + 1]) {
            temp = arr[j];
            arr[j] = arr[j + 1];
            arr[j + 1] = temp;
        }
    }
}

likho("Sorted:", arr);

// Debug: Go back through sorting steps
peeche();  // See previous swap
peeche();  // See swap before that
timeline();  // See complete history
```

### Find Where Bug Started

```hinglish
time_machine_on();

balance = 1000;
balance = balance - 100;  // Purchase
balance = balance + 50;   // Refund
balance = balance - 200;  // Purchase
balance = balance - 800;  // Purchase (bug: went negative!)

// Find the problem
timeline();  // See all steps
peeche();    // Go back to find where it went wrong
```

### Combine SAMJHO + Time Machine

```hinglish
samjhao_on();
time_machine_on();

karya calculate_discount(price, percent) {
    discount = price * (percent / 100);
    final_price = price - discount;
    vapas final_price;
}

result = calculate_discount(1000, 20);

// Debug with both tools
samjhao();   // See explanations
timeline();  // See history
peeche();    // Go back if needed
```

---