# Codesi: Complete Intermediate Guide

This guide builds upon the [Complete Basics Guide](COMPLETE_BASICS.md) and delves into more intermediate concepts in Codesi. Here, you'll learn about advanced function techniques, robust error handling, working with classes and objects, and more sophisticated data manipulation.

## 1. Advanced Functions

Beyond basic function definitions, Codesi offers powerful features for more flexible and expressive functions.

### Default Parameters

You can assign default values to function parameters. If an argument is not provided for such a parameter during a function call, its default value will be used.

```codesi
karya greetUser(name = "Guest", greeting = "Hello") {
    likho(greeting, ", ", name, "!");
}

greetUser("Rishaank");             // Output: Hello, Rishaank!
greetUser("Codesi Dev", "Namaste"); // Output: Namaste, Codesi Dev!
greetUser();                      // Output: Hello, Guest!
```

### Variadic Parameters (`...`)

Use the `...` (ellipsis) operator to define functions that can accept a variable number of arguments. These arguments are collected into an array.

```codesi
karya logMessages(...messages) {
    har msg mein messages {
        likho("LOG: ", msg);
    }
}

logMessages("App started", "User logged in", "Data fetched");
// Output:
// LOG: App started
// LOG: User logged in
// LOG: Data fetched
```

### Lambda Functions (`lambda`)

Lambda functions provide a concise way to define anonymous (unnamed) functions, often used for short, inline operations or as callbacks.

```codesi
// Single expression lambda (implicitly returns the expression result)
const add = lambda (a, b) -> a joda b;
likho("Sum: ", add(5, 7)); // Output: Sum: 12

// Lambda with a block body (requires 'vapas' for explicit return)
const processString = lambda (text) -> {
    likho("Original: ", text);
    vapas (text.upper() joda "!!!");
};
likho("Processed: ", processString("codesi"));
// Output:
// Original: codesi
// Processed: CODESI!!!
```

### Higher-Order Functions

Functions in Codesi can be passed as arguments to other functions or returned from functions. This enables powerful functional programming patterns.

```codesi
karya operate(num1, num2, operationFunc) {
    vapas (operationFunc(num1, num2));
}

const multiply = lambda (x, y) -> x guna y;
const divide = lambda (x, y) -> x bhag y;

likho("Result of multiply: ", operate(10, 5, multiply)); // Output: Result of multiply: 50
likho("Result of divide: ", operate(10, 5, divide));   // Output: Result of divide: 2.0
```

## 2. Object-Oriented Programming (OOP)

Codesi's OOP features allow you to structure your code using classes and objects, promoting reusability and modularity. Refer to [OOPs.md](OOPs.md) for a detailed guide.

### Classes and Objects

```codesi
class Book {
    banao(title, author) {
        ye.title = title;
        ye.author = author;
    }

    karya getInfo() {
        vapas (ye.title joda " by " joda ye.author);
    }
}

const myBook = new Book("The Codesi Way", "Rishaank Gupta");
likho("Book Info: ", myBook.getInfo()); // Output: Book Info: The Codesi Way by Rishaank Gupta
```

### Inheritance (`extends`)

Create new classes that inherit properties and methods from existing classes.

```codesi
class EBook extends Book {
    banao(title, author, fileSize) {
        super(title, author); // Call parent class constructor
        ye.fileSize = fileSize;
    }

    karya getInfo() {
        vapas (super.getInfo() joda " (File Size: " joda ye.fileSize joda "MB)");
    }
}

const digitalBook = new EBook("Codesi Advanced", "Rishaank", 5.2);
likho("EBook Info: ", digitalBook.getInfo()); // Output: EBook Info: Codesi Advanced by Rishaank (File Size: 5.2MB)
```

### Static Methods

Methods that belong to the class itself, not to instances of the class.

```codesi
class Utility {
    static karya generateId() {
        vapas ("ID-" joda math_random(1000, 9999));
    }
}

likho("New ID: ", Utility.generateId()); // Output: New ID: ID-XXXX (random number)
```

## 3. Error Handling (`try`, `catch`, `finally`, `throw`)

Codesi provides robust mechanisms to handle errors gracefully, preventing your program from crashing unexpectedly.

### `try...catch...finally` Block

