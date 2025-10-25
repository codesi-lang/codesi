# Security Policy

## 🛡️ Security at Codesi

We take the security of Codesi Programming Language seriously. This document outlines our security policies and how to report vulnerabilities.

---

## 📋 Supported Versions

| Version | Supported          | Security Updates |
| ------- | ------------------ | ---------------- |
| 0.0.1   | ✅ Yes            | ✅ Active       |

**Note**: We recommend always using the latest stable version for the best security and features.

---

## 🔒 Security Features

Codesi has been designed with security in mind:

### Built-in Security Measures

1. **No External Dependencies**: Zero third-party libraries reduce attack surface
2. **Safe Evaluation**: No use of Python's dangerous `eval()` function
3. **Scope Isolation**: Proper variable scoping prevents unintended access
4. **Input Sanitization**: File operations validate paths
5. **Error Handling**: Comprehensive exception handling prevents crashes
6. **Type Safety**: Strong type checking at runtime

### File System Security

```python
# Safe file operations
- Path validation
- Permission checking
- Error handling for all file I/O
- No arbitrary code execution
```

### Code Execution Security

```python
# Codesi interpreter
- AST-based interpretation (no eval)
- Sandboxed scope execution
- Controlled function calls
- Safe built-in functions only
```

---

## 🚨 Reporting a Vulnerability

### Where to Report

**DO NOT** create a public GitHub issue for security vulnerabilities.

Instead, report vulnerabilities privately to:

**Email**: codesilang@gmail.com 
**GitHub**: Send a private security advisory at https://github.com/codesi-lang  
**Direct Contact**: [@rishaankgupta](site.rishaank@gmail.com)

### What to Include

A good security report should include:

```markdown
## Vulnerability Type
[e.g., Code Injection, Path Traversal, DoS, etc.]

## Affected Version
Codesi version number (e.g., 0.0.1)

## Description
Clear description of the vulnerability

## Steps to Reproduce
1. Create file with: ...
2. Run command: ...
3. Observe: ...

## Impact
What can an attacker do with this?

## Proof of Concept
```codesi
// Minimal code demonstrating the issue
```

## Suggested Fix
If you have ideas for fixing it

## Your Environment
- OS: Windows/macOS/Linux
- Python version: 3.x
- Additional context
```

### Response Timeline

We aim to respond to security reports within:

- **Acknowledgment**: 48 hours
- **Initial Assessment**: 5 business days
- **Fix Development**: Depends on severity
  - **Critical**: 7 days
  - **High**: 14 days
  - **Medium**: 30 days
  - **Low**: Next release
- **Public Disclosure**: After fix is released

### Disclosure Policy

We follow responsible disclosure:

1. **Private Report**: You report the issue privately
2. **Acknowledgment**: We acknowledge receipt
3. **Investigation**: We investigate and develop a fix
4. **Testing**: We test the fix thoroughly
5. **Release**: We release a patched version
6. **Public Disclosure**: We publicly disclose after users have time to update (typically 7-14 days)
7. **Credit**: We credit you (unless you prefer anonymity)

---

## 🎯 Security Vulnerability Categories

### Critical 🔴

Vulnerabilities that:
- Allow arbitrary code execution
- Enable privilege escalation
- Expose sensitive data without authentication
- Cause complete system compromise

**Response Time**: Immediate (within 7 days)

### High 🟠

Vulnerabilities that:
- Allow unauthorized data access
- Enable authentication bypass
- Cause significant data loss
- Lead to denial of service

**Response Time**: 14 days

### Medium 🟡

Vulnerabilities that:
- Expose limited information
- Require user interaction
- Have limited impact scope
- Affect only specific configurations

**Response Time**: 30 days

### Low 🟢

Vulnerabilities that:
- Require complex attack chains
- Have minimal real-world impact
- Affect only edge cases
- Are easily mitigated by users

**Response Time**: Next release

---

## 🔐 Known Security Considerations

### Current Design Decisions

1. **File System Access**
   - Codesi can read/write files with user permissions
   - Users should be careful with untrusted `.cds` files
   - No privilege escalation possible

2. **REPL Mode**
   - Full access to interpreter features
   - Runs with current user permissions
   - Use caution when running untrusted code

3. **Import System**
   - Can import other Codesi files
   - Imported files execute with same permissions
   - Be cautious with untrusted imports

### Best Practices for Users

```codesi
// ✅ Safe: Read from controlled locations
content = file_padho("data/config.txt")

// ⚠️  Caution: User-provided paths
user_path = input_lo("File path: ")
// Validate before using!

// ❌ Risky: Blindly trusting user input
// Always validate and sanitize!
```

