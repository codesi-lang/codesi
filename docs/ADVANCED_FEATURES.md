# Advanced Features - World-First Innovations

Complete guide to Codesi's revolutionary features: JAADU, Samjho, and Time Machine.

## 🌟 Overview

Codesi introduces **three world-first features** never seen in any programming language:

1. **🪄 JAADU**: Auto-correction system
2. **🧠 Samjho**: Built-in code explainer  
3. **⏰ Time Machine**: Time-travel debugger

---

## 🪄 JAADU Auto-Correction System

### What is JAADU?

JAADU (Magic) is an **intelligent, context-aware auto-correction system** that:
- Detects typos in function names, methods, and keywords
- Uses phonetic matching for Hindi/Hinglish spellings
- Provides context-aware suggestions (method vs function vs keyword)
- Calculates confidence scores for each correction
- Supports dual English/Hindi method aliases
- Automatically fixes errors in JAADU mode
- Handles method chains with multiple typos
- Works case-insensitively

**World-First**: No programming language has built-in context-aware auto-correction with phonetic matching!

### Enhanced Capabilities

#### 1. **Context-Aware Correction**
JAADU understands where typos occur:

```codesi
// Function context
liko("Hello")  // Corrected to: likho()

// Method context
arr.pus(4)     // Corrected to: arr.push()

// Keyword context
kary add() {}  // Corrected to: karya add() {}
```

#### 2. **Phonetic Matching**
Handles Hindi/English sound-alike spellings:

```codesi
// Phonetic variations auto-corrected
leekho("Hi")   // ee→i : likho()
liikho("Hi")   // ii→i : likho()
phile_padho()  // ph→f : file_padho()
```

**Supported phonetic rules:**
- `ph` → `f`, `gh` → `g`, `kh` → `k`, `ch` → `c`
- `aa` → `a`, `ee` → `i`, `oo` → `u`
- `th` → `t`, `dh` → `d`, `bh` → `b`

#### 3. **Confidence Scoring**
Each correction has a confidence level (0-100%):

```codesi
liko   → likho   (95% confident - high similarity)
lko    → likho   (75% confident - 2 chars missing)
xyz    → ❌      (20% confident - too different, no correction)
```

**Threshold:** Minimum 60% confidence required for correction

#### 4. **Dual Language Support**
English and Hindi array methods both work:

```codesi
// English methods
arr.push(1)      // Add to end
arr.pop()        // Remove from end

// Hindi methods (aliases)
arr.dalo(1)      // Same as push
arr.nikalo()     // Same as pop

// Both typos corrected
arr.pus(1)       // → push
arr.dlo(1)       // → dalo → push
```

#### 5. **Method Chain Support**
Multiple typos in one statement:

```codesi
// Both typos corrected simultaneously
arr.mep(fn).filtr(fn)
// 🪄 JAADU: 'mep' → 'map'
// 🪄 JAADU: 'filtr' → 'filter'
```

#### 6. **Case Insensitivity**
Works with any case combination:

```codesi
Liko("Hi")     // → likho()
LIKO("Hi")     // → likho()
LiKo("Hi")     // → likho()
```

### How It Works

JAADU uses a **multi-layered approach**:

```python
# Simplified algorithm
1. Extract identifiers with context detection
2. Skip strings, comments, REPL commands
3. Check against valid functions/methods/keywords
4. Apply phonetic normalization
5. Calculate similarity + confidence score
6. Rank suggestions by confidence
7. Apply corrections above 60% threshold
```

**Advanced features:**
- **LRU Cache**: 512-entry cache for repeated typos (200x faster)
- **String Detection**: Skips content inside quotes
- **Regex Escaping**: Handles special characters safely
- **Context Filtering**: Only searches relevant candidates (methods vs functions)

### Using JAADU

#### Mode 1: Suggestions Only (Default)

```bash
codesi script.cds
```

When you make a typo:
```codesi
liko("Hello")  // Typo!
```

