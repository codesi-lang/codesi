# Quick Start Guide

Get started with Codesi in 5 minutes! 🚀

## 📋 Prerequisites

- Codesi installed ([Installation Guide](INSTALLATION.md))

---

## 🎯 Your First Program

### Step 1: Create a File

Create `hello.cds`:
```codesi
likho("Namaste Duniya!")
```

### Step 2: Run It

```bash
codesi hello.cds
```

**Output:**
```
Namaste Duniya!
```

**Congratulations! You just ran your first Codesi program!** 🎉

---

## 💬 Interactive Mode (REPL)

Start the REPL:
```bash
codesi
```

Try these:
```codesi
codesi:1> likho("Hello")
Hello

codesi:2> naam = "Rishaank"
codesi:3> likho("Mera naam", naam, "hai")
Mera naam Rishaank hai

codesi:4> x = 10
codesi:5> y = 20
codesi:6> likho(x + y)
30

codesi:7> exit()
```

---

## 📚 Basic Concepts

### Variables

```codesi
// Simple assignment
naam = "Raj"
umra = 25
height = 5.8

// Output
likho(naam, umra, height)
```

### Math Operations

```codesi
a = 10
b = 3

likho("Sum:", a + b)        // 13
likho("Difference:", a - b) // 7
likho("Product:", a * b)    // 30
likho("Division:", a / b)   // 3.333...
likho("Modulo:", a % b)     // 1
likho("Power:", a ** b)     // 1000
```

### If-Else Conditions

```codesi
umra = 20

agar (umra >= 18) {
    likho("Adult ho")
} nahi_to {
    likho("Minor ho")
}
```

### Multiple Conditions

```codesi
marks = 85

agar (marks >= 90) {
    likho("A+ Grade")
} ya_phir (marks >= 80) {
    likho("A Grade")
} ya_phir (marks >= 70) {
    likho("B Grade")
} nahi_to {
    likho("C Grade")
}
```

### Loops

```codesi
// For loop - basic syntax
har i se 1 tak 6 {
    likho("Number:", i)
}

// For loop - with parentheses
har i ke liye (0 se 5 tak) {
    likho(i)
}

// While loop
count = 0
jabtak (count < 5) {
    likho(count)
    count = count + 1
}

// ForEach loop
fruits = ["Apple", "Banana", "Orange"]
har fruit mein fruits {
    likho("Fruit:", fruit)
}
```

### Functions

```codesi
// Simple function
karya greet(naam) {
    likho("Hello", naam, "!")
}

greet("Rishaank")

// Function with return
karya add(a, b) {
    vapas a + b
}

result = add(5, 3)
likho("Sum:", result)  // 8
```

### Arrays

```codesi
// Create array
numbers = [1, 2, 3, 4, 5]

// Access elements
likho(numbers[0])  // 1
likho(numbers[2])  // 3

// Modify
numbers[1] = 10
likho(numbers)  // [1, 10, 3, 4, 5]

// Array methods
numbers.push(6)
likho(numbers)  // [1, 10, 3, 4, 5, 6]

last = numbers.pop()
likho(last)  // 6
```

### Objects

```codesi
// Create object
person = {
    naam: "Raj",
    umra: 25,
    city: "Mumbai"
}

// Access properties
likho(person.naam)     // Raj
likho(person["umra"])  // 25

// Modify
person.umra = 26
person.job = "Developer"
```

---

## 🎮 Try These Examples

### 1. Temperature Converter

```codesi
karya celsius_to_fahrenheit(c) {
    vapas (c * 9 / 5) + 32
}

celsius = float_lo("Temperature in Celsius: ")
fahrenheit = celsius_to_fahrenheit(celsius)
likho(celsius, "°C =", fahrenheit, "°F")
```

### 2. Even/Odd Checker

```codesi
num = int_lo("Enter a number: ")

agar (num % 2 == 0) {
    likho(num, "is Even")
} nahi_to {
    likho(num, "is Odd")
}
```

### 3. Sum of Array

```codesi
numbers = [10, 20, 30, 40, 50]
total = 0

har num mein numbers {
    total = total + num
}

likho("Sum:", total)  // 150
```

### 4. Count Vowels

```codesi
karya count_vowels(text) {
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    
    har char mein text {
        agar (char mein vowels) {
            count = count + 1
        }
    }
    
    vapas count
}

word = input_lo("Enter a word: ")
result = count_vowels(word.chota_karo())
likho("Vowels:", result)
```

---

## 🪄 Special Features

### JAADU Context-Aware Auto-Correction

Enable smart typo fixing with revolutionary features:

```bash
# Run with JAADU mode
codesi script.cds --jaadu
```

Now if you write:
```codesi
liko("Hello")  // Typo: liko
```

JAADU automatically fixes it to `likho()`!

**What makes JAADU special:**
- ✨ Context-aware: Methods vs Functions vs Keywords
- ✨ Phonetic matching: `leekho` → `likho`
- ✨ Method chains: `arr.mep().filtr()` → `arr.map().filter()`
- ✨ Case insensitive: `LIKO` → `likho`
- ✨ Dual language: Hindi + English method aliases
- ✨ Corrects up to 3-4 character differences

