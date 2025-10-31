import os
import sys

from codesi.exceptions import BreakException, ContinueException, ReturnException, CodesiError
from codesi.features.jaadu import jaadu_system
from codesi.features.samjho import samjho_system
from codesi.features.timemachine import time_machine
from codesi.interpreter.interpreter import CodesiInterpreter
from codesi.lexer.lexer import CodesiLexer
from codesi.parser.ast_nodes import (
    Assignment, CompoundAssignment, IndexAssignment, MemberAssignment, FunctionDef, ClassDef
)
from codesi.parser.parser import CodesiParser


HELP_TEXT = """
╔══════════════════════════════════════════════════════════════════════════╗
║                     CODESI PROGRAMMING LANGUAGE                          ║
║                       Programming Made Easy                              ║
║                           Version 0.0.1                                  ║
╚══════════════════════════════════════════════════════════════════════════╝

  BASIC SYNTAX
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  📤 OUTPUT
    likho("Hello World");              // Print to console
    likho("Name:", naam, "Age:", age); // Multiple values

  📥 INPUT
    naam = input_lo("Enter name: ");   // String input
    age = int_lo("Enter age: ");       // Integer input
    price = float_lo("Enter price: "); // Float input

  📦 VARIABLES
    x = 10;                // Integer
    naam = "Raj";          // String
    price = 99.99;         // Float
    active = sach;         // Boolean (true)
    empty = khaali;        // Null/None
    const PI = 3.14;       // Constant (immutable)

  ➕ OPERATORS
    Arithmetic: +  -  *  /  %  **  (power)
    Comparison: ==  !=  <  >  <=  >=
    Logical:    aur (and)  ya (or)  nahi (not)
    Assignment: =  +=  -=  *=  /=

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  CONTROL FLOW
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ❓ IF-ELSE (4 Variants)
    // Variant 1: Simple if
    agar (x > 5) likho("Big");

    // Variant 2: If-else with blocks
    agar (age >= 18) {
        likho("Adult");
    } nahi_to {
        likho("Minor");
    }

    // Variant 3: If-elif-else chain
    agar (marks >= 90) {
        likho("A Grade");
    } ya_phir (marks >= 75) {
        likho("B Grade");
    } nahi_to {
        likho("C Grade");
    }

    // Variant 4: Ternary operator
    result = age >= 18 ? "Adult" : "Minor";

  🔁 LOOPS (5+ Variants)
    // While loop
    jabtak (x < 10) {
        likho(x);
        x = x + 1;
    }

    // Do-while loop
    karo {
        likho(x);
        x = x + 1;
    } jabtak (x < 5);

    // For loop - Range based (2 ways)
    har i ke liye (0 se 5 tak) { likho(i); }
    har i se 0 tak 5 { likho(i); }

    // ForEach loop (3 ways)
    har item mein array { likho(item); }
    har fruit ke liye fruits mein { likho(fruit); }
    x ke liye array mein { likho(x); }

    // Loop control
    break;      // Exit loop
    continue;   // Skip to next iteration

  🔀 SWITCH-CASE
    day ke case mein {
        1 -> likho("Monday");
        2 -> likho("Tuesday");
        default -> likho("Other day");
    }

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  FUNCTIONS (7 Variants)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  // Simple function
  karya greet() {
      likho("Hello!");
  }

  // With parameters
  karya add(a, b) {
      vapas a + b;
  }

  // Default parameters
  karya greet(naam = "Guest") {
      vapas "Hello " + naam;
  }

  // Type annotations (parsed, not enforced)
  karya multiply(a: int, b: int) -> int {
      vapas a * b;
  }

  // Variadic/Rest parameters
  karya sum(...numbers) {
      total = 0;
      har num mein numbers { total = total + num; }
      vapas total;
  }

  // Lambda functions
  square = lambda (x) -> x * x;
  add = lambda (a, b) -> a + b;

  // Lambda with block
  complex = lambda (x, y) -> {
      result = x * x + y * y;
      vapas result;
  };

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ARRAYS (Lists)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  // Creation & Access
  arr = [1, 2, 3, 4, 5];
  first = arr[0];              // 1
  last = arr[-1];              // 5
  arr[2] = 100;                // Modify element

  // Methods
  arr.push(6);                 // Add to end → dalo
  arr.pop();                   // Remove from end → nikalo
  arr.shift();                 // Remove from start → pehla_nikalo
  arr.unshift(0);              // Add to start → pehle_dalo
  arr.lambai();                // Length → size
  arr.sort();                  // Sort array → arrange
  arr.reverse();               // Reverse → ulta
  arr.jodo(", ");              // Join → "1, 2, 3"
  arr.slice(1, 3);             // Slice → cutkr

  // Higher-order functions
  arr.map(lambda (x) -> x * 2);
  arr.filter(lambda (x) -> x > 5);
  arr.reduce(lambda (acc, x) -> acc + x, 0);

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   OBJECTS (Dictionaries)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  // Creation & Access
  person = {naam: "Raj", umra: 25, city: "Mumbai"};
  person.naam;                 // "Raj"
  person["umra"];              // 25
  person.phone = "9876543210"; // Add property
  likho(person.keys());               
  likho(person.values());             
  likho(person.hai_kya("naam")); 

  // Methods
  person.keys();               // [naam, umra, city, phone]
  person.values();             // [Raj, 25, Mumbai, 9876543210]
  person.hai_kya("naam");      // Check if key exists

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   CLASSES & OOP
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  // Simple class
  class Person {
      banao(naam, umra) {      // Constructor
          ye.naam = naam;      // 'ye' = 'this/self'
          ye.umra = umra;
      }

      karya intro() {
          vapas "I am " + ye.naam;
      }
  }

  // Create instance
  raj = new Person("Raj", 25);
  likho(raj.naam);                    // "Raj"
  likho(raj.intro());                 // "I am Raj"

  // Inheritance
  class Student extends Person {
      banao(naam, umra, roll) {
          super.banao(naam, umra);
          ye.roll = roll;
      }

      karya details() {
          vapas ye.naam + " - " + ye.roll;
      }
  }

  // Static methods
  class Math {
      static karya square(x) {
          vapas x * x;
      }
  }

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   ERROR HANDLING
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  try {
      x = 10 / 0;
  } catch (e) {
      likho("Error:", e.message);
  } finally {
      likho("Cleanup code");
  }

  // Throw custom errors
  throw {message: "Something went wrong!"};

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

   BUILT-IN FUNCTIONS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

     TYPE FUNCTIONS
    type_of(value)             // Get type name
    string_hai(x)              // Check if string
    array_hai(x)               // Check if array
    int_hai(x)                 // Check if integer
    float_hai(x)               // Check if float
    bool_hai(x)                // Check if boolean

     CONVERSION
    int_bnao("123")            // String to int → 123
    float_bnao("3.14")         // String to float → 3.14
    string_bnao(456)           // Any to string → "456"
    bool_bnao(1)               // Any to boolean → sach

     MATH FUNCTIONS
    math_absolute(-10)         // Absolute value → 10
    math_square(16)            // Square root → 4.0
    math_power(2, 10)          // Power → 1024
    math_random(1, 100)        // Random int between 1-100
    math_gol(3.7)              // Round → 4
    math_niche(3.7)            // Floor → 3
    math_upar(3.2)             // Ceil → 4
    math_sin(x)                // Trigonometric functions
    math_cos(x)
    math_tan(x)
    math_log(x)
    math_exp(x)

     STRING METHODS
    text.lambai()              // Length → size
    text.bada_karo()           // Uppercase
    text.chota_karo()          // Lowercase
    text.saaf_karo()           // Trim whitespace
    text.todo(" ")             // Split by space
    text.badlo("old", "new")   // Replace first occurrence
    text.sab_badlo("old", "new") // Replace all
    text.included_hai("sub")   // Check substring
    text.start_hota_hai("Hi")  // Starts with
    text.end_hota_hai("!")     // Ends with

     FILE OPERATIONS
    file_padho("data.txt")           // Read file
    file_likho("out.txt", "content") // Write file
    file_append("log.txt", "line")   // Append to file
    file_hai("file.txt")             // Check if exists
    file_delete("old.txt")           // Delete file
    file_copy("a.txt", "b.txt")      // Copy file
    file_move("old.txt", "new.txt")  // Move file
    file_size("data.txt")            // Get file size
    dir_banao("folder")              // Create directory
    dir_list(".")                    // List directory

     JSON OPERATIONS
    json_parse('{"naam": "Raj"}')    // Parse JSON string
    json_stringify({naam: "Raj"})    // Convert to JSON

     TIME FUNCTIONS
    time_now()                 // Current timestamp
    time_sleep(2)              // Sleep for 2 seconds

     UTILITY
    lambai(arr)                // Length of array/string
    range(5)                   // [0, 1, 2, 3, 4]
    range(2, 5)                // [2, 3, 4]
    repeatkr("Hi", 3)          // "HiHiHi"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  FIRST OF ITS KIND FEATURES
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

    JAADU MODE (Context-Aware Auto-Correction)
    Start REPL with: codesi --jaadu
    
    Revolutionary features:
    ✨ Context-aware: Knows methods vs functions vs keywords
    ✨ Phonetic matching: leekho → likho (Hindi sounds)
    ✨ Confidence scoring: 60-100% accuracy levels
    ✨ Method chains: arr.mep().filtr() → arr.map().filter()
    ✨ Dual language: English + Hindi method aliases
    ✨ Case insensitive: Liko/LIKO/liko → likho
    ✨ Performance: 200x faster with LRU cache
    
    Example corrections:
    • liko("Hi") → likho("Hi")           [Function typo]
    • arr.pus(4) → arr.push(4)           [Method typo]
    • leekho("Hi") → likho("Hi")         [Phonetic match]
    • arr.mep().filtr() → arr.map().filter() [Chain typos]
    
    Maximum correction: Up to 3-4 character differences!

    SAMJHAO MODE (Code Explainer without AI)
    samjhao_on()               // Enable explanation mode
    samjhao_off()              // Disable explanation
    samjhao()                  // Shows the explanations

    Explains every step of code execution:
    - Variable assignments
    - Operations & calculations
    - Function calls & returns
    - Loop iterations
    - Conditional branches

    TIME MACHINE (Time-Travel)
    time_machine_on()          // Enable time travel
    time_machine_on(max=500)   // With custom snapshot limit
    time_machine_off()         // Disable time machine
    time_machine_status()      // Check status

    peeche()                   // Go back 1 step
    peeche(3)                  // Go back 3 steps
    aage()                     // Go forward 1 step
    aage(2)                    // Go forward 2 steps
    timeline()                 // Show complete execution history

    Travel through your code's execution history!
    - View variable states at any point
    - Debug by going backwards
    - Understand program flow

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  REPL COMMANDS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  TIPS & TRICKS
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  1. Use JAADU mode for typo protection: codesi --jaadu
  2. Enable samjhao_on() to understand complex code flows
  3. Use time_machine for debugging without print statements
  4. Semicolons are optional in REPL (but recommended in files)
  5. Use !! to quickly repeat the last command
  6. Type vars() anytime to see current state
  7. Lambda functions great for array operations (map/filter)
  8. Use 'ye' instead of 'this' or 'self' in classes

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  LEARN MORE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  Documentation:  https://github.com/codesi-lang/codesi/tree/main/docs
  Examples:       https://github.com/codesi-lang/codesi/tree/main/examples
  Report Issues:  https://github.com/codesi-lang/codesi/issues
  Community:      https://discord.gg/codesi

  Type 'exit()' to quit REPL
  Type 'help()' anytime to see this guide again

╔══════════════════════════════════════════════════════════════════════════╗
║            Made with Love for everyone                                   ║
║                  Happy Coding!                                           ║
╚══════════════════════════════════════════════════════════════════════════╝
"""

