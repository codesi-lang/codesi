# Object-Oriented Programming in Codesi

Complete guide to OOP concepts in Codesi Programming Language.

## 📋 Table of Contents

- [Introduction to OOP](#introduction-to-oop)
- [Classes and Objects](#classes-and-objects)
- [Constructors](#constructors)
- [Methods](#methods)
- [Properties](#properties)
- [Inheritance](#inheritance)
- [Static Methods](#static-methods)
- [The 'ye' Keyword](#the-ye-keyword)
- [Real-World Examples](#real-world-examples)

---

## 🌟 Introduction to OOP

Object-Oriented Programming helps organize code by grouping related data and functions together.

### Why OOP?

```codesi
// Without OOP - scattered data
student1_naam = "Raj"
student1_roll = 101
student1_marks = 85

student2_naam = "Priya"
student2_roll = 102
student2_marks = 92

// With OOP - organized
class Student {
    banao(naam, roll, marks) {
        ye.naam = naam
        ye.roll = roll
        ye.marks = marks
    }
}

student1 = new Student("Raj", 101, 85)
student2 = new Student("Priya", 102, 92)
```

---

## 🏗️ Classes and Objects

### Defining a Class

```codesi
class ClassName {
    // Constructor
    banao(parameters) {
        // Initialize properties
    }
    
    // Methods
    karya method_name() {
        // Method code
    }
}
```

### Basic Example

```codesi
class Person {
    banao(naam, umra) {
        ye.naam = naam
        ye.umra = umra
    }
    
    karya introduce() {
        likho("Mera naam", ye.naam, "hai")
        likho("Main", ye.umra, "saal ka/ki hun")
    }
}

// Create object (instance)
person1 = new Person("Rishaank", 15)
person1.introduce()

person2 = new Person("Priya", 20)
person2.introduce()
```

---

## 🔧 Constructors

The `banao` method is the constructor - called when creating an object.

### Simple Constructor

```codesi
class Book {
    banao(title, author) {
        ye.title = title
        ye.author = author
        ye.pages = 0  // Default value
    }
}

book = new Book("Codesi Guide", "Rishaank")
```

### Constructor with Default Values

```codesi
class User {
    banao(naam, email, role = "member") {
        ye.naam = naam
        ye.email = email
        ye.role = role
        ye.created_at = time_now()
    }
}

admin = new User("Admin", "admin@site.com", "admin")
user = new User("Raj", "raj@site.com")  // Uses default role
```

### Constructor with Validation

```codesi
class BankAccount {
    banao(account_number, initial_balance) {
        agar (initial_balance < 0) {
            throw {message: "Balance cannot be negative"}
        }
        
        ye.account_number = account_number
        ye.balance = initial_balance
        ye.transactions = []
    }
}

try {
    account = new BankAccount("ACC001", 1000)
    likho("Account created successfully")
} catch (e) {
    likho("Error:", e.message)
}
```

---

## 📦 Methods

Methods are functions inside a class.

### Instance Methods

```codesi
class Calculator {
    banao() {
        ye.history = []
    }
    
    karya add(a, b) {
        result = a + b
        ye.history.push("Added: " + string_bnao(result))
        vapas result
    }
    
    karya subtract(a, b) {
        result = a - b
        ye.history.push("Subtracted: " + string_bnao(result))
        vapas result
    }
    
    karya show_history() {
        likho("Calculation History:")
        har entry mein ye.history {
            likho("-", entry)
        }
    }
}

calc = new Calculator()
calc.add(10, 5)
calc.subtract(20, 8)
calc.show_history()
```

### Methods with Return Values

```codesi
class Rectangle {
    banao(length, width) {
        ye.length = length
        ye.width = width
    }
    
    karya area() {
        vapas ye.length * ye.width
    }
    
    karya perimeter() {
        vapas 2 * (ye.length + ye.width)
    }
    
    karya is_square() {
        vapas ye.length == ye.width
    }
}

rect = new Rectangle(10, 5)
likho("Area:", rect.area())           // 50
likho("Perimeter:", rect.perimeter()) // 30
likho("Is square?", rect.is_square()) // jhooth
```

### Method Chaining

```codesi
class Counter {
    banao() {
        ye.count = 0
    }
    
    karya increment() {
        ye.count = ye.count + 1
        vapas ye  // Return self for chaining
    }
    
    karya decrement() {
        ye.count = ye.count - 1
        vapas ye
    }
    
    karya reset() {
        ye.count = 0
        vapas ye
    }
    
    karya get_value() {
        vapas ye.count
    }
}

counter = new Counter()
counter.increment().increment().increment().decrement()
likho(counter.get_value())  // 2
```

---

## 🎯 Properties

Properties are variables that belong to an object.

### Public Properties

```codesi
class Student {
    banao(naam, roll) {
        ye.naam = naam
        ye.roll = roll
        ye.marks = {}
        ye.attendance = 0
    }
    
    karya add_marks(subject, marks) {
        ye.marks[subject] = marks
    }
}

student = new Student("Raj", 101)
student.add_marks("Math", 95)

// Access properties
likho(student.naam)      // "Raj"
likho(student.roll)      // 101
likho(student.marks)     // {Math: 95}

// Modify properties
student.attendance = 85
```

### Computed Properties (Getters)

```codesi
class Circle {
    banao(radius) {
        ye.radius = radius
    }
    
    karya get_area() {
        vapas 3.14159 * ye.radius * ye.radius
    }
    
    karya get_circumference() {
        vapas 2 * 3.14159 * ye.radius
    }
    
    karya get_diameter() {
        vapas 2 * ye.radius
    }
}

circle = new Circle(5)
likho("Area:", circle.get_area())                 // 78.54
likho("Circumference:", circle.get_circumference()) // 31.42
```

---

## 🔗 Inheritance

Child classes inherit properties and methods from parent classes.

### Basic Inheritance

```codesi
// Parent class
class Animal {
    banao(naam) {
        ye.naam = naam
    }
    
    karya speak() {
        likho(ye.naam, "makes a sound")
    }
    
    karya info() {
        likho("Animal:", ye.naam)
    }
}

// Child class
class Dog extends Animal {
    banao(naam, breed) {
        super.banao(naam)  // Call parent constructor
        ye.breed = breed
    }
    
    karya speak() {
        likho(ye.naam, "barks: Woof!")
    }
    
    karya show_breed() {
        likho("Breed:", ye.breed)
    }
}

dog = new Dog("Tommy", "Labrador")
dog.speak()        // Tommy barks: Woof!
dog.info()         // Animal: Tommy (inherited)
dog.show_breed()   // Breed: Labrador
```

### Multi-Level Inheritance

```codesi
// Level 1: Base class
class Vehicle {
    banao(brand) {
        ye.brand = brand
    }
    
    karya start() {
        likho(ye.brand, "vehicle started")
    }
}

// Level 2: Intermediate class
class Car extends Vehicle {
    banao(brand, model) {
        super.banao(brand)
        ye.model = model
        ye.doors = 4
    }
    
    karya display() {
        likho("Car:", ye.brand, ye.model)
    }
}

// Level 3: Specialized class
class ElectricCar extends Car {
    banao(brand, model, battery_capacity) {
        super.banao(brand, model)
        ye.battery_capacity = battery_capacity
        ye.fuel_type = "Electric"
    }
    
    karya charge() {
        likho("Charging", ye.brand, ye.model)
    }
}

tesla = new ElectricCar("Tesla", "Model 3", 75)
tesla.start()      // Tesla vehicle started (from Vehicle)
tesla.display()    // Car: Tesla Model 3 (from Car)
tesla.charge()     // Charging Tesla Model 3 (from ElectricCar)
```

### Method Overriding

```codesi
class Shape {
    banao(naam) {
        ye.naam = naam
    }
    
    karya area() {
        vapas 0  // Default implementation
    }
    
    karya describe() {
        likho("This is a", ye.naam)
    }
}

class Square extends Shape {
    banao(side) {
        super.banao("Square")
        ye.side = side
    }
    
    karya area() {
        // Override parent method
        vapas ye.side * ye.side
    }
}

class Circle extends Shape {
    banao(radius) {
        super.banao("Circle")
        ye.radius = radius
    }
    
    karya area() {
        // Override parent method
        vapas 3.14159 * ye.radius * ye.radius
    }
}

square = new Square(5)
circle = new Circle(3)

likho(square.area())  // 25
likho(circle.area())  // 28.27
```

---

## ⚡ Static Methods

Static methods belong to the class, not instances.

### Defining Static Methods

```codesi
class MathHelper {
    static karya add(a, b) {
        vapas a + b
    }
    
    static karya multiply(a, b) {
        vapas a * b
    }
    
    static karya square(x) {
        vapas x * x
    }
}

// Call without creating instance
result = MathHelper.add(5, 3)
likho(result)  // 8

likho(MathHelper.multiply(4, 5))  // 20
likho(MathHelper.square(7))       // 49
```

### Utility Classes

```codesi
class StringUtils {
    static karya reverse(text) {
        reversed = ""
        har i se text.lambai() - 1 tak -1 {
            reversed = reversed + text[i]
        }
        vapas reversed
    }
    
    static karya is_palindrome(text) {
        clean = text.chota_karo()
        vapas clean == StringUtils.reverse(clean)
    }
    
    static karya count_vowels(text) {
        vowels = "aeiouAEIOU"
        count = 0
        har char mein text {
            agar (vowels.included_hai(char)) {
                count = count + 1
            }
        }
        vapas count
    }
}

likho(StringUtils.reverse("hello"))           // "olleh"
likho(StringUtils.is_palindrome("radar"))     // sach
likho(StringUtils.count_vowels("education"))  // 5
```

---

## 👤 The 'ye' Keyword

`ye` is like `this` or `self` - refers to current object instance.

### Accessing Properties

```codesi
class Person {
    banao(naam, umra) {
        ye.naam = naam  // 'ye' refers to current object
        ye.umra = umra
    }
    
    karya birthday() {
        ye.umra = ye.umra + 1  // Modify own property
    }
    
    karya introduce() {
        // Access own properties
        likho("Main", ye.naam, "hun")
        likho("Meri umra", ye.umra, "saal hai")
    }
}
```

### 'ye' in Methods

```codesi
class BankAccount {
    banao(balance) {
        ye.balance = balance
        ye.transactions = []
    }
    
    karya deposit(amount) {
        ye.balance = ye.balance + amount
        ye.log_transaction("Deposit", amount)
    }
    
    karya withdraw(amount) {
        agar (amount > ye.balance) {
            likho("Insufficient balance")
            vapas
        }
        ye.balance = ye.balance - amount
        ye.log_transaction("Withdraw", amount)
    }
    
    karya log_transaction(type, amount) {
        ye.transactions.push({
            type: type,
            amount: amount,
            balance: ye.balance
        })
    }
}
```

---

## 🌍 Real-World Examples

### Example 1: School Management System

```codesi
class Person {
    banao(naam, umra) {
        ye.naam = naam
        ye.umra = umra
    }
    
    karya introduce() {
        likho("Namaste! Main", ye.naam, "hun")
    }
}

class Student extends Person {
    banao(naam, umra, roll_number, class_name) {
        super.banao(naam, umra)
        ye.roll_number = roll_number
        ye.class_name = class_name
        ye.marks = {}
        ye.attendance = 0
    }
    
    karya add_marks(subject, marks) {
        ye.marks[subject] = marks
    }
    
    karya calculate_average() {
        agar (ye.marks.keys().lambai() == 0) {
            vapas 0
        }
        
        total = 0
        har subject mein ye.marks {
            total = total + ye.marks[subject]
        }
        vapas total / ye.marks.keys().lambai()
    }
    
    karya get_grade() {
        avg = ye.calculate_average()
        agar (avg >= 90) vapas "A+"
        agar (avg >= 80) vapas "A"
        agar (avg >= 70) vapas "B"
        agar (avg >= 60) vapas "C"
        vapas "D"
    }
}

class Teacher extends Person {
    banao(naam, umra, subject, employee_id) {
        super.banao(naam, umra)
        ye.subject = subject
        ye.employee_id = employee_id
        ye.students = []
    }
    
    karya add_student(student) {
        ye.students.push(student)
    }
    
    karya show_students() {
        likho("\n📚", ye.subject, "Teacher:", ye.naam)
        likho("Students:")
        har student mein ye.students {
            likho("-", student.naam, "(Roll:", student.roll_number, ")")
        }
    }
}

// Usage
student1 = new Student("Rishaank", 15, 101, "10th")
student1.add_marks("Math", 95)
student1.add_marks("Science", 88)
student1.add_marks("English", 92)

student2 = new Student("Priya", 15, 102, "10th")
student2.add_marks("Math", 98)
student2.add_marks("Science", 95)

teacher = new Teacher("Sharma Sir", 35, "Mathematics", "T001")
teacher.add_student(student1)
teacher.add_student(student2)

likho("Student:", student1.naam)
likho("Average:", student1.calculate_average())
likho("Grade:", student1.get_grade())

teacher.show_students()
```

### Example 2: E-Commerce System

```codesi
class Product {
    banao(id, naam, price, stock) {
        ye.id = id
        ye.naam = naam
        ye.price = price
        ye.stock = stock
    }
    
    karya is_available() {
        vapas ye.stock > 0
    }
    
    karya reduce_stock(quantity) {
        agar (quantity > ye.stock) {
            vapas jhooth
        }
        ye.stock = ye.stock - quantity
        vapas sach
    }
}

class Cart {
    banao() {
        ye.items = []
    }
    
    karya add_item(product, quantity) {
        agar (!product.is_available()) {
            likho("Product out of stock")
            vapas
        }
        
        ye.items.push({
            product: product,
            quantity: quantity
        })
        likho("Added", product.naam, "to cart")
    }
    
    karya calculate_total() {
        total = 0
        har item mein ye.items {
            total = total + (item.product.price * item.quantity)
        }
        vapas total
    }
    
    karya show_cart() {
        likho("\n🛒 Shopping Cart:")
        har item mein ye.items {
            likho("-", item.product.naam)
            likho("  Price:", item.product.price)
            likho("  Quantity:", item.quantity)
            likho("  Subtotal:", item.product.price * item.quantity)
        }
        likho("\nTotal:", ye.calculate_total())
    }
}

// Usage
laptop = new Product(1, "Laptop", 50000, 10)
mouse = new Product(2, "Mouse", 500, 50)
keyboard = new Product(3, "Keyboard", 1500, 30)

cart = new Cart()
cart.add_item(laptop, 1)
cart.add_item(mouse, 2)
cart.add_item(keyboard, 1)
cart.show_cart()
```

### Example 3: Game Character System

```codesi
class Character {
    banao(naam) {
        ye.naam = naam
        ye.health = 100
        ye.level = 1
        ye.experience = 0
    }
    
    karya take_damage(damage) {
        ye.health = ye.health - damage
        agar (ye.health < 0) {
            ye.health = 0
        }
        likho(ye.naam, "took", damage, "damage. Health:", ye.health)
    }
    
    karya heal(amount) {
        ye.health = ye.health + amount
        agar (ye.health > 100) {
            ye.health = 100
        }
        likho(ye.naam, "healed", amount, ". Health:", ye.health)
    }
    
    karya gain_exp(exp) {
        ye.experience = ye.experience + exp
        likho("Gained", exp, "XP")
        ye.check_level_up()
    }
    
    karya check_level_up() {
        required_exp = ye.level * 100
        agar (ye.experience >= required_exp) {
            ye.level = ye.level + 1
            ye.experience = ye.experience - required_exp
            likho("🎉 Level Up! Now level", ye.level)
        }
    }
    
    karya is_alive() {
        vapas ye.health > 0
    }
}

class Warrior extends Character {
    banao(naam) {
        super.banao(naam)
        ye.strength = 15
        ye.armor = 10
    }
    
    karya attack() {
        damage = ye.strength + (ye.level * 5)
        likho("⚔️", ye.naam, "attacks for", damage, "damage!")
        vapas damage
    }
    
    karya defend() {
        reduction = ye.armor + (ye.level * 2)
        likho("🛡️", ye.naam, "defends, reducing", reduction, "damage")
        vapas reduction
    }
}

class Mage extends Character {
    banao(naam) {
        super.banao(naam)
        ye.mana = 100
        ye.magic_power = 20
    }
    
    karya cast_spell() {
        agar (ye.mana < 20) {
            likho("Not enough mana!")
            vapas 0
        }
        
        ye.mana = ye.mana - 20
        damage = ye.magic_power + (ye.level * 8)
        likho("✨", ye.naam, "casts spell for", damage, "damage!")
        vapas damage
    }
    
    karya restore_mana(amount) {
        ye.mana = ye.mana + amount
        agar (ye.mana > 100) {
            ye.mana = 100
        }
    }
}

// Game simulation
warrior = new Warrior("Bheem")
mage = new Mage("Gandalf")

likho("⚔️  Battle Begins!")
likho()

// Turn 1
damage = warrior.attack()
mage.take_damage(damage)

// Turn 2
spell_damage = mage.cast_spell()
warrior.take_damage(spell_damage)

// Level up
warrior.gain_exp(150)

likho()
likho("Warrior Health:", warrior.health)
likho("Mage Health:", mage.health)
```

---

## 📚 Summary

### OOP Concepts in Codesi

| Concept | Keyword | Purpose |
|---------|---------|---------|
| Class | `class` | Define blueprint |
| Constructor | `banao` | Initialize object |
| Instance | `new` | Create object |
| Method | `karya` | Class function |
| Inheritance | `extends` | Inherit from parent |
| Super | `super` | Access parent |
| Self Reference | `ye` | Current object |
| Static | `static` | Class-level method |

### Key Takeaways

1. **Classes** organize related data and functions
2. **Objects** are instances of classes
3. **Inheritance** promotes code reuse
4. **Methods** define object behavior
5. **Properties** store object data
6. **'ye'** refers to current instance
7. **Static methods** don't need instances

---

**Next**: [Functions Guide](FUNCTIONS.md)