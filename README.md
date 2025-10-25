# 🚀 Codesi Programming Language

<div align="center">

![Codesi Version](https://img.shields.io/badge/version-0.0.1-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Python](https://img.shields.io/badge/python-3.8+-yellow.svg)
![Status](https://img.shields.io/badge/status-production--ready-success.svg)

**The World's First Hinglish Programming Language with Revolutionary Features**

[Quick Start](#-quick-start) • [Documentation](#-documentation) • [Features](#-world-first-features) • [Examples](#-examples) • [Contributing](#-contributing)

---

</div>

## 🌟 What Makes Codesi Revolutionary?

Codesi isn't just another programming language—it's a **paradigm shift** in how we think about code. Created by a 15-year-old developer on a mobile phone, it introduces **multiple world-first features** that have never existed in any programming language before.

### 🎯 Core Innovation

- **🇮🇳 Hinglish Syntax**: First programming language with native Hindi-English hybrid syntax
- **🪄 JAADU Auto-Correction**: Intelligent, context-aware error correction built into the language itself
- **🧠 Self-Explaining Code**: No AI/ML needed—the language explains itself natively
- **⏰ Time Machine Debugger**: Travel through execution history, modify past states
- **📚 Smart History**: Complete execution timeline with state snapshots
- **💡 Personalized Hints**: Context-aware suggestions for common patterns

---

## 🚀 Quick Start

### Installation

#### 🪟 Windows Users (Recommended)

**Easiest Method - One-Click Installer:**

1. Go to [Releases](https://github.com/codesi-lang/codesi/releases)
2. Download the latest **Codesi Setup.exe**
3. Run the installer
4. Access Codesi from:
   - 🖥️ Desktop Icon
   - 📋 Start Menu
   - ⌨️ CMD/PowerShell (type `codesi`)

**If CMD access not working:**

Press `Win + R` and paste this command:

```powershell
powershell -NoProfile -Command "$add='C:\Program Files\Codesi'; $p=[Environment]::GetEnvironmentVariable('Path','User'); if(-not $p){ [Environment]::SetEnvironmentVariable('Path',$add,'User') } elseif($p -notlike '*'+$add+'*'){ [Environment]::SetEnvironmentVariable('Path',$p + ';' + $add,'User') }; Start-Process -FilePath 'RUNDLL32.EXE' -ArgumentList 'USER32.DLL,SendMessageA 0xFFFF,0x1A,0,`'Environment`'' -NoNewWindow"
```

Restart CMD and type `codesi` - it will work!

---

#### 🍎 macOS / 🐧 Linux Users

**Installer Coming Soon!** (In development)

For now, use Python installation:

```bash
# Install Python (if not installed)
# macOS: brew install python
# Linux: sudo apt install python3

# Install Codesi via pip
pip install codesi

# Access Codesi
codesi
```

---

#### 📱 Android Users (Termux)

```bash
# 1. Install Termux from Play Store or F-Droid
# 2. Open Termux and run:

apt update && apt upgrade -y
pkg install python
pip install codesi

# Access Codesi
codesi
```

---

#### 🌐 Need Help?

Visit our official website: **[https://thecodesi.xyz](https://thecodesi.xyz)**

Complete installation guides and troubleshooting available!

### Your First Program

Create `hello.cds`:

```codesi
likho("Hello, World!")
naam = sunao("Aapka naam kya hai? ")
likho("Namaste, " + naam + "!")
```

Run it:

```bash
codesi hello.cds
```

Or use interactive mode:

```bash
codesi
```

---

## 🌍 World-First Features

### 1️⃣ 🪄 JAADU - Auto-Correction System

**First programming language with built-in auto-correction**

```codesi
# You type (with typo):
linkho("Hello")  

# JAADU automatically corrects to:
🪄 JAADU: 'linkho' → 'likho'
```

Enable JAADU mode:
```bash
codesi --jaadu
```

### 2️⃣ ⏰ Time Machine Debugger

**First language with execution time travel**

```codesi
time_machine_on()  # Activate time travel

x = 5
likho(x)           # Prints: 5

x = 10
likho(x)           # Prints: 10

peeche()           # Go back in time!
likho(x)           # Prints: 5 (traveled back!)

aage()             # Go forward
timeline()         # See complete execution history
```

**Real-world use case:**
```codesi
time_machine_on()

arr = [1, 2, 3]
arr.push(4)
arr.push(5)
likho(arr)  // [1, 2, 3, 4, 5]

peeche(2)   // Go back 2 steps
likho(arr)  // [1, 2, 3] (before pushes!)
```

### 3️⃣ 🧠 Samjhao - Self-Explaining Code

**First language that explains itself without external AI**

```codesi
samjhao_on()  # Enable explanation mode

x = 10
y = 20
result = x + y
likho(result)

samjhao()  # Get detailed explanation
```

**Output:**
```
📖 Code Explanation:
============================================================
1. Variable 'x' mein value 10 store ki
2. Variable 'y' mein value 20 store ki
3. 🔢 Operation: 10 + 20 = 30
4. Variable 'result' mein value 30 store ki
============================================================
```

### 4️⃣ 🇮🇳 Hinglish Syntax

**First language designed for Indian developers**

```codesi
// Variables (English or Hindi)
naam = "Rishaank"
age = 15

// Conditions (Hinglish)
agar (age < 18) {
    likho("Aap minor ho")
} nahi_to {
    likho("Aap adult ho")
}

// Loops (Natural Hinglish)
har i se 1 tak 5 {
    likho("Number: " + i)
}

// Functions (Intuitive)
karya greet(naam) {
    vapas "Namaste, " + naam
}
```

---

## 💻 Complete Feature Set

### 📊 Data Types

```codesi
// Numbers
sankhya = 42
decimal = 3.14

// Strings
message = "Hello, Codesi!"

// Booleans
hai_sach = sach
hai_jhooth = jhooth

// Null
khaali_value = khaali

// Arrays
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", sach, [1, 2]]

// Objects
person = {
    naam: "Rishaank",
    age: 15,
    skills: ["Python", "Codesi"]
}
```

### 🔄 Control Flow

```codesi
// If-Elif-Else
agar (score > 90) {
    likho("A Grade")
} ya_phir (score > 75) {
    likho("B Grade")
} nahi_to {
    likho("C Grade")
}

// While Loop
jabtak (count < 10) {
    likho(count)
    count += 1
}

// Do-While
karo {
    likho("Executing...")
} jabtak (condition)

// For Loop (Range)
har i se 0 tak 10 {
    likho(i)
}

// For-Each
fruits = ["Apple", "Banana", "Mango"]
har fruit mein fruits {
    likho(fruit)
}

// Switch-Case
status ke case mein {
    200 -> likho("Success")
    404 -> likho("Not Found")
    500 -> likho("Server Error")
    default -> likho("Unknown")
}
```

### ⚡ Functions

```codesi
// Simple Function
karya add(a, b) {
    vapas a + b
}

// With Default Parameters
karya greet(naam = "Guest") {
    vapas "Hello, " + naam
}

// Variadic Functions
karya sum(...numbers) {
    total = 0
    har num mein numbers {
        total += num
    }
    vapas total
}

// Lambda Functions
square = lambda(x) -> x * x
result = square(5)  // 25
```

### 🏗️ Object-Oriented Programming

```codesi
// Class Definition
class Person {
    // Constructor
    banao(naam, age) {
        ye.naam = naam
        ye.age = age
    }
    
    // Methods
    karya introduce() {
        likho("Mera naam " + ye.naam + " hai")
        likho("Meri age " + ye.age + " saal hai")
    }
    
    // Static Methods
    static karya create_guest() {
        vapas new Person("Guest", 0)
    }
}

// Inheritance
class Student extends Person {
    banao(naam, age, grade) {
        super.banao(naam, age)
        ye.grade = grade
    }
    
    karya study() {
        likho(ye.naam + " is studying")
    }
}

// Usage
student = new Student("Rishaank", 15, 10)
student.introduce()
student.study()
```

### 📦 Array Methods

```codesi
arr = [1, 2, 3, 4, 5]

// Push/Pop
arr.push(6)          // [1, 2, 3, 4, 5, 6]
arr.pop()            // [1, 2, 3, 4, 5]

// Map
doubled = arr.map(lambda(x) -> x * 2)

// Filter
evens = arr.filter(lambda(x) -> x % 2 == 0)

// Reduce
sum = arr.reduce(lambda(a, b) -> a + b, 0)

// Others
arr.reverse()
arr.sort()
slice = arr.slice(1, 3)
```

### 📄 File Operations

```codesi
// Read File
content = file_padho("data.txt")

// Write File
file_likho("output.txt", "Hello World")

// Append
file_append("log.txt", "New entry\n")

// File Info
hai = file_hai("test.txt")
size = file_size("test.txt")

// Directory Operations
dir_banao("new_folder")
files = dir_list(".")
```

### 🛡️ Error Handling

```codesi
try {
    result = 10 / 0
} catch(error) {
    likho("Error: " + error.message)
} finally {
    likho("Cleanup code")
}

// Custom Errors
agar (age < 0) {
    throw {message: "Invalid age"}
}
```

---

## 🎓 Real-World Examples

### Example 1: Student Management System

```codesi
class Student {
    banao(naam, roll, marks) {
        ye.naam = naam
        ye.roll = roll
        ye.marks = marks
    }
    
    karya calculate_grade() {
        agar (ye.marks >= 90) {
            vapas "A+"
        } ya_phir (ye.marks >= 75) {
            vapas "A"
        } ya_phir (ye.marks >= 60) {
            vapas "B"
        } nahi_to {
            vapas "C"
        }
    }
    
    karya display() {
        likho("Student: " + ye.naam)
        likho("Roll: " + ye.roll)
        likho("Marks: " + ye.marks)
        likho("Grade: " + ye.calculate_grade())
    }
}

// Create students
s1 = new Student("Rishaank", 1, 95)
s2 = new Student("Raj", 2, 78)

// Display info
s1.display()
s2.display()
```

### Example 2: Time Machine Debugging

```codesi
time_machine_on()

// Buggy code - let's debug it
balance = 1000
likho("Initial: " + balance)

balance -= 200  // Withdrawal
likho("After withdrawal: " + balance)

balance -= 500  // Another withdrawal
likho("After 2nd withdrawal: " + balance)

balance -= 400  // ERROR: Insufficient balance!

// Go back and check
peeche(2)
likho("Checking balance: " + balance)  // 800

// See complete timeline
timeline()
```

### Example 3: File Processing with JAADU

```codesi
// JAADU will auto-correct typos
samjhao_on()  // Enable explanations

// Read file
data = file_padho("students.txt")
lines = data.todo("\n")

// Process each line
har line mein lines {
    parts = line.todo(",")
    naam = parts[0]
    marks = int_bnao(parts[1])
    
    agar (marks >= 75) {
        likho(naam + " passed!")
    }
}

// See what happened
samjhao()
```

---

## 🎮 Interactive REPL Mode

```bash
$ codesi
======================================================================
  🚀 Codesi Programming Language - Interactive Mode
  Version 1.0.0 | Hinglish Programming Language
======================================================================

📚 Commands:
  exit() or quit()      - Exit REPL
  help()               - Show help
  vars()               - Show all variables
  samjhao_on()         - Enable explanation mode
  time_machine_on()    - Enable time travel
  peeche() / aage()    - Time travel
  --jaadu flag         - Enable auto-correction

codesi:1> naam = "Rishaank"
codesi:2> likho("Hello, " + naam)
Hello, Rishaank
codesi:3> vars()

📊 Current Variables:
  naam = 'Rishaank'
```

---

## 🛠️ Built-in Functions

### Output Functions
```codesi
likho("Hello")           // Print output
```

### Input Functions
```codesi
naam = sunao("Name: ")          // String input
age = int_lo("Age: ")           // Integer input
score = float_lo("Score: ")     // Float input
```

### Math Functions
```codesi
math_absolute(-5)        // 5
math_square(16)          // 4
math_power(2, 3)         // 8
math_random(1, 10)       // Random number
math_gol(3.7)            // 4 (round)
```

### Type Functions
```codesi
type_of(value)           // Get type
string_bnao(123)         // "123"
int_bnao("456")          // 456
float_bnao("3.14")       // 3.14
bool_bnao(1)             // sach
```

### Array/String Functions
```codesi
lambai(arr)              // Length
range(1, 10)             // [1,2,3...9]
```

---

## 📚 Documentation

Comprehensive guides for all skill levels:

- **[Installation Guide](docs/INSTALLATION.md)** - Setup instructions
- **[Quickstart Guide](docs/QUICKSTART.md)** - Get started in 5 minutes
- **[Syntax Guide](docs/SYNTAX_GUIDE.md)** - Complete syntax reference
- **[Complete Basics](docs/COMPLETE_BASICS.md)** - Beginner tutorials
- **[Complete Intermediate](docs/COMPLETE_INTERMEDIATE.md)** - Advanced concepts
- **[Advanced Features](docs/ADVANCED_FEATURES.md)** - Time Machine, JAADU, Samjhao
- **[OOP Guide](docs/OOPs.md)** - Object-oriented programming
- **[Functions](docs/FUNCTIONS.md)** - Function reference
- **[Built-in Functions](docs/BUILTIN_FUNCTIONS.md)** - Standard library

---

## 🎯 Use Cases

### Perfect For:

✅ **Education** - Teaching programming in Hindi/Hinglish  
✅ **Rapid Prototyping** - Fast development with auto-correction  
✅ **Debugging** - Time Machine makes debugging trivial  
✅ **Learning** - Self-explaining code helps understanding  
✅ **Indian Developers** - Natural syntax for Hindi speakers  

---

## 🌟 Why Codesi?

| Feature | Traditional Languages | Codesi |
|---------|----------------------|---------|
| Language Barrier | English only | Hinglish (Hindi + English) |
| Error Correction | Manual debugging | Auto-correction (JAADU) |
| Code Understanding | External documentation | Self-explaining (Samjhao) |
| Time Travel Debugging | None | Built-in Time Machine |
| Learning Curve | Steep | Gentle with hints |
| Cultural Relevance | Western-centric | India-first design |

---

## 🤝 Contributing

We welcome contributions! Here's how:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing`)
3. **Commit** changes (`git commit -m 'Add amazing feature'`)
4. **Push** to branch (`git push origin feature/amazing`)
5. **Open** a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 📝 License

Codesi is open-source software licensed under the **MIT License**.

See [LICENSE](LICENSE) for details.

---

## 🙏 Credits

**Creator**: Rishaank Gupta  
**Development**: Entirely on mobile phone  
**Inspiration**: Making programming accessible to Everyone

### Special Thanks

- To all early testers and contributors
- The Python community for inspiration
- Everyone who believed in this vision

---

## 📞 Contact & Support

- **GitHub Issues**: [Report bugs or request features](https://github.com/codesi-lang/codesi/issues)
- **Discussions**: [Join the community](https://discord.gg/codesilang)
- **Email**: [codesilang@gmail.com](mailto:codesilang@gmail.com)

---

## 🗺️ Roadmap

### Version 0.0.1
- ✅ Core language features
- ✅ Time Machine debugger
- ✅ JAADU auto-correction
- ✅ Samjhao self-explanation
- ✅ OOP support

---

## 📊 Statistics

- **Lines of Code**: 2000+
- **Features**: 50+ unique features
- **World Firsts**: 4 major innovations
- **Development Time**: 6+ months
- **Platform**: Pure Python (3.8+)

---

## 💡 Fun Facts

- 🎓 Created by a 10th grade student
- 📱 Entirely developed on a mobile phone
- 🇮🇳 First Hinglish programming language
- ⏰ First language with time-travel debugging
- 🪄 First with built-in auto-correction
- 🧠 First self-explaining language (no AI needed)

---

<div align="center">

**Made with ❤️ in India**

[![GitHub stars](https://img.shields.io/github/stars/codesi-lang/Codesi?style=social)](https://github.com/codesi-lang/codesi/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/codesi-lang/Codesi?style=social)](https://github.com/codesi-lang/codesi/network/members)

[⬆ Back to Top](#-codesi-programming-language)

</div>