def repl(jaadu_mode=False):
    """Interactive REPL mode - Professional Edition"""
    print("=" * 88)
    print("Codesi REPL v0.0.1 - The first of its kind Programming Language")
    if jaadu_mode:
        print("JAADU Mode: Auto-correction is ON.")
    print("Type 'help', 'copyright', 'credits' or 'license' for more information or 'exit' to quit.")
    print("=" * 88)
    
    interpreter = CodesiInterpreter()
    line_num = 1
    history = []
    multiline_buffer = ""
    in_multiline = False
    
    while True:
        try:
            if in_multiline:
                prompt = f"      ...> "
            else:
                prompt = f"codesi:{line_num}> "
            
            code = input(prompt)
            
            stripped_code = code.strip()

            if stripped_code in ['exit()', 'quit()', 'exit', 'quit']:
                print("Alvida! (Goodbye!)")
                break
            
            if stripped_code in ['help()', 'help']:
                print(HELP_TEXT)
                continue

            if code.strip() in ['copyright()', 'copyright']:
                print("""
            ╔══════════════════════════════════════════════════════════════════════════╗
            ║                            COPYRIGHT NOTICE                              ║
            ╚══════════════════════════════════════════════════════════════════════════╝

            Codesi Programming Language
            Version 0.0.1

            Copyright (c) 2025 Codesi Community
            All rights reserved.

            ╚══════════════════════════════════════════════════════════════════════════╝
            """)
                continue

            if code.strip() in ['credits()', 'credits']:
                print("""
            ╔══════════════════════════════════════════════════════════════════════════╗
            ║                          CREDITS & THANKS                                ║
            ╚══════════════════════════════════════════════════════════════════════════╝

              Core Team:
                • Rishaank Gupta - Creator/Founder & Lead Developer
                • Codesi Community - Contributors

              Inspired By:
                • Python - For elegant syntax
                • JavaScript - For flexibility
                • Ruby - For developer happiness
                • Hindi/Hinglish - Our beautiful language

              Special Thanks To:
                • All open-source contributors
                • Early adopters and testers
                • Everyone who believed in accessible programming

              Want to Contribute?
                GitHub: https://github.com/codesi-lang/codesi?tab=contributing-ov-file
                Join our Discord: https://discord.gg/codesi

              Support Us:
                  Star us on GitHub
                  Share with friends
                  Report bugs
                  Contribute code
                  Improve documentation

            ╔══════════════════════════════════════════════════════════════════════════╗
            ║                         Thank you! Shukriya!                             ║
            ╚══════════════════════════════════════════════════════════════════════════╝
            """)
                continue
            
            if code.strip() in ['license()', 'license']:
                print("""
            ╔══════════════════════════════════════════════════════════════════════════╗
            ║                           MIT LICENSE                                    ║
            ╚══════════════════════════════════════════════════════════════════════════╝

            MIT License

            Copyright (c) 2025 Codesi Community

            Permission is hereby granted, free of charge, to any person obtaining a copy
            of this software and associated documentation files (the "Software"), to deal
            in the Software without restriction, including without limitation the rights
            to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
            copies of the Software, and to permit persons to whom the Software is
            furnished to do so, subject to the following conditions:

            The above copyright notice and this permission notice shall be included in all
            copies or substantial portions of the Software.

            THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
            IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
            FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
            AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
            LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
            OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
            SOFTWARE.

            ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

              In Simple Terms (Hinglish):

              KYA KAR SAKTE HO:
                • Apne projects mein use karo (personal/commercial)
                • Code modify karo aur redistribute karo
                • Sublicense bana sakte ho
                • Bech sakte ho

               SHARTE (Conditions):
                • Is copyright notice ko rakhna ZAROORI hai
                • License text include karna hoga

              WARRANTY NAHI HAI:
                • Software "jaise hai waisa hai" diya gaya hai
                • Koi guarantee nahi ki bug-free hoga
                • Authors ki koi legal liability nahi hai

            Full license: https://opensource.org/licenses/MIT

           ╚══════════════════════════════════════════════════════════════════════════╝
            """)
                continue
            
            if stripped_code in ['clear()', 'clear']:
                os.system('cls' if os.name == 'nt' else 'clear')
                continue
            
            if stripped_code in ['samjhao()']:
                print(samjho_system.get_explanation())
                continue

            if stripped_code in ['samjhao_on()']:
                samjho_system.enable()
                print("Samjhao mode activated! Ab har step explain hoga.")
                continue

            if stripped_code in ['samjhao_off()']:
                samjho_system.disable()
                print("Samjhao mode deactivated!")
                continue

            if stripped_code in ['samjhao_clear()']:
                samjho_system.clear()
                print("Explanations cleared!")
                continue

            if code.strip() in ['quickhelp()', 'qhelp()']:
                print("""
            🚀 CODESI QUICK REFERENCE
            ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            likho("text")              Print
            naam = input_lo("?")       Input
            agar (x > 5) {...}         If statement
            jabtak (x < 10) {...}      While loop
            har i ke liye (0 se 5 tak) {...}     For loop
            karya add(a,b) {...}       Function
            class Name {...}           Class
            try {...} catch(e) {...}   Error handling
            
            Special: samjhao_on(), time_machine_on(), help()
            ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
            Type 'help()' for complete guide
            """)
                continue

            if stripped_code in ['peeche()']:
                snapshot_index = time_machine.go_back()
                if isinstance(snapshot_index, str):
                    print(snapshot_index)
                else:
                    snap = time_machine.get_snapshot(snapshot_index)
                    if snap:
                        builtins = {k: v for k, v in interpreter.current_scope.items() if k.startswith('_') or callable(v)}
                        interpreter.current_scope.clear()
                        interpreter.current_scope.update(builtins)
                        interpreter.current_scope.update(snap['variables'])
                        print(time_machine._show_snapshot(snapshot_index))
                continue

            if stripped_code in ['aage()']:
                snapshot_index = time_machine.go_forward()
                if isinstance(snapshot_index, str):
                    print(snapshot_index)
                else:
                    snap = time_machine.get_snapshot(snapshot_index)
                    if snap:
                        builtins = {k: v for k, v in interpreter.current_scope.items() if k.startswith('_') or callable(v)}
                        interpreter.current_scope.clear()
                        interpreter.current_scope.update(builtins)
                        interpreter.current_scope.update(snap['variables'])
                        print(time_machine._show_snapshot(snapshot_index))
                continue

            if stripped_code in ['timeline()']:
                print(time_machine.show_all_steps())
                continue

            if stripped_code.startswith('!!'):
                if history:
                    code = history[-1]
                    print(f"Repeating: {code}")
                else:
                    print("Error: No previous command")
                    continue

            if stripped_code.startswith('!') and stripped_code[1:].isdigit():
                
                n = int(stripped_code[1:])
                if 0 < n <= len(history):
                    code = history[n-1]
                    print(f"Repeating #{n}: {code}")
                else:
                    print(f"Error: Command #{n} not found")
                    continue
            
            if stripped_code in ['vars()', 'vars']:
                print("\nCurrent Variables:")
                for key, val in interpreter.current_scope.items():
                    if not key.startswith('_') and not callable(val):
                        print(f"  {key} = {interpreter.to_string(val)}")
                print()
                continue
            
            if stripped_code in ['history()', 'history']:
                print("\nCommand History:")
                for i, cmd in enumerate(history[-10:], 1):
                    print(f"  {i}. {cmd}")
                print()
                continue
            
            if not stripped_code:
                continue
            
            if stripped_code.endswith('{') and not stripped_code.endswith('}'):
                in_multiline = True
                multiline_buffer = code + "\n"
                continue
            
            if in_multiline:
                multiline_buffer += code + "\n"
                if stripped_code == '}' or stripped_code.endswith('}'):
                    code = multiline_buffer
                    multiline_buffer = ""
                    in_multiline = False
                else:
                    continue
            
            history.append(code)
            
            try:
                if jaadu_mode:
                    fixed_code, fixes = jaadu_system.auto_fix_code(code)
                    if fixes:
                        for wrong, correct in fixes:
                            print(f"JAADU: '{wrong}' -> '{correct}'")
                        code = fixed_code
                
                lexer = CodesiLexer(code)
                tokens = lexer.tokenize()
            except Exception as e:
                print(f"Codesi Lexer Error: {str(e)}")
                continue

            try:
                parser = CodesiParser(tokens)
                ast = parser.parse()
            except SyntaxError as e:
                print(f"Codesi Syntax Error: {e}")
                continue
            except Exception as e:
                print(f"Codesi Parser Error: Code ya structure galat hai")
                print(f"   Kya likha hai: {code[:50]}...")
                continue
            
            try:
                for statement in ast.statements:
                    result = interpreter.visit(statement)
                    if result is not None and not isinstance(statement, 
                        (Assignment, CompoundAssignment, IndexAssignment, 
                         MemberAssignment, FunctionDef, ClassDef)):
                        print(f">= {interpreter.to_string(result)}")
            except CodesiError as e:
                print(f"Codesi Runtime Error: {e.message}")
                if hasattr(e, 'suggestion') and e.suggestion:
                    print(f"Suggestion: {e.suggestion}")
                if "define nahi hai" in e.message:
                    print(f"Hint: Spelling check karo ya pehle variable define karo.")
                continue
            except BreakException:
                print(f"Codesi Error: 'break' sirf loop ke andar use kar sakte hain")
                continue
            except ContinueException:
                print(f"Codesi Error: 'continue' sirf loop ke andar use kar sakte hain")
                continue
            except ReturnException:
                print(f"Codesi Error: 'vapas' sirf function ke andar use kar sakte hain")
                continue
            except ZeroDivisionError:
                print(f"Codesi Math Error: Zero se divide nahi kar sakte!")
                continue
            except IndexError as e:
                print(f"Codesi Array Error: Index out of range - array ki size check karo")
                continue
            except KeyError as e:
                print(f"Codesi Object Error: Property '{e}' nahi mili")
                continue
            except TypeError as e:
                print(f"Codesi Type Error: Galat data type use kiya")
                print(f"   Hint: Integer, float, string, array types check karo")
                continue
            except Exception as e:
                print(f"Codesi Unexpected Error: Kuch galat ho gaya")
                print(f"   Debug info: {type(e).__name__}")
                continue
            
            line_num += 1
            
        except KeyboardInterrupt:
            print("\nInterrupted! 'exit()' type karo band karne ke liye")
            in_multiline = False
            multiline_buffer = ""
            continue
        except EOFError:
            print("\nAlvida! (Goodbye!)")
            break  
        except SyntaxError as e:
            print(f"Syntax Error: {e}")
        except CodesiError as e:
            print(f"Runtime Error: {e.message}")
        except Exception as e:
            print(f"Error: {e}")