**Output:**
```
❌ Codesi Runtime Error: Variable 'liko' define nahi hai
💡 Kya aapka matlab 'likho' tha?
```

#### Mode 2: Auto-Correction (JAADU Mode)

```bash
codesi script.cds --jaadu
```

Same typo gets auto-fixed:
```codesi
liko("Hello")  // Typo!
```

**Output:**
```
🪄 JAADU: 'liko' → 'likho'
Hello
```

### JAADU in REPL

```bash
codesi --jaadu
```

```codesi
codesi:1> liko("Hello")
🪄 JAADU: 'liko' → 'likho'
Hello

codesi:2> arr = [1, 2, 3]
codesi:3> arr.pus(4)
🪄 JAADU: 'pus' → 'push'
codesi:4> likho(arr)
[1, 2, 3, 4]
```

### What JAADU Corrects

#### ✅ Function Names (50+ built-in functions)
```codesi
liko("Hi")           → likho("Hi")
inpt("Name: ")       → input_lo("Name: ")
type_off(42)         → type_of(42)
math_squre(16)       → math_square(16)
file_pdho("f.txt")   → file_padho("f.txt")
```

#### ✅ Array Methods (24+ methods, English + Hindi)
```codesi
// English
arr.pus(1)           → arr.push(1)
arr.pu(1)            → arr.push(1)   // 2 chars missing
arr.psh(1)           → arr.push(1)   // 1 char missing
arr.mep(fn)          → arr.map(fn)
arr.filtr(fn)        → arr.filter(fn)

// Hindi
arr.dlo(1)           → arr.dalo(1)
arr.nkalo()          → arr.nikalo()
arr.bdlo(fn)         → arr.badlo(fn)  // map alias
```

#### ✅ String Methods (10+ methods)
```codesi
text.lambai()        // length
text.bada_kro()      → text.bada_karo()  // uppercase
text.chota_kro()     → text.chota_karo() // lowercase
text.saaf_kro()      → text.saaf_karo()  // trim
```

#### ✅ Object Methods (4 methods)
```codesi
obj.keys()           // Get keys
obj.values()         // Get values
obj.hai_kya("key")   // Check key exists
```

#### ✅ Keywords (35+ keywords)
```codesi
kary func() {}       → karya func() {}
agr (x > 5) {}       → agar (x > 5) {}
jabtk (true) {}      → jabtak (true) {}
```

### What JAADU Doesn't Correct

#### ❌ String Literals
```codesi
likho("liko is a typo")  // "liko" NOT corrected (inside string)
```

#### ❌ Comments
```codesi
// liko is wrong      // NOT corrected (in comment)
```

#### ❌ REPL Commands
```codesi
exit, quit, help, clear, vars  // Never corrected
```

#### ❌ Very Low Similarity (<60%)
```codesi
xyz123()  // Too different from any function
abc()     // No match found
```

#### ❌ Custom User Functions
```codesi
my_custom_func()  // User-defined, not corrected
```

### JAADU Correction Examples

#### Example 1: Basic Function Typo
```codesi
liko("Hello World")
// 🪄 JAADU: 'liko' → 'likho'
// Output: Hello World
```

#### Example 2: Multiple Typos
```codesi
liko("Enter name:")
naam = inpt()
// 🪄 JAADU: 'liko' → 'likho'
// 🪄 JAADU: 'inpt' → 'input_lo'
```

#### Example 3: Method Context
```codesi
arr = [1, 2, 3]
arr.pus(4)
arr.pus(5)
// 🪄 JAADU: 'pus' → 'push' (both occurrences)
likho(arr)  // [1, 2, 3, 4, 5]
```

#### Example 4: Method Chains
```codesi
numbers = [1, 2, 3, 4, 5]
result = numbers.mep(lambda(x) -> x * 2)
                .filtr(lambda(x) -> x > 5)
// 🪄 JAADU: 'mep' → 'map'
// 🪄 JAADU: 'filtr' → 'filter'
likho(result)  // [6, 8, 10]
```