```codesi
karya safeDivide(numerator, denominator) {
    try {
        agar (denominator barabar 0) {
            throw { message: "Division by zero is not allowed." };
        }
        vapas (numerator bhag denominator);
    }
    catch (error) {
        likho("Error in safeDivide: ", error.message);
        vapas (khaali); // Return null on error
    }
    finally {
        likho("Division attempt completed.");
    }
}

likho("Result 1: ", safeDivide(10, 2)); // Output: Division attempt completed.
                                     // Output: Result 1: 5.0

likho("Result 2: ", safeDivide(10, 0)); // Output: Error in safeDivide: Division by zero is not allowed.
                                     // Output: Division attempt completed.
                                     // Output: Result 2: khaali
```

### `throw` Statement

You can explicitly `throw` an error using any value, typically an object with a `message` property.

```codesi
karya validateInput(value) {
    agar (value chota 0) {
        throw { code: 400, message: "Input value cannot be negative." };
    }
    vapas (sach);
}

try {
    validateInput(-10);
}
catch (e) {
    likho("Validation Failed: ", e.code, " - ", e.message);
}
// Output: Validation Failed: 400 - Input value cannot be negative.
```

## 4. Working with Arrays and Objects

### Array Methods

Codesi arrays come with several built-in methods for common operations.

*   **`push(element)`**: Adds an element to the end of the array.
*   **`pop()`**: Removes and returns the last element.
*   **`shift()`**: Removes and returns the first element.
*   **`unshift(element)`**: Adds an element to the beginning of the array.
*   **`lambai`**: Property to get the length of the array.
*   **`map(callback)`**: Creates a new array by calling a provided function on every element.
*   **`filter(callback)`**: Creates a new array with all elements that pass the test implemented by the provided function.
*   **`join(separator)`**: Joins all elements of an array into a string.
*   **`slice(start, end)`**: Returns a shallow copy of a portion of an array into a new array.
*   **`reverse()`**: Reverses the order of the elements in an array.
*   **`sort()`**: Sorts the elements of an array.
*   **`reduce(callback, initialValue)`**: Executes a reducer function on each element of the array, resulting in a single output value.

```codesi
const numbers = [1, 2, 3];
numbers.push(4);
likho(numbers); // Output: [1, 2, 3, 4]

const doubled = numbers.map(lambda (num) -> num guna 2);
likho(doubled); // Output: [2, 4, 6, 8]

const even = numbers.filter(lambda (num) -> num modulo 2 barabar 0);
likho(even);    // Output: [2, 4]

const sum = numbers.reduce(lambda (acc, num) -> acc joda num, 0);
likho("Sum: ", sum); // Output: Sum: 10
```

### Object Methods

Codesi objects also provide utility methods.

*   **`keys()`**: Returns an array of a given object's own enumerable property names.
*   **`values()`**: Returns an array of a given object's own enumerable property values.
*   **`items()`**: Returns an array of `[key, value]` pairs for a given object.
*   **`hai_kya(key)`**: Checks if an object has a specified key.

```codesi
const person = { name: "Alice", age: 30 };
likho(person.keys());   // Output: ["name", "age"]
likho(person.values()); // Output: ["Alice", 30]
likho(person.items());  // Output: [["name", "Alice"], ["age", 30]]
likho(person.hai_kya("name")); // Output: sach
```

## 5. File I/O Operations

Codesi provides built-in functions for reading from and writing to files, enabling your programs to interact with the file system.

```codesi
const filePath = "my_data.txt";

// Write to a file
file_likho(filePath, "Hello from Codesi file!");
likho("File written.");

// Read from a file
const content = file_padho(filePath);
likho("File content: ", content);

// Append to a file
file_append(filePath, "\nThis is appended text.");
likho("Text appended.");

// Check if file exists
likho("File exists: ", file_hai(filePath)); // Output: File exists: sach

// Delete the file
file_delete(filePath);
likho("File deleted.");
```

## What's Next?

You've now covered the intermediate aspects of Codesi. To explore the most powerful and unique features of Codesi, proceed to the [Complete Advanced Guide](COMPLETE_ADVANCED.md) and [Advanced Features Guide](ADVANCED_FEATURES.md)
