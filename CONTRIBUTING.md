# Contributing to Codesi

First off, **thank you** for considering contributing to Codesi! 🎉

Codesi is a community-driven project, and we welcome contributions from developers of all skill levels. Whether you're fixing a typo, adding a feature, or improving documentation, every contribution matters.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Coding Guidelines](#coding-guidelines)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)
- [Community](#community)

---

## 📜 Code of Conduct

This project adheres to a [Code of Conduct](CODE_OF_CONDUCT.md). By participating, you are expected to uphold this code. Please report unacceptable behavior to the maintainers.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.7 or higher
- Git
- A GitHub account
- Basic understanding of Python (for code contributions)

### First Time Contributors

New to open source? Here are some good first issues:
- Documentation improvements
- Adding examples
- Fixing typos
- Writing tests
- Translating error messages

Look for issues labeled `good first issue` or `help wanted`.

---

## 🤝 How Can I Contribute?

### 1. 🐛 Reporting Bugs

Before creating a bug report:
- Check the [existing issues](https://github.com/codesi-lang)
- Try the latest version
- Collect debug information

**Bug Report Template:**

```markdown
## Bug Description
A clear description of the bug

## Steps to Reproduce
1. Create file with code: ...
2. Run command: ...
3. See error: ...

## Expected Behavior
What should happen

## Actual Behavior
What actually happened

## Environment
- Codesi Version: 1.0.0
- Python Version: 3.9.0
- OS: Windows 10 / macOS 12 / Ubuntu 20.04

## Additional Context
Any other relevant information
```

### 2. 💡 Suggesting Features

We love new ideas! Before suggesting:
- Check if it's already suggested
- Ensure it aligns with Codesi's goals
- Consider if it benefits most users

**Feature Request Template:**

```markdown
## Feature Description
Clear description of the feature

## Use Case
Why is this feature needed?

## Proposed Syntax (if applicable)
```codesi
// Example code showing the feature
```

## Alternative Solutions
Other ways to achieve this

## Additional Context
Links, references, mockups
```

### 3. 📝 Improving Documentation

Documentation is crucial! You can help by:
- Fixing typos and grammar
- Adding examples
- Clarifying confusing sections
- Translating to other languages
- Adding more detailed explanations

### 4. 🎨 Adding Examples

Share your Codesi programs! We need:
- Beginner-friendly examples
- Real-world use cases
- Algorithm implementations
- Game examples
- Utility scripts

### 5. 💻 Writing Code

Ready to code? Here's what we need:
- Bug fixes
- New features
- Performance improvements
- Test coverage
- Refactoring

---

## 🛠️ Development Setup

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then:
git clone https://github.com/codesi-lang
cd codesi
```

### 2. Create a Branch

```bash
# Create a new branch for your feature
git checkout -b feature/your-feature-name

# Or for bug fixes
git checkout -b fix/bug-description
```

### 3. Make Changes

Edit `codesi.py` and test your changes:

```bash
# Test with REPL
python codesi.py

# Test with a file
python codesi.py test.cds

# Debug mode
python codesi.py test.cds --debug
```

### 4. Test Thoroughly

Create test cases in the `examples/` folder:

```codesi
// test_your_feature.cds
// Test your new feature here
```

Run through common scenarios:
- ✅ Basic functionality
- ✅ Edge cases
- ✅ Error handling
- ✅ Integration with existing features

### 5. Update Documentation

If you changed:
- **Syntax**: Update `docs/SYNTAX_GUIDE.md`
- **Functions**: Update `docs/BUILTIN_FUNCTIONS.md`
- **Features**: Update `README.md` and relevant docs
- **Examples**: Add to `examples/` folder

---

## 📐 Coding Guidelines

### Python Style

Follow PEP 8 with these specifics:

```python
# Use descriptive variable names
def visit_BinaryOp(self, node):  # Good
def vbo(self, n):  # Bad

# Add docstrings for complex functions
def complex_function(param):
    """
    Brief description of what this does.
    
    Args:
        param: Description of parameter
        
    Returns:
        Description of return value
    """
    pass

# Use type hints where helpful
def tokenize(self) -> List[Token]:
    pass

# Keep functions focused (single responsibility)
# Use dataclasses for structured data
# Comment complex logic
```

### Codesi Language Design Principles

When adding language features:

1. **Hinglish First**: Use natural Hindi-English mix
   ```codesi
   // Good
   agar (condition) { ... }
   
   // Avoid pure English
   if (condition) { ... }
   ```

2. **Consistency**: Follow existing patterns
   ```codesi
   // We use 'karya' for functions
   karya name() { ... }
   
   // Don't introduce 'function'
   ```

3. **Beginner-Friendly**: Clear error messages
   ```python
   # Good
   raise CodesiError("Variable 'x' define nahi hai")
   
   # Bad
   raise CodesiError("Undefined variable: x")
   ```

4. **Multiple Syntaxes**: Support learning progression
   ```codesi
   // Both should work
   har i se 0 tak 5 { ... }
   har i ke liye (0 se 5 tak) { ... }
   ```

### Code Organization

```python
# Keep this structure in codesi.py:

# 1. Imports and constants
# 2. Token types (Enum)
# 3. Token and AST classes (@dataclass)
# 4. Lexer class
# 5. Parser class
# 6. Exception classes
# 7. Runtime classes (Function, Class, Object)
# 8. Special systems (JAADU, Samjho, TimeMachine)
# 9. Interpreter class
# 10. Runner functions (run_codesi, run_file, repl, main)
```

### Testing Checklist

Before submitting, verify:

- [ ] Code runs without errors
- [ ] All existing features still work
- [ ] New feature works as expected
- [ ] Error messages are helpful
- [ ] Documentation is updated
- [ ] Examples are added (if applicable)
- [ ] No performance regression
- [ ] JAADU suggestions work correctly (if modified)
- [ ] Samjho explanations are accurate (if modified)
- [ ] Time Machine snapshots correctly (if modified)

---

## 📝 Commit Guidelines

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting)
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

**Examples:**

```bash
feat(parser): add support for switch-case statements

- Implemented SwitchCase AST node
- Added case and default keywords
- Updated parser to handle multiple cases

Closes #123

---

fix(lexer): handle escape sequences in strings

- Fixed \n, \t escape handling
- Added \r, \b, \f, \v support
- Added tests for edge cases

Fixes #456

---

docs(examples): add fibonacci sequence example

- Created examples/fibonacci.cds
- Shows both recursive and iterative approaches
- Added comments explaining logic
```

### Commit Best Practices

- Write clear, descriptive messages
- Keep commits focused (one logical change)
- Reference issues when applicable
- Use present tense ("add feature" not "added feature")

---

## 🔄 Pull Request Process

### Before Submitting

1. **Update your fork**:
   ```bash
   git remote add upstream https://github.com/codesi-lang
   git fetch upstream
   git merge upstream/main
   ```

2. **Run final tests**:
   ```bash
   # Test REPL
   python codesi.py
   
   # Test all examples
   for file in examples/*.cds; do
       python codesi.py "$file"
   done
   ```

3. **Update documentation**: Ensure README.md and docs/ are current

### Submitting the PR

1. **Push your branch**:
   ```bash
   git push origin feature/your-feature-name
   ```

2. **Create Pull Request** on GitHub with this template:

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Code refactoring

## Changes Made
- Change 1
- Change 2
- Change 3

## Testing Done
- [ ] Tested in REPL
- [ ] Tested with example files
- [ ] Tested edge cases
- [ ] Updated documentation

## Screenshots (if UI changes)
[Add screenshots]

## Related Issues
Closes #123
Related to #456

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] No breaking changes (or documented)
- [ ] All tests pass
```

### Review Process

1. **Automated checks** will run (if configured)
2. **Maintainers review** your code
3. **Discussion** may happen on the PR
4. **Changes requested** may need addressing
5. **Approval and merge** once ready

### After Merge

- Delete your branch (optional)
- Update your fork
- Celebrate! 🎉 You're now a Codesi contributor!

---

## 🎯 Areas Needing Help

### High Priority

1. **Testing Framework**: Help build comprehensive tests
2. **VSCode Extension**: Syntax highlighting for `.cds` files
3. **Performance**: Optimize interpreter performance
4. **Standard Library**: Add more built-in functions
5. **Documentation**: Improve and expand docs

### Feature Requests

Check [Issues](https://github.com/codesi-lang) for:
- Features marked `help wanted`
- Documentation improvements
- Performance optimizations
- New examples

### Long-term Goals

- Package manager (CPI - Codesi Package Index)
- JIT compilation
- Mobile app (Android/iOS)
- Web-based playground
- Debugger protocol
- IDE integrations

---

## 🌍 Community

### Communication Channels

- **GitHub Issues**: Bug reports, feature requests
- **GitHub Discussions**: Questions, ideas, showcase
- **Pull Requests**: Code contributions
- **Discord**: (Coming soon!)

### Getting Help

- Read the [Documentation](docs/)
- Check [existing issues](https://github.com/codesi-lang)
- Ask in GitHub Discussions
- Tag maintainers for urgent issues

### Recognition

Contributors are recognized in:
- README.md Contributors section
- CHANGELOG.md for each version
- GitHub contributor graphs
- Special mentions for significant contributions

---

## 💎 Quality Standards

We maintain high standards:

- ✅ **Code Quality**: Clean, readable, documented
- ✅ **Testing**: Thoroughly tested changes
- ✅ **Documentation**: Clear and comprehensive
- ✅ **Performance**: No unnecessary slowdowns
- ✅ **Security**: Safe and secure code
- ✅ **Accessibility**: Features work for all users

---

## 🙏 Thank You!

Every contribution, no matter how small, helps make Codesi better. We appreciate your time and effort!

**Special Thanks** to all our contributors! 🌟

---

## 📞 Contact

**Project Maintainer**: Rishaank Gupta
- GitHub: [@rishaankgupta](https://github.com/theLostB)
- Email: codesilang@gmail.com

**Project Repository**: https://github.com/codesi-lang

---

<div align="center">

**Happy Contributing! 🚀**

Made with ❤️ by the Codesi Community

</div>