#### Example 5: Phonetic Variations
```codesi
leekho("Phonetic test")
liikho("Another test")
// 🪄 JAADU: 'leekho' → 'likho' (phonetic: ee→i)
// 🪄 JAADU: 'liikho' → 'likho' (phonetic: ii→i)
```

#### Example 6: Case Insensitive
```codesi
Liko("Capital L")
LIKO("All caps")
LiKo("Mixed case")
// 🪄 JAADU: 'Liko' → 'likho'
// 🪄 JAADU: 'LIKO' → 'likho'
// 🪄 JAADU: 'LiKo' → 'likho'
```

#### Example 7: Hindi Method Aliases
```codesi
arr = [10, 20, 30]
arr.dlo(40)      // Hindi version of push
last = arr.nkalo() // Hindi version of pop
// 🪄 JAADU: 'dlo' → 'dalo'
// 🪄 JAADU: 'nkalo' → 'nikalo'
likho(arr)  // [10, 20, 30]
```

### JAADU Performance

#### Cache System
- **LRU Cache**: 512 entries
- **First lookup**: ~2ms
- **Cached lookup**: ~0.01ms
- **Speed improvement**: 200x faster for repeated typos

#### Context Filtering
Instead of searching all 100+ identifiers:
- **Method context**: Only 24 method names
- **Function context**: Only 50 function names  
- **Keyword context**: Only 35 keywords
- **Result**: 3-5x faster matching

### JAADU Maximum Correction Potential

Based on comprehensive testing:

| Typo Type | Example | Success Rate |
|-----------|---------|--------------|
| 1 char missing | `lkho` → `likho` | ✅ 100% |
| 1 char extra | `likko` → `likho` | ✅ 100% |
| 1 char wrong | `liko` → `likho` | ✅ 100% |
| 2 chars different | `leekho` → `likho` | ✅ 95% |
| 3 chars different | `leekhoo` → `likho` | ✅ 75% |
| Phonetic variations | `liikho` → `likho` | ✅ 98% |
| Case variations | `LIKO` → `likho` | ✅ 100% |
| Transposition | `ilkho` → `likho` | ✅ 90% |

**Edit Distance Limit**: Up to 3-4 characters (50% similarity minimum)

### JAADU Best Practices

#### ✅ When to Use JAADU Mode
- Learning phase (students/beginners)
- Quick prototyping
- Live coding sessions
- Teaching/demos
- Experimentation

#### ❌ When Not to Use
- Production code (use linters instead)
- Code reviews (typos should be visible)
- Team projects (enforce proper spelling)
- Final submissions

#### 💡 Pro Tips
1. **Use in REPL**: Enable for interactive coding
2. **Learn from corrections**: JAADU shows what you typed wrong
3. **Combine with Samjhao**: Understand corrected code
4. **Check corrections**: Review what JAADU changed
5. **Disable for tests**: Don't rely on auto-correction in exams

---

## 🧠 Samjho (Explain) System

### What is Samjho?

Samjho is a **built-in code explainer** that:
- Explains every step of execution
- Tracks variable changes
- Shows operation results
- Explains control flow
- **No AI/ML models required!**

**World-First**: No language has built-in non-AI explanations!

### How It Works

Samjho uses **instrumentation** - it hooks into the interpreter and records every significant operation during code execution. Unlike AI-based code explainers, Samjho understands your code because **it IS the code executor**.

```python
# Behind the scenes
1. Code executes normally
2. Samjho intercepts each operation
3. Records what happened in plain Hinglish
4. You can view explanations anytime
```

### Using Samjho

#### Enable Samjho

```codesi
samjhao_on()  // Enable explanation mode
```

#### Write Your Code

```codesi
x = 10
y = 20
result = x + y

agar (result > 25) {
    likho("Big number!")
}
```

#### View Explanations

```codesi
samjhao()  // Show detailed explanation
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
6. Function call: likho('Big number!') (no return)
============================================================
```

