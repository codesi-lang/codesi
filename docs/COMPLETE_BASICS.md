# Complete Basics - Week 1 Learning Path

Complete beginner's guide to Codesi Programming Language.

## 🎯 Learning Goals

By the end of this week, you will:
- ✅ Write and run basic Codesi programs
- ✅ Understand variables and data types
- ✅ Use operators and expressions
- ✅ Write conditional statements
- ✅ Create and use loops
- ✅ Build simple functions

**Time Required**: 7 days, 1-2 hours per day

---

## 📅 Day 1: Getting Started

### Morning Session (30 mins)

#### 1. Installation
- Download Codesi
- Run your first program

```codesi
likho("Namaste Duniya!")
likho("Welcome to Codesi!")
```

#### 2. REPL Mode
```bash
python codesi_production.py
```

Try these:
```codesi
codesi:1> likho("Hello")
codesi:2> 2 + 2
codesi:3> "Rishaank" + " Gupta"
```

### Afternoon Session (1 hour)

#### 3. Comments
```codesi
// This is a comment
// Comments help explain code

likho("This will run")
// likho("This won't run")
```

#### Practice Exercise
Create `day1.cds`:
```codesi
// My First Codesi Program
// Author: [Your Name]

likho("Hello from Codesi!")
likho("I am learning programming")
likho("2 + 2 =", 2 + 2)
```

---

## 📅 Day 2: Variables and Data Types

### Morning Session (45 mins)

#### 1. Variables
```codesi
// Creating variables
naam = "Rishaank"
umra = 15
height = 5.8
is_student = sach

// Using variables
likho("Mera naam", naam, "hai")
likho("Main", umra, "saal ka hun")
```

#### 2. Data Types
```codesi
// Numbers
age = 15            // Integer
price = 99.99       // Float

// Strings
naam = "Raj"
message = 'Hello'

// Booleans
is_adult = sach     // True
is_minor = jhooth   // False

// Null
value = khaali      // None/Null
```

### Afternoon Session (1 hour)

#### 3. Type Checking
```codesi
x = 10
likho(prakar(x))  // "Integer"

naam = "Raj"
likho(prakar(naam))  // "shabd"
```

#### Practice Exercise
Create `day2_profile.cds`:
```codesi
// My Profile
naam = "[Your Name]"
umra = [Your Age]
city = "[Your City]"
hobby = "[Your Hobby]"
is_programmer = sach

likho("Profile Information")
likho("==================")
likho("Name:", naam)
likho("Age:", umra)
likho("City:", city)
likho("Hobby:", hobby)
likho("Programmer?", is_programmer)
```

---

## 📅 Day 3: Operators

### Morning Session (45 mins)

#### 1. Arithmetic Operators
```codesi
a = 10
b = 3

likho("Addition:", a + b)       // 13
likho("Subtraction:", a - b)    // 7
likho("Multiplication:", a * b) // 30
likho("Division:", a / b)       // 3.333...
likho("Modulo:", a % b)         // 1
likho("Power:", a ** b)         // 1000
```

#### 2. Comparison Operators
```codesi
x = 10
y = 20

likho(x == y)   // jhooth
likho(x != y)   // sach
likho(x < y)    // sach
likho(x > y)    // jhooth
likho(x <= 10)  // sach
likho(y >= 20)  // sach
```

### Afternoon Session (1 hour)

#### 3. Logical Operators
```codesi
age = 20
has_id = sach

// AND
agar ((age >= 18) aur (has_id == sach)) {
    likho("Can enter")
}

// OR
is_student = jhooth
is_teacher = sach

agar (is_student ya is_teacher) {
    likho("Educational discount available")
}

// NOT
is_blocked = jhooth
agar (nahi is_blocked) {
    likho("Access granted")
}
```

#### Practice Exercise
Create `day3_calculator.cds`:
```codesi
// Simple Calculator
a = 15
b = 4

likho("Calculator Results")
likho("================")
likho(a, "+", b, "=", a + b)
likho(a, "-", b, "=", a - b)
likho(a, "*", b, "=", a * b)
likho(a, "/", b, "=", a / b)
likho(a, "%", b, "=", a % b)
likho(a, "**", b, "=", a ** b)
```