---

## 🛡️ Security Hardening

### For Script Authors

1. **Validate Input**
   ```codesi
   // Always validate user input
   naam = input_lo("Naam: ")
   agar (naam.lambai() > 100) {
       throw {message: "Naam bahut lamba hai"}
   }
   ```

2. **Check File Paths**
   ```codesi
   // Validate file paths before using
   karya safe_read(path) {
       // Check if file exists
       agar (!file_hai(path)) {
           throw {message: "File nahi mili"}
       }
       vapas file_padho(path)
   }
   ```

3. **Handle Errors**
   ```codesi
   // Use try-catch for file operations
   try {
       content = file_padho("data.txt")
   } catch (e) {
       likho("Error:", e.message)
   }
   ```

### For Environment Setup

1. **Run with Minimal Permissions**: Don't run Codesi as root/admin
2. **Isolated Directories**: Use separate directories for untrusted scripts
3. **Virtual Environments**: Use Python virtual environments
4. **Code Review**: Review `.cds` files before running
5. **Backup Data**: Regular backups before running new scripts

---

## 🔍 Security Audit

### Last Security Review
- **Date**: 2025-10-XX
- **Version**: 0.0.1
- **Reviewer**: Rishaank Gupta
- **Status**: No critical issues found

### Areas Audited
- ✅ Lexer and tokenizer
- ✅ Parser and AST generation
- ✅ Interpreter execution
- ✅ Built-in functions
- ✅ File I/O operations
- ✅ Scope management
- ✅ Error handling

### Security Testing
- Input fuzzing
- Path traversal attempts
- Code injection attempts
- Memory leak testing
- Error handling validation

---

## 🏆 Security Researchers

We appreciate security researchers who help keep Codesi secure.

### Recognition

Security researchers who responsibly disclose vulnerabilities will be:
- Credited in the security advisory (unless they prefer anonymity)
- Listed in our Hall of Fame
- Mentioned in release notes
- Given our sincere thanks!

### Hall of Fame

*No reported vulnerabilities yet - be the first!*

---

## 📚 Additional Resources

### Security Best Practices
- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Python Security](https://python.readthedocs.io/en/latest/library/security_warnings.html)
- [Secure Coding Guidelines](https://www.securecoding.cert.org/)

### Related Documentation
- [Contributing Guidelines](CONTRIBUTING.md)
- [Code of Conduct](CODE_OF_CONDUCT.md)
- [Issue Tracker](https://github.com/codesi-lang)

---

## 🔄 Updates to This Policy

This security policy may be updated from time to time. Major changes will be announced through:
- GitHub releases
- Repository README
- Security advisories

**Last Updated**: 2025-10-XX  
**Version**: 0.0.1

---

## ✅ Security Checklist for Contributors

Before submitting code that touches security-sensitive areas:

- [ ] No use of Python `eval()` or `exec()`
- [ ] Input validation for all user-provided data
- [ ] Path validation for file operations
- [ ] Proper error handling with no sensitive info leaks
- [ ] No hardcoded credentials or secrets
- [ ] Safe defaults for all options
- [ ] Documentation of security implications
- [ ] No introduction of new dependencies
- [ ] Testing for edge cases and attacks

---

## 🆘 Emergency Security Hotline

For critical, actively exploited vulnerabilities:

**Contact**: codesilang@gmail.com (Priority response)  
**GitHub Security Advisory**: https://github.com/codesi-lang
**Expected Response**: Within 24 hours

---

## 📜 Vulnerability Disclosure History

### Version 0.0.1
- **Status**: No known vulnerabilities
- **Release Date**: 2025-10-XX
- **Security Improvements**: Initial secure implementation

*Future vulnerabilities and fixes will be documented here*

---

## 🤝 Working With Us

We believe in:
- **Transparency**: Open communication about security
- **Collaboration**: Working together with researchers
- **Respect**: Treating all reporters with respect
- **Responsibility**: Quick action on valid reports
- **Recognition**: Crediting those who help us

---

## 📞 Contact

**Security Team**: codesilang@gmail.com  
**Project Lead**: Rishaank Gupta ([@rishaankgupta](https://github.com/theLostB))  
**GitHub**: https://github.com/codesi-lang

---

<div align="center">

**Thank you for helping keep Codesi secure! 🛡️**

Report vulnerabilities responsibly • Get recognized • Make Codesi safer for everyone

</div>