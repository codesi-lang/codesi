# Troubleshooting Guide

Common issues and their solutions when using Codesi Programming Language.

## 📋 Table of Contents

- [Running Programs](#running-programs)
- [REPL Issues](#repl-issues)
- [Syntax Errors](#syntax-errors)
- [Runtime Errors](#runtime-errors)
- [Performance Issues](#performance-issues)
- [FAQ](#faq)

---

## 🚀 Running Programs

### Problem: .cds File Won't Run

**Error:**
```
Error: Cannot open file 'script.cds'
```

**Solution:**
```bash
# Check file exists
ls script.cds

# Run with full path
codesi /full/path/to/script.cds

# Check file extension
# Must be .cds not .txt or other
```

---

### Problem: No Output

**Issue:** Program runs but shows nothing

**Solution:**
```codesi
// Check if you're using likho()
// ❌ Wrong
"Hello World"

// ✅ Correct
likho("Hello World")

// Check if variables are printed
x = 10
likho(x)  // Must use likho()
```

---

### Problem: Code Runs Partially

**Issue:** Program stops in middle

**Solution:**
```codesi
// Check for errors before stopping point
try {
    // Your code
} catch (e) {
    likho("Error:", e.message)
}

// Check for break statements
har i se 1 tak 10 {
    agar (i == 5) {
        break  // This stops loop!
    }
}
```

---

## 💬 REPL Issues

### Problem: REPL Won't Start

**Error:**
```
Error starting REPL
```

**Solution:**
```bash
# Check Python version
python3 --version  # Must be 3.7+

# Try with explicit python
codesi

```

---

### Problem: Can't Exit REPL

**Issue:** exit or quit doesn't work

**Solution:**
```
# Try these:
exit()
quit()

# Or press:
Ctrl+C (then type exit())
Ctrl+D (Linux/Mac)
Ctrl+Z (Windows)
```

---

### Problem: Lost All Variables

**Issue:** Variables disappeared after error

**Solution:**
```codesi
// REPL keeps variables unless:
// 1. You restart REPL
// 2. Error crashes REPL
// 3. You use time machine peeche()

// To preserve work:
// 1. Save important code to .cds file
// 2. Use history() to see past commands
```

---

### Problem: Multi-line Input Not Working

**Issue:** Can't write functions in REPL

**Solution:**
```codesi
// Codesi supports multi-line!
// Just start with { and it continues

codesi:1> karya add(a, b) {
      ...>     vapas a + b
      ...> }

// Or write single line
codesi:1> karya add(a, b) { vapas a + b }
```

---

## ❌ Syntax Errors

### Problem: Unexpected Token

**Error:**
```
Line 5 par '}' ka unexpected use hai
```

**Solution:**
```codesi
// Check matching braces
// ❌ Wrong - missing closing brace
agar (x > 5) {
    likho("Big")

// ✅ Correct
agar (x > 5) {
    likho("Big")
}

// Use editor with brace matching!
```

---

### Problem: Missing Parentheses

**Error:**
```
Line 3 par '(' ki ummeed thi
```

**Solution:**
```codesi
// Conditions need parentheses
// ❌ Wrong
agar x > 5 {
    likho("Big")
}

// ✅ Correct
agar (x > 5) {
    likho("Big")
}
```

---

### Problem: Invalid Assignment

**Error:**
```
Line 7 par galat assignment hai
```

**Solution:**
```codesi
// Can't assign to expressions
// ❌ Wrong
x + y = 10

// ✅ Correct
result = x + y

// Can assign to variables, array indices, object properties
x = 10           // ✅
arr[0] = 5       // ✅
obj.naam = "Raj" // ✅
```

---

### Problem: String Not Closed

**Error:**
```
Unterminated string
```

**Solution:**
```codesi
// Check matching quotes
// ❌ Wrong
naam = "Rishaank

// ✅ Correct
naam = "Rishaank"

// Use same quote type
naam = "Rishaank"  // ✅
naam = 'Rishaank'  // ✅
naam = "Rishaank'  // ❌ Mismatch
```

---

## 🐛 Runtime Errors

### Problem: Variable Not Defined

**Error:**
```
Variable 'x' define nahi hai
```

**Solution:**
```codesi
// Define variable before using
// ❌ Wrong
likho(naam)

// ✅ Correct
naam = "Rishaank"
likho(naam)

// Check spelling
naame = "Rishaank"
likho(naam)  // ❌ Typo: naam vs naame
```

---

### Problem: Division by Zero

**Error:**
```
Zero se divide nahi kar sakte
```

**Solution:**
```codesi
// Check before dividing
// ❌ Wrong
result = 10 / 0

// ✅ Correct
agar (b != 0) {
    result = a / b
} nahi_to {
    likho("Cannot divide by zero")
}

// Or use try-catch
try {
    result = a / b
} catch (e) {
    likho("Error:", e.message)
}
```

---

### Problem: Index Out of Range

**Error:**
```
Index range ke bahar hai
```

**Solution:**
```codesi
arr = [1, 2, 3]

// ❌ Wrong
likho(arr[10])  // Only 3 elements!

// ✅ Correct - check length first
agar (10 < arr.lambai()) {
    likho(arr[10])
} nahi_to {
    likho("Index too large")
}

// Use negative indices for end
likho(arr[-1])  // Last element
```

---

### Problem: Type Mismatch

**Error:**
```
Type mismatch in operation
```

**Solution:**
```codesi
// Can't mix incompatible types
// ❌ Wrong
result = "10" * 2  // String * Number

// ✅ Correct - convert first
result = int_bnao("10") * 2  // 20

// Check types
agar (int_hai(value)) {
    result = value * 2
}
```

---

### Problem: Function Not Found

**Error:**
```
Function 'xyz' define nahi hai
```

**Solution:**
```codesi
// Define function before calling
// ❌ Wrong
greet("Raj")

karya greet(naam) {
    likho("Hello", naam)
}

// ✅ Correct - define first
karya greet(naam) {
    likho("Hello", naam)
}

greet("Raj")

// Check spelling and JAADU suggestions
likho("Hello")  // JAADU suggests 'likho'
```

---

### Problem: Break/Continue Outside Loop

**Error:**
```
'break' sirf loop ke andar use kar sakte hain
```

**Solution:**
```codesi
// Only use break/continue inside loops
// ❌ Wrong
agar (x > 5) {
    break  // Not in a loop!
}

// ✅ Correct
har i se 1 tak 10 {
    agar (i == 5) {
        break  // Inside loop
    }
}
```

---

## ⚡ Performance Issues

### Problem: Program Very Slow

**Issue:** Code takes too long to run

**Solution:**

**1. Check for infinite loops:**
```codesi
// ❌ Infinite loop
jabtak (sach) {
    likho("Forever")
    // Missing break!
}

// ✅ Add exit condition
jabtak (sach) {
    input = input_lo("Command: ")
    agar (input == "exit") {
        break
    }
}
```

**2. Optimize recursive functions:**
```codesi
// ❌ Slow - recalculates
karya fibonacci(n) {
    agar (n <= 1) vapas n
    vapas fibonacci(n-1) + fibonacci(n-2)
}

// ✅ Fast - iterative
karya fibonacci(n) {
    agar (n <= 1) vapas n
    a = 0
    b = 1
    har i se 2 tak n + 1 {
        temp = a + b
        a = b
        b = temp
    }
    vapas b
}
```

**3. Disable Samjho/Time Machine:**
```codesi
// These add overhead
samjhao_off()
time_machine_off()
```

---

### Problem: High Memory Usage

**Issue:** Program uses too much RAM

**Solution:**

**1. Time Machine snapshots:**
```codesi
// Limit snapshots
time_machine_on(50)  // Instead of default 100

// Or disable
time_machine_off()
```

**2. Large arrays:**
```codesi
// Don't create unnecessarily large arrays
// Process in chunks instead
```

---



## ❓ FAQ

### Q: Why is JAADU not working?

**A:** JAADU only works with `--jaadu` flag:
```bash
codesi --jaadu
```

Default mode only shows suggestions.

---

### Q: How to save REPL session?

**A:** REPL doesn't auto-save. Copy your code to a `.cds` file:
```codesi
// Save important code as you write
// Use history() to see past commands
```

---

### Q: Can I use Codesi in Jupyter notebooks?

**A:** Not directly. Codesi is a standalone interpreter. Use:
```python
# In Python
import subprocess
result = subprocess.run(['python', 'codesi_production.py', 'script.cds'])
```

---

### Q: Why don't I see colors in output?

**A:** Codesi uses plain text output. For colored output, you'd need terminal support.

---

### Q: How to clear REPL screen?

**A:** Use:
```codesi
clear()
```

Or use terminal command:
- Windows: `cls`
- Mac/Linux: `clear` (Ctrl+L)

---

### Q: Can I import Python libraries?

**A:** No. Codesi is independent of Python libraries. It has its own built-in functions.

---

### Q: How to debug my code?

**A:** Use these tools:
1. **Samjho**: `samjhao_on()` - Explain execution
2. **Time Machine**: `time_machine_on()` - Navigate history
3. **Try-catch**: Catch errors
4. **likho()**: Print debug info

---

### Q: Where are error logs saved?

**A:** Codesi doesn't save logs by default. To save:
```bash
# Redirect output to file
codesi script.cds > output.log 2>&1
```

---

### Q: Program crashes without error message

**A:** Add try-catch at top level:
```codesi
try {
    // Your entire program
} catch (e) {
    likho("Fatal error:", e.message)
}
```

---

## 🆘 Still Having Issues?

### Get Help:

1. **Check Documentation**: `docs/` folder
2. **Search Issues**: [GitHub Issues](https://github.com/rishaankgupta/codesi/issues)
3. **Ask Community**: GitHub Discussions
4. **Report Bug**: Open new issue with:
   - Codesi version
   - Python version
   - Operating system
   - Complete error message
   - Minimal code to reproduce

### Before Reporting:

- [ ] Checked this troubleshooting guide
- [ ] Searched existing issues
- [ ] Tried on latest version
- [ ] Can reproduce consistently
- [ ] Have minimal example

---

## 🔍 Debug Checklist

When something goes wrong:

1. **Read the error message** - It usually tells you what's wrong
2. **Check line number** - Error messages show line numbers
3. **Enable Samjho** - See what's happening step by step
4. **Use Time Machine** - Go back and check state
5. **Add likho()** - Print variables to see values
6. **Simplify** - Remove code until it works, then add back
7. **Check examples** - Compare with working examples
8. **Ask for help** - With specific error message and code

---

## 💡 Prevention Tips

Avoid issues before they happen:

1. **Use JAADU mode** while learning
2. **Enable Samjho** for new concepts
3. **Write comments** to explain logic
4. **Test frequently** - Don't write too much before testing
5. **Use try-catch** for risky operations
6. **Validate input** - Check user input before using
7. **Check types** - Use `prakar()` when unsure
8. **Read docs** - Check syntax before using new features

---

**Happy Coding! 🚀**

If this guide helped you, consider contributing your own solutions!