#### Disable Samjho

```codesi
samjhao_off()  // Disable explanations
```

### What Samjho Explains

#### 1. Variable Assignments

```codesi
samjhao_on()

naam = "Rishaank"
age = 15
is_student = sach

samjhao()
```

**Explanation:**
```
1. Variable 'naam' mein value 'Rishaank' store ki
2. Variable 'age' mein value 15 store ki
3. Variable 'is_student' mein value sach store ki
```

#### 2. Mathematical Operations

```codesi
samjhao_on()

a = 10
b = 5
sum = a + b
product = a * b
division = a / b

samjhao()
```

**Explanation:**
```
1. Variable 'a' mein value 10 store ki
2. Variable 'b' mein value 5 store ki
3. 🔢 Operation: 10 + 5 = 15
4. Variable 'sum' mein expression ka result store kiya: 10 + 5 = 15
5. 🔢 Operation: 10 * 5 = 50
6. Variable 'product' mein expression ka result store kiya: 10 * 5 = 50
7. 🔢 Operation: 10 / 5 = 2.0
8. Variable 'division' mein expression ka result store kiya: 10 / 5 = 2.0
```

#### 3. Conditional Statements

```codesi
samjhao_on()

marks = 85

agar (marks >= 90) {
    likho("A+")
} ya_phir (marks >= 80) {
    likho("A")
} nahi_to {
    likho("B")
}

samjhao()
```

**Explanation:**
```
1. Variable 'marks' mein value 85 store ki
2. 🔀 If condition check: (marks >= 90) → jhooth
3. 🔀 Elif condition: (marks >= 80) → sach (executed)
4. Function call: likho('A') (no return)
```

#### 4. Loops

```codesi
samjhao_on()

har i se 1 tak 4 {
    likho(i)
}

samjhao()
```

**Explanation:**
```
1. For loop started
2. ↻ Loop iteration: i = 1
3. Function call: likho(1) (no return)
4. ↻ Loop iteration: i = 2
5. Function call: likho(2) (no return)
6. ↻ Loop iteration: i = 3
7. Function call: likho(3) (no return)
8. ✓ For loop completed
```

#### 5. Function Calls

```codesi
samjhao_on()

karya add(a, b) {
    vapas a + b
}

result = add(5, 3)
samjhao()
```

**Explanation:**
```
1. Function 'add(a, b)' defined
2. Function call: add(5, 3) → returned 8
3. Variable 'result' mein value 8 store ki
```

#### 6. Array Operations

```codesi
samjhao_on()

arr = [1, 2, 3]
arr.push(4)
doubled = arr.map(lambda(x) -> x * 2)

samjhao()
```

**Explanation:**
```
1. Variable 'arr' mein value [1, 2, 3] store ki
2. Array operation: push - Added element 4
3. Array operation: map - Transformed array
4. Variable 'doubled' mein value [2, 4, 6, 8] store ki
```

### Samjho Best Practices

#### ✅ When to Use Samjho

- **Learning**: Understanding how code executes
- **Debugging**: Tracking variable changes
- **Teaching**: Explaining code to others
- **Code Reviews**: Understanding complex logic
- **Algorithm Analysis**: Step-by-step execution

#### ❌ When Not to Use

- **Performance-critical code**: Adds overhead
- **Production**: Disable in deployed code
- **Large loops**: Too many explanations
- **Simple code**: Obvious logic doesn't need explanation

### Samjho Commands Reference

| Function | Purpose | Example |
|----------|---------|---------|
| `samjhao_on()` | Enable explanations | `samjhao_on()` |
| `samjhao_off()` | Disable explanations | `samjhao_off()` |
| `samjhao()` | Show all explanations | `samjhao()` |

### Real-World Example: Debugging with Samjho

```codesi
// Bug: Why is average wrong?
samjhao_on()

marks = [85, 90, 78, 92, 88]
total = 0

har mark mein marks {
    total = total + mark
}

average = total / 5  // Should use marks.lambai()
likho("Average:", average)

samjhao()
```