---

## 📅 Day 4: If-Else Statements

### Morning Session (45 mins)

#### 1. Simple If
```codesi
age = 20

agar (age >= 18) {
    likho("Adult")
}
```

#### 2. If-Else
```codesi
marks = 55

agar (marks >= 40) {
    likho("Pass")
} nahi_to {
    likho("Fail")
}
```

### Afternoon Session (1 hour)

#### 3. If-Elif-Else
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

#### Practice Exercise
Create `day4_age_checker.cds`:
```codesi
// Age Group Checker
age = 25

agar (age < 0) {
    likho("Invalid age")
} ya_phir (age < 13) {
    likho("Child")
} ya_phir (age < 20) {
    likho("Teenager")
} ya_phir (age < 60) {
    likho("Adult")
} nahi_to {
    likho("Senior Citizen")
}
```

---

## 📅 Day 5: Loops

### Morning Session (45 mins)

#### 1. For Loop
```codesi
// Basic for loop
har i se 1 tak 6 {
    likho("Number:", i)
}

// With parentheses
har i ke liye (0 se 5 tak) {
    likho(i)
}
```

#### 2. While Loop
```codesi
count = 1

jabtak (count <= 5) {
    likho("Count:", count)
    count = count + 1
}
```

### Afternoon Session (1 hour)

#### 3. ForEach Loop (Arrays)
```codesi
fruits = ["Apple", "Banana", "Orange"]

har fruit mein fruits {
    likho("Fruit:", fruit)
}
```

#### 4. Break and Continue
```codesi
// Break example
har i se 1 tak 11 {
    agar (i == 5) {
        break
    }
    likho(i)
}

// Continue example
har i se 1 tak 11 {
    agar (i % 2 == 0) {
        continue  // Skip even numbers
    }
    likho(i)  // Only odd numbers
}
```

#### Practice Exercise
Create `day5_multiplication_table.cds`:
```codesi
// Multiplication Table
number = 7

likho("Multiplication Table of", number)
likho("========================")

har i se 1 tak 11 {
    result = number * i
    likho(number, "x", i, "=", result)
}
```

---

## 📅 Day 6: Functions

### Morning Session (45 mins)

#### 1. Basic Functions
```codesi
karya greet() {
    likho("Hello, World!")
}

greet()  // Call function
```

#### 2. Functions with Parameters
```codesi
karya greet_person(naam) {
    likho("Hello,", naam, "!")
}

greet_person("Rishaank")
greet_person("Priya")
```

### Afternoon Session (1 hour)

#### 3. Functions with Return
```codesi
karya add(a, b) {
    vapas a + b
}

result = add(5, 3)
likho("Sum:", result)

// Use in expressions
total = add(10, 20) + add(5, 5)
likho("Total:", total)  // 40
```

#### 4. Multiple Parameters
```codesi
karya calculate_area(length, width) {
    area = length * width
    vapas area
}

room_area = calculate_area(10, 12)
likho("Room area:", room_area, "sq ft")
```

#### Practice Exercise
Create `day6_functions_practice.cds`:
```codesi
// Function Practice

// 1. Function to check even/odd
karya is_even(num) {
    vapas num % 2 == 0
}

// 2. Function to calculate square
karya square(x) {
    vapas x * x
}

// 3. Function to find maximum
karya max_of_two(a, b) {
    agar (a > b) {
        vapas a
    } nahi_to {
        vapas b
    }
}

// Test functions
likho("Is 10 even?", is_even(10))
likho("Square of 7:", square(7))
likho("Max of 15 and 23:", max_of_two(15, 23))
```

---

## 📅 Day 7: Review and Project

### Morning Session (1 hour)

#### Review Concepts
1. Variables and data types
2. Operators (arithmetic, comparison, logical)
3. If-else statements
4. Loops (for, while, foreach)
5. Functions

### Afternoon Session (2 hours)

#### Final Project: Number Guessing Game

Create `week1_project_game.cds`:

```codesi
// Number Guessing Game - Week 1 Project

karya play_game() {
    likho("==========================")
    likho("  Number Guessing Game")
    likho("==========================")
    likho()
    
    // Generate random target (1 to 50)
    target = math_random(1, 50)
    attempts = 0
    max_attempts = 7
    
    likho("Maine 1 se 50 ke beech ek number socha hai!")
    likho("Aapko", max_attempts, "attempts hai.")
    likho()
    
    won = jhooth
    
    jabtak (attempts < max_attempts) {
        attempts = attempts + 1
        likho("Attempt", attempts, "of", max_attempts)
        guess = int_lo("Apna guess: ")
        
        agar (guess == target) {
            likho("🎉 Correct! Aapne jeet liya!")
            likho("Total attempts:", attempts)
            won = sach
            break
        } ya_phir (guess < target) {
            likho("❌ Too low! Try higher")
        } nahi_to {
            likho("❌ Too high! Try lower")
        }
        
        likho()
    }
    
    agar (nahi won) {
        likho("😞 Game Over!")
        likho("Sahi answer tha:", target)
    }
}

// Start game
play_game()

// Ask to play again
likho()
again = input_lo("Phir se khelna hai? (yes/no): ")
agar (again == "yes") {
    likho()
    play_game()
}

likho("\nDhanyavaad for playing! 🙏")
```

---

## 📊 Week 1 Checklist

Complete these to master basics:

### Concepts
- [ ] Understand variables
- [ ] Know all data types
- [ ] Use operators correctly
- [ ] Write if-else statements
- [ ] Create loops
- [ ] Define functions

### Skills
- [ ] Can write and run .cds files
- [ ] Can use REPL mode
- [ ] Can debug simple errors
- [ ] Can read and understand code
- [ ] Can write comments

### Projects
- [ ] Profile display program
- [ ] Simple calculator
- [ ] Grade calculator
- [ ] Multiplication table
- [ ] Number guessing game

---

## 💡 Tips for Success

### 1. Practice Daily
- Code for at least 30 minutes every day
- Type code yourself (don't copy-paste)
- Make mistakes and learn from them

### 2. Experiment
```codesi
// Try different values
x = 10
likho(x * 2)  // What happens?
likho(x * 3)  // How about this?
```

### 3. Use Comments
```codesi
// Always explain your code
naam = "Raj"  // Store user's name
```

### 4. Test Everything
```codesi
// Test edge cases
karya divide(a, b) {
    agar (b == 0) {
        likho("Cannot divide by zero!")
        vapas
    }
    vapas a / b
}
```

### 5. Ask Questions
- What does this do?
- Why did this happen?
- How can I improve this?

---

## 🎯 Practice Challenges

### Challenge 1: Temperature Converter
```codesi
// Convert Celsius to Fahrenheit
celsius = 25
fahrenheit = (celsius * 9 / 5) + 32
likho(celsius, "°C =", fahrenheit, "°F")
```

### Challenge 2: Leap Year Checker
```codesi
year = 2024

agar ((year % 4 == 0) aur ((year % 100 != 0) ya (year % 400 == 0))) {
    likho(year, "is a leap year")
} nahi_to {
    likho(year, "is not a leap year")
}
```

### Challenge 3: Prime Number Checker
```codesi
num = 17
is_prime = sach

agar (num <= 1) {
    is_prime = jhooth
} nahi_to {
    har i se 2 tak num {
        agar (num % i == 0) {
            is_prime = jhooth
            break
        }
    }
}

agar (is_prime) {
    likho(num, "is prime")
} nahi_to {
    likho(num, "is not prime")
}
```

---

## 🚀 Ready for Week 2?

Before moving to Intermediate level, ensure you can:

✅ Write programs with variables  
✅ Use all operators confidently  
✅ Create complex if-else chains  
✅ Use loops effectively  
✅ Define and call functions  
✅ Complete the Week 1 project  

**Congratulations on completing Week 1! 🎉**

---

**Next**: [Complete Intermediate Guide](COMPLETE_INTERMEDIATE.md)