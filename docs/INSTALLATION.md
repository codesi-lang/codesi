# Installation Guide

Complete installation instructions for Codesi Programming Language.

## 📋 Table of Contents

- [System Requirements](#system-requirements)
- [Quick Install](#quick-install)
- [Platform-Specific Instructions](#platform-specific-instructions)
- [Verification](#verification)
- [IDE Setup](#ide-setup)

---

## 💻 System Requirements

### Minimum Requirements
- **Python**: 3.7 or higher
- **RAM**: 512 MB
- **Disk Space**: 10 MB
- **OS**: Windows, macOS, Linux, Android (through termux)

### Recommended
- **Python**: 3.9 or higher
- **RAM**: 2 GB
- **Disk Space**: 50 MB (for examples and docs)

### Dependencies
**None!** Codesi has zero external dependencies. It's pure Python.

---

## ⚡ Quick Install

### Method 1: Install through pip (Recommended for android user, using termux)

```bash
# Clone the repository
pip install codesi

# Test installation
codesi --version
```

### Method 2: Install through installer (Recommended for Windows/Linux/Mac)

1. Go to release section of this repo
2. Click on the installer for your OS
3. Download it
4. Open and run the installer
5. Run: `codesi --version` in your cmd (if windows) or in terminal

---

## ✅ Verification

### Test Installation

```bash
# Check version
codesi --version
```

### Run Test Script

```bash
# Create test file
echo 'likho("Namaste Duniya!")' > test.cds

# Run it
codesi test.cds

# Should output: Namaste Duniya!
```

### Interactive REPL

```bash
# Start REPL
codesi

# Try these commands:
codesi:1> likho("Hello")
codesi:2> x = 10
codesi:3> likho(x * 2)
codesi:4> exit()
```

### Run Examples

```bash
# Run hello world
codesi examples/hello_world.cds

# Run calculator
codesi examples/calculator.cds

# Run with JAADU mode
codesi examples/fibonacci.cds --jaadu
```

---

## 🚀 Next Steps

After installation:

1. **Learn the Basics**: Read [QUICKSTART.md](QUICKSTART.md)
2. **Try Examples**: Run files in `examples/` folder
3. **Read Documentation**: Check `docs/` for detailed guides
4. **Join Community**: GitHub Discussions

---

## 📞 Need Help?

If you're still having issues:

1. Check [GitHub Issues](https://github.com/codesi-lang)
2. Create a new issue with:
   - Your OS and Python version
   - Error message (full output)
   - Steps you tried
3. Join community discussions

---

Next: [Quick Start Guide](QUICKSTART.md)