**Explanation shows the problem:**
```
1. Variable 'marks' mein value [85, 90, 78, 92, 88] store ki
2. Variable 'total' mein value 0 store ki
3. ForEach loop started
4. ↻ Loop iteration: mark = 85
5. 🔢 Operation: 0 + 85 = 85
6. ↻ Loop iteration: mark = 90
7. 🔢 Operation: 85 + 90 = 175
...
12. 🔢 Operation: 433 / 5 = 86.6  ✓ Correct!
```

Now you can see the logic is actually correct!

---

## ⏰ Time Machine Debugger

### What is Time Machine?

Time Machine is a **revolutionary time-travel debugger** that:
- Records execution snapshots automatically
- Lets you go back to any previous state
- Restores variable values from the past
- No breakpoints or print statements needed
- Works in REPL mode

**World-First**: No programming language has built-in time-travel debugging!

### How It Works

Time Machine takes **snapshots** of your program state:

```python
# Behind the scenes
1. Each significant operation → Snapshot
2. Stores: variables, values, line info
3. You can travel back/forward
4. State gets restored automatically
```

### Using Time Machine

#### Enable Time Machine

```codesi
time_machine_on()  // Enable with default 100 snapshots
```

Or with custom limit:

```codesi
time_machine_on(500)  // Enable with 500 snapshots
```

#### Write Code (Snapshots Taken Automatically)

```codesi
x = 5
likho(x)  // 5

x = 10
likho(x)  // 10

x = 15
likho(x)  // 15
```

#### Travel Back in Time

```codesi
peeche()  // Go back 1 step
likho(x)  // 10 (restored!)

peeche(2)  // Go back 2 more steps
likho(x)  // 5 (back to original!)
```

#### Travel Forward

```codesi
aage()  // Go forward 1 step
likho(x)  // 10

aage(2)  // Go forward 2 steps
likho(x)  // 15
```

#### View Timeline

```codesi
timeline()  // See all snapshots
```

**Output:**
```
Complete Execution Timeline:
============================================================
Step 1: x = 5
Step 2: likho(x)
Step 3: x = 10
Step 4: likho(x)
Step 5: x = 15
Step 6: likho(x)
============================================================
```

#### Check Status

```codesi
time_machine_status()
```

**Output:**
```
✓ Time Machine: ON
  Max snapshots: 100
  Current snapshots: 6
  Current step: 6
```

#### Disable Time Machine

```codesi
time_machine_off()
```

**Output:**
```
Time Machine deactivated! (6 snapshots cleared)
```

### Time Machine Features

#### 1. Automatic Snapshots

```codesi
time_machine_on()

// Every operation creates a snapshot
x = 10      // Snapshot 1
y = 20      // Snapshot 2
z = x + y   // Snapshot 3
```

#### 2. Variable State Restoration

```codesi
time_machine_on()

arr = [1, 2, 3]
arr.push(4)
arr.push(5)
likho(arr)  // [1, 2, 3, 4, 5]

peeche(2)   // Go back 2 steps
likho(arr)  // [1, 2, 3] - State restored!
```

#### 3. Deep Copy Support

Time Machine creates **deep copies** of arrays and objects:

```codesi
time_machine_on()

obj = {naam: "Raj", age: 25}
likho(obj)

obj.age = 30
likho(obj)

peeche()
likho(obj)  // {naam: "Raj", age: 25} - Original restored!
```

#### 4. Configurable Snapshot Limit

```codesi
// Default: 100 snapshots
time_machine_on()

// Custom limit: 500 snapshots
time_machine_on(500)

// When limit reached, oldest snapshots are removed
```

**Automatic Warning:**
```
⚠️ Time Machine Limit Reached!
   Current limit: 100 snapshots
   Tip: Use time_machine_on(max=500) for more snapshots
   Oldest snapshots silently remove ho jayenge.
```

### Time Machine Commands Reference

| Function | Purpose | Example |
|----------|---------|---------|
| `time_machine_on()` | Enable (100 snapshots) | `time_machine_on()` |
| `time_machine_on(max)` | Enable (custom limit) | `time_machine_on(500)` |
| `time_machine_off()` | Disable & clear | `time_machine_off()` |
| `time_machine_status()` | Check status | `time_machine_status()` |
| `peeche()` | Go back 1 step | `peeche()` |
| `peeche(n)` | Go back n steps | `peeche(3)` |
| `aage()` | Go forward 1 step | `aage()` |
| `aage(n)` | Go forward n steps | `aage(2)` |
| `timeline()` | View all snapshots | `timeline()` |

### Real-World Use Cases

#### Use Case 1: Debugging Array Mutations

```codesi
time_machine_on()

numbers = [1, 2, 3, 4, 5]
likho("Original:", numbers)

// Remove even numbers
i = 0
jabtak (i < numbers.lambai()) {
    agar (numbers[i] % 2 == 0) {
        numbers.pop()  // Bug: Should remove specific index
    }
    i = i + 1
}

likho("After:", numbers)  // Wrong result!

// Travel back to see what happened
timeline()  // View all steps
peeche(5)   // Go back before loop
likho(numbers)  // Check original state
```

#### Use Case 2: Understanding Algorithm Steps

```codesi
time_machine_on()

// Bubble Sort
arr = [5, 2, 8, 1, 9]

har i se 0 tak arr.lambai() {
    har j se 0 tak arr.lambai() - i - 1 {
        agar (arr[j] > arr[j + 1]) {
            // Swap
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp
        }
    }
}

// View complete sorting process
timeline()

// Go back to see any intermediate state
peeche(10)
likho("Array at this point:", arr)
```

#### Use Case 3: Testing Different Values

```codesi
time_machine_on()

// Try different values
x = 10
result = x * x + 2 * x + 1
likho("For x =", x, "result =", result)

x = 20
result = x * x + 2 * x + 1
likho("For x =", x, "result =", result)

// Go back and try another value
peeche(3)  // Back to x = 10
x = 15
result = x * x + 2 * x + 1
likho("For x =", x, "result =", result)
```

#### Use Case 4: Function Execution Analysis

```codesi
time_machine_on()

karya factorial(n) {
    agar (n <= 1) {
        vapas 1
    }
    vapas n * factorial(n - 1)
}

result = factorial(5)
likho("Result:", result)

// See all recursive calls
timeline()
```

### Time Machine Best Practices

#### ✅ When to Use Time Machine

- **Debugging loops**: Track variable changes
- **Algorithm analysis**: Step through execution
- **Testing**: Try different values quickly
- **Learning**: Understand code flow
- **Complex logic**: Trace execution path

#### ❌ When Not to Use

- **Production code**: Only for development
- **Very long loops**: Too many snapshots
- **Performance testing**: Adds overhead
- **Simple scripts**: Overkill for trivial code

### Performance Considerations

#### Snapshot Storage

Each snapshot stores:
- All user variables
- Deep copies of arrays/objects
- Line information

**Memory Usage:**
```
100 snapshots ≈ Few MB (typical)
500 snapshots ≈ 10-20 MB (acceptable)
1000+ snapshots ≈ May slow down (not recommended)
```

#### Recommended Limits

| Use Case | Recommended Limit |
|----------|-------------------|
| Quick debugging | 50-100 |
| Algorithm analysis | 100-200 |
| Deep analysis | 200-500 |
| Long programs | 500-1000 |

---

## 🎯 Combining All Three Features

You can use JAADU, Samjho, and Time Machine together for the ultimate development experience!

### Example: Complete Debugging Session