**More examples:**
```codesi
arr.pus(4)         // Method typo → arr.push(4)
leekho("Test")     // Phonetic → likho("Test")
arr.dlo(1)         // Hindi → arr.dalo(1) → arr.push(1)
```

### Samjho (Explain Mode)

Understand your code execution:

```codesi
samjhao_on()  // Enable explanation

x = 10
y = 20
sum = x + y

samjhao()  // View explanations
```

**Output:**
```
📖 Code Explanation:
============================================================
1. Variable 'x' mein value 10 store ki
2. Variable 'y' mein value 20 store ki
3. 🔢 Operation: 10 + 20 = 30
4. Variable 'sum' mein value 30 store ki
============================================================
```

### Time Machine Debugger

Travel through execution history:

```codesi
time_machine_on()  // Activate

x = 5
x = x * 2
x = x + 3

// In REPL, use:
// peeche()   - Go back
// aage()     - Go forward
// timeline() - See history
```

---

## 🎯 Common Patterns

### User Input

```codesi
// String input
naam = input_lo("Aapka naam: ")

// Integer input
umra = int_lo("Aapki umra: ")

// Float input
height = float_lo("Height in cm: ")
```

### String Operations

```codesi
text = "Hello World"

likho(text.lambai())           // 11
likho(text.bada_karo())        // HELLO WORLD
likho(text.chota_karo())       // hello world
likho(text.todo(" "))          // ["Hello", "World"]
likho(text.badlo("World", "Codesi"))  // Hello Codesi
```

### Error Handling

```codesi
try {
    result = 10 / 0
} catch (e) {
    likho("Error:", e.message)
} finally {
    likho("Program complete")
}
```

### File Operations

```codesi
// Write to file
file_likho("data.txt", "Hello Codesi!")

// Read from file
content = file_padho("data.txt")
likho(content)

// Append to file
file_append("data.txt", "\nNew line")
```

---

## 🎓 Learning Path

### Beginner (Week 1)
1. ✅ Variables and data types
2. ✅ Basic operators
3. ✅ If-else statements
4. ✅ Simple loops
5. ✅ Functions

**Practice**: Build a calculator

### Intermediate (Week 2)
1. ✅ Arrays and array methods
2. ✅ Objects
3. ✅ String manipulation
4. ✅ File I/O
5. ✅ Error handling

**Practice**: Build a todo list

### Advanced (Week 3)
1. ✅ Classes and OOP
2. ✅ Inheritance
3. ✅ Lambda functions
4. ✅ Advanced loops
5. ✅ Switch-case

**Practice**: Build a student management system

---

## 📖 Next Steps

Now that you know the basics:

1. **Run Examples**: Try all files in `examples/` folder
2. **Read Docs**: 
   - [Complete Syntax Guide](SYNTAX_GUIDE.md)
   - [Built-in Functions](BUILTIN_FUNCTIONS.md)
   - [Data Types](DATA_TYPES.md)
3. **Build Projects**: Start with small programs
4. **Join Community**: Share your creations!

---

## 💡 Pro Tips

### REPL Commands
```
help()                       // Show this help
qhelp()                      // Show quick reference
license()                    // Show license info
copyright()                  // Show copyright info
credits()                    // Show credits & thanks
exit() or quit()             // Exit REPL
clear()                      // Clear screen
vars()                       // Show all variables
history()                    // Show command history
!!                           // Repeat last command
!5                           // Repeat command #5 from history
```

### Debugging
```codesi
// Use samjhao for step-by-step
samjhao_on()

// Use time machine for history
time_machine_on()

// Print debugging
likho("Debug: x =", x)
```

### Code Style
```codesi
// Good: Descriptive names
student_marks = 85

// Bad: Single letters
m = 85

// Good: Comments
// Calculate average marks
avg = total / count

// Good: Spacing
x = 10 + 20
```

---

## 🐛 Common Mistakes

### 1. Forgetting Parentheses
```codesi
// ❌ Wrong
agar x > 5 {
    likho("Big")
}

// ✅ Correct
agar (x > 5) {
    likho("Big")
}
```

### 2. Using = instead of ==
```codesi
// ❌ Wrong (assignment)
agar (x = 5) {
    // ...
}

// ✅ Correct (comparison)
agar (x == 5) {
    // ...
}
```

### 3. Division by Zero
```codesi
// ✅ Always check
agar (b != 0) {
    result = a / b
} nahi_to {
    likho("Cannot divide by zero")
}
```

---

## 🎉 Congratulations!

You now know enough to start building real programs in Codesi!

**Quick Challenge**: Build a program that:
1. Takes user's name and age
2. Calculates birth year
3. Tells if they can vote (18+)
4. Saves result to a file

---

## 📞 Need Help?

- **Documentation**: Check `docs/` folder
- **Examples**: See `examples/` folder
- **Issues**: [GitHub Issues](https://github.com/codesi-lang/codesi/issues)
- **Community**: GitHub Discussions

---

**Happy Coding in Hinglish! 🚀**

Next: [Complete Basics Guide](COMPLETE_BASICS.md)