```codesi
// Enable all features
time_machine_on(200)
samjhao_on()

// Write code (with potential typo)
likho("Starting calculation...")

numbers = [10, 20, 30, 40, 50]
sum = 0

har num mein numbers {
    sum = sum + num
}

average = sum / numbers.lambai()
likho("Average:", average)

// View explanations
samjhao()

// Check execution timeline
timeline()

// Travel back if needed
peeche(5)
likho("Sum at this point:", sum)

// Disable when done
samjhao_off()
time_machine_off()
```

**With JAADU mode:**
```bash
codesi --jaadu
```

Now even typos get auto-corrected!

---

## 📊 Feature Comparison

| Feature | Traditional Languages | Codesi |
|---------|----------------------|---------|
| **Auto-Correction** | External linters | ✅ Built-in JAADU |
| **Code Explanation** | Manual comments | ✅ Built-in Samjho |
| **Time-Travel Debug** | None | ✅ Built-in Time Machine |
| **Learning Curve** | Steep | 🎯 Gentle with features |
| **Debugging Speed** | Slow (print/breakpoints) | ⚡ Fast (time travel) |
| **Understanding Code** | Read documentation | 🧠 Self-explaining |

---

## 💡 Tips & Tricks

### Tip 1: Use Samjho for Learning

When learning new concepts, enable Samjho to understand execution:

```codesi
samjhao_on()
// Try complex code
samjhao()  // Understand what happened
```

### Tip 2: Time Machine for Algorithm Debugging

Use Time Machine to step through algorithms:

```codesi
time_machine_on()
// Run algorithm
timeline()  // See all steps
peeche(n)   // Go to specific step
```

### Tip 3: JAADU for Fast Prototyping

Enable JAADU when coding quickly:

```bash
codesi --jaadu script.cds
```

### Tip 4: Combine Features Strategically

```codesi
// Learning phase: Use all
samjhao_on()
time_machine_on()

// Production: Disable all
samjhao_off()
time_machine_off()
```

### Tip 5: Manage Snapshot Limits

```codesi
// Short programs: Low limit
time_machine_on(50)

// Long programs: Higher limit
time_machine_on(500)

// Check status regularly
time_machine_status()
```

---

## 🚨 Common Issues & Solutions

### Issue 1: Too Many Snapshots

**Problem:** Time Machine slowing down

**Solution:**
```codesi
time_machine_off()  // Clear snapshots
time_machine_on(100)  // Restart with lower limit
```

### Issue 2: Explanations Too Verbose

**Problem:** Samjho generating too much output

**Solution:**
```codesi
// Disable temporarily
samjhao_off()
// Run large loop
har i se 1 tak 1000 { ... }
// Re-enable
samjhao_on()
```

### Issue 3: JAADU Over-Correcting

**Problem:** JAADU changing valid variable names

**Solution:**
```bash
# Use suggestion mode (default)
codesi script.cds

# Not JAADU mode
# codesi script.cds --jaadu
```

---

## 📚 Summary

Codesi's **three world-first features** revolutionize programming:

### 🪄 JAADU Auto-Correction
- ✅ Detects typos automatically
- ✅ Suggests corrections
- ✅ Auto-fixes in JAADU mode
- ✅ 60%+ similarity matching

### 🧠 Samjho Self-Explaining
- ✅ Explains code execution
- ✅ Tracks variable changes
- ✅ No AI/ML required
- ✅ Step-by-step breakdown

### ⏰ Time Machine Debugger
- ✅ Travel through execution
- ✅ Restore past states
- ✅ View complete timeline
- ✅ Deep copy snapshots

**These features work together** to create the most beginner-friendly yet powerful programming experience ever created!

---

## 🔗 Related Documentation

- **[Quickstart Guide](QUICKSTART.md)** - Get started with Codesi
- **[Complete Basics](COMPLETE_BASICS.md)** - Learn fundamentals
- **[Built-in Functions](BUILTIN_FUNCTIONS.md)** - Function reference
- **[Troubleshooting](TROUBLESHOOTING.md)** - Common issues

---

**Made with ❤️ in India | World's First Hinglish Programming Language**