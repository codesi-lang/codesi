# Complete Advanced - Week 3 Learning Path

Advanced guide to Codesi Programming Language - Master OOP and build real applications.

## 🎯 Learning Goals

By the end of this week, you will:
- ✅ Master Object-Oriented Programming
- ✅ Build classes with inheritance
- ✅ Use static methods and properties
- ✅ Create recursive algorithms
- ✅ Build complete applications
- ✅ Use advanced Codesi features

**Time Required**: 7 days, 3-4 hours per day

**Prerequisites**: Complete Week 1 & Week 2

---

## 📅 Day 15: Classes - Part 1

### Morning Session (1.5 hours)

#### 1. Basic Class
```codesi
class Person {
    banao(naam, umra) {
        ye.naam = naam
        ye.umra = umra
    }
    
    karya introduce() {
        likho("Namaste! Mera naam", ye.naam, "hai")
        likho("Main", ye.umra, "saal ka/ki hun")
    }
    
    karya birthday() {
        ye.umra = ye.umra + 1
        likho("🎂 Happy Birthday!")
        likho("Ab aap", ye.umra, "saal ke ho!")
    }
}

// Create objects
person1 = new Person("Rishaank", 15)
person1.introduce()
person1.birthday()

person2 = new Person("Priya", 20)
person2.introduce()
```

#### 2. Class with Methods
```codesi
class BankAccount {
    banao(account_number, initial_balance) {
        ye.account_number = account_number
        ye.balance = initial_balance
        ye.transactions = []
    }
    
    karya deposit(amount) {
        ye.balance = ye.balance + amount
        ye.transactions.push({
            type: "Deposit",
            amount: amount,
            balance: ye.balance
        })
        likho("✅ Deposited:", amount)
    }
    
    karya withdraw(amount) {
        agar (amount > ye.balance) {
            likho("❌ Insufficient balance")
            vapas
        }
        
        ye.balance = ye.balance - amount
        ye.transactions.push({
            type: "Withdraw",
            amount: amount,
            balance: ye.balance
        })
        likho("✅ Withdrawn:", amount)
    }
    
    karya show_balance() {
        likho("Current Balance:", ye.balance)
    }
    
    karya show_history() {
        likho("\n📜 Transaction History:")
        har t mein ye.transactions {
            likho("-", t.type, ":", t.amount, "(Balance:", t.balance, ")")
        }
    }
}

// Usage
account = new BankAccount("ACC001", 1000)
account.show_balance()
account.deposit(500)
account.withdraw(200)
account.show_balance()
account.show_history()
```

### Afternoon Session (2 hours)

#### Practice Exercise
Create `day15_student_class.cds`:
```codesi
// Student Management with Classes

class Student {
    banao(naam, roll, class_name) {
        ye.naam = naam
        ye.roll = roll
        ye.class_name = class_name
        ye.marks = {}
        ye.attendance = 0
    }
    
    karya add_marks(subject, marks) {
        ye.marks[subject] = marks
        likho("✅ Marks added for", subject)
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
    
    karya display_report() {
        likho("\n" + "=" * 40)
        likho("Student Report Card")
        likho("=" * 40)
        likho("Name:", ye.naam)
        likho("Roll:", ye.roll)
        likho("Class:", ye.class_name)
        likho("\nMarks:")
        
        har subject mein ye.marks {
            likho("  ", subject, ":", ye.marks[subject])
        }
        
        likho("\nAverage:", ye.calculate_average())
        likho("Grade:", ye.get_grade())
        likho("Attendance:", ye.attendance, "%")
        likho("=" * 40)
    }
}

// Create students
student1 = new Student("Rishaank", 101, "10th")
student1.add_marks("Math", 95)
student1.add_marks("Science", 88)
student1.add_marks("English", 92)
student1.attendance = 95

student2 = new Student("Priya", 102, "10th")
student2.add_marks("Math", 98)
student2.add_marks("Science", 95)
student2.add_marks("English", 90)
student2.attendance = 98

// Display reports
student1.display_report()
student2.display_report()
```

---

## 📅 Day 16: Inheritance

### Morning Session (1.5 hours)

#### 1. Basic Inheritance
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
        // Override parent method
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

#### 2. Multi-Level Inheritance
```codesi
// Level 1
class Vehicle {
    banao(brand) {
        ye.brand = brand
    }
    
    karya start() {
        likho(ye.brand, "started")
    }
}

// Level 2
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

// Level 3
class ElectricCar extends Car {
    banao(brand, model, battery) {
        super.banao(brand, model)
        ye.battery = battery
        ye.type = "Electric"
    }
    
    karya charge() {
        likho("Charging", ye.brand, ye.model)
    }
    
    karya show_specs() {
        likho("Brand:", ye.brand)
        likho("Model:", ye.model)
        likho("Battery:", ye.battery, "kWh")
        likho("Type:", ye.type)
    }
}

tesla = new ElectricCar("Tesla", "Model 3", 75)
tesla.start()        // Tesla started (from Vehicle)
tesla.display()      // Car: Tesla Model 3 (from Car)
tesla.charge()       // Charging Tesla Model 3
tesla.show_specs()   // Show all specs
```

### Afternoon Session (2 hours)

#### Practice Exercise
Create `day16_employee_system.cds`:
```codesi
// Employee Management System with Inheritance

class Person {
    banao(naam, umra) {
        ye.naam = naam
        ye.umra = umra
    }
    
    karya introduce() {
        likho("Name:", ye.naam)
        likho("Age:", ye.umra)
    }
}

class Employee extends Person {
    banao(naam, umra, employee_id, department) {
        super.banao(naam, umra)
        ye.employee_id = employee_id
        ye.department = department
        ye.salary = 0
    }
    
    karya set_salary(amount) {
        ye.salary = amount
    }
    
    karya display_info() {
        ye.introduce()
        likho("Employee ID:", ye.employee_id)
        likho("Department:", ye.department)
        likho("Salary:", ye.salary)
    }
}

class Manager extends Employee {
    banao(naam, umra, employee_id, department) {
        super.banao(naam, umra, employee_id, department)
        ye.team = []
        ye.bonus = 0
    }
    
    karya add_team_member(employee) {
        ye.team.push(employee)
        likho("✅ Added", employee.naam, "to team")
    }
    
    karya show_team() {
        likho("\nTeam Members:")
        har member mein ye.team {
            likho("-", member.naam, "(", member.department, ")")
        }
    }
    
    karya calculate_total_compensation() {
        vapas ye.salary + ye.bonus
    }
}

// Create employees
emp1 = new Employee("Raj", 28, "E001", "Engineering")
emp1.set_salary(50000)

emp2 = new Employee("Priya", 26, "E002", "Engineering")
emp2.set_salary(48000)

// Create manager
manager = new Manager("Amit", 35, "M001", "Engineering")
manager.set_salary(80000)
manager.bonus = 20000
manager.add_team_member(emp1)
manager.add_team_member(emp2)

// Display info
likho("\n--- Employee Info ---")
emp1.display_info()

likho("\n--- Manager Info ---")
manager.display_info()
likho("Total Compensation:", manager.calculate_total_compensation())
manager.show_team()
```

---

## 📅 Day 17: Static Methods & Advanced OOP

### Morning Session (1.5 hours)

#### 1. Static Methods
```codesi
class MathHelper {
    static karya add(a, b) {
        vapas a + b
    }
    
    static karya multiply(a, b) {
        vapas a * b
    }
    
    static karya factorial(n) {
        agar (n <= 1) vapas 1
        vapas n * MathHelper.factorial(n - 1)
    }
}

// Call without creating instance
likho(MathHelper.add(5, 3))        // 8
likho(MathHelper.multiply(4, 5))   // 20
likho(MathHelper.factorial(5))     // 120
```

#### 2. Utility Classes
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
    
    static karya capitalize_words(text) {
        words = text.todo(" ")
        result = []
        
        har word mein words {
            agar (word.lambai() > 0) {
                first = word[0].bada_karo()
                rest = word.slice(1)
                result.push(first + rest)
            }
        }
        
        vapas result.join(" ")
    }
}

likho(StringUtils.reverse("hello"))
likho(StringUtils.is_palindrome("radar"))
likho(StringUtils.capitalize_words("hello world"))
```

### Afternoon Session (2 hours)

#### Practice Exercise
Create `day17_library_system.cds`:
```codesi
// Library Management System

class Book {
    banao(id, title, author, copies) {
        ye.id = id
        ye.title = title
        ye.author = author
        ye.total_copies = copies
        ye.available_copies = copies
    }
    
    karya is_available() {
        vapas ye.available_copies > 0
    }
    
    karya borrow() {
        agar (!ye.is_available()) {
            vapas jhooth
        }
        ye.available_copies = ye.available_copies - 1
        vapas sach
    }
    
    karya return_book() {
        agar (ye.available_copies < ye.total_copies) {
            ye.available_copies = ye.available_copies + 1
            vapas sach
        }
        vapas jhooth
    }
}

class Member {
    banao(id, naam) {
        ye.id = id
        ye.naam = naam
        ye.borrowed_books = []
    }
    
    karya borrow_book(book) {
        agar (book.borrow()) {
            ye.borrowed_books.push(book)
            likho("✅", ye.naam, "borrowed", book.title)
            vapas sach
        }
        likho("❌ Book not available")
        vapas jhooth
    }
    
    karya return_book(book) {
        // Find book in borrowed list
        index = -1
        har i se 0 tak ye.borrowed_books.lambai() {
            agar (ye.borrowed_books[i].id == book.id) {
                index = i
                break
            }
        }
        
        agar (index >= 0) {
            book.return_book()
            // Remove from borrowed list
            new_list = []
            har i se 0 tak ye.borrowed_books.lambai() {
                agar (i != index) {
                    new_list.push(ye.borrowed_books[i])
                }
            }
            ye.borrowed_books = new_list
            likho("✅", ye.naam, "returned", book.title)
            vapas sach
        }
        
        likho("❌ Book not borrowed by this member")
        vapas jhooth
    }
    
    karya show_borrowed() {
        agar (ye.borrowed_books.lambai() == 0) {
            likho(ye.naam, "has no borrowed books")
            vapas
        }
        
        likho("\n", ye.naam, "'s Borrowed Books:")
        har book mein ye.borrowed_books {
            likho("-", book.title, "by", book.author)
        }
    }
}

class Library {
    static books = []
    static members = []
    
    static karya add_book(book) {
        Library.books.push(book)
        likho("✅ Book added:", book.title)
    }
    
    static karya add_member(member) {
        Library.members.push(member)
        likho("✅ Member added:", member.naam)
    }
    
    static karya show_available_books() {
        likho("\n📚 Available Books:")
        har book mein Library.books {
            agar (book.is_available()) {
                likho("-", book.title, "by", book.author)
                likho("  Available:", book.available_copies, "/", book.total_copies)
            }
        }
    }
}

// Setup library
book1 = new Book(1, "Codesi Guide", "Rishaank", 3)
book2 = new Book(2, "Python Basics", "Author2", 2)
book3 = new Book(3, "Web Development", "Author3", 1)

Library.add_book(book1)
Library.add_book(book2)
Library.add_book(book3)

member1 = new Member(101, "Raj")
member2 = new Member(102, "Priya")

Library.add_member(member1)
Library.add_member(member2)

// Transactions
member1.borrow_book(book1)
member1.borrow_book(book2)
member2.borrow_book(book1)

Library.show_available_books()

member1.show_borrowed()
member2.show_borrowed()

member1.return_book(book1)
Library.show_available_books()
```

---

## 📅 Day 18: Recursion

### Morning Session (1.5 hours)

#### 1. Simple Recursion
```codesi
// Countdown
karya countdown(n) {
    agar (n <= 0) {
        likho("Blast off!")
        vapas
    }
    likho(n)
    countdown(n - 1)
}

countdown(5)

// Factorial
karya factorial(n) {
    agar (n <= 1) vapas 1
    vapas n * factorial(n - 1)
}

likho("Factorial of 5:", factorial(5))
```

#### 2. Fibonacci
```codesi
karya fibonacci(n) {
    agar (n <= 1) vapas n
    vapas fibonacci(n - 1) + fibonacci(n - 2)
}

// Generate sequence
likho("Fibonacci Sequence:")
har i se 0 tak 10 {
    likho("F(", i, ") =", fibonacci(i))
}
```

### Afternoon Session (2 hours)

#### 3. Advanced Recursion
```codesi
// Sum of digits
karya sum_digits(n) {
    agar (n < 10) vapas n
    vapas (n % 10) + sum_digits(math_niche(n / 10))
}

likho("Sum of digits in 12345:", sum_digits(12345))  // 15

// Power function
karya power(base, exp) {
    agar (exp == 0) vapas 1
    agar (exp == 1) vapas base
    vapas base * power(base, exp - 1)
}

likho("2^10 =", power(2, 10))

// Array sum
karya array_sum(arr, index = 0) {
    agar (index >= arr.lambai()) vapas 0
    vapas arr[index] + array_sum(arr, index + 1)
}

numbers = [1, 2, 3, 4, 5]
likho("Array sum:", array_sum(numbers))
```

#### Practice Exercise
Create `day18_recursive_algorithms.cds`:
```codesi
// Recursive Algorithms

// 1. GCD (Greatest Common Divisor)
karya gcd(a, b) {
    agar (b == 0) vapas a
    vapas gcd(b, a % b)
}

// 2. Binary Search
karya binary_search(arr, target, left = 0, right = -1) {
    agar (right == -1) {
        right = arr.lambai() - 1
    }
    
    agar (left > right) {
        vapas -1  // Not found
    }
    
    mid = math_niche((left + right) / 2)
    
    agar (arr[mid] == target) {
        vapas mid
    } ya_phir (arr[mid] > target) {
        vapas binary_search(arr, target, left, mid - 1)
    } nahi_to {
        vapas binary_search(arr, target, mid + 1, right)
    }
}

// 3. Tower of Hanoi
karya tower_of_hanoi(n, from, to, aux, moves) {
    agar (n == 1) {
        moves.push("Move disk 1 from " + from + " to " + to)
        vapas
    }
    
    tower_of_hanoi(n - 1, from, aux, to, moves)
    moves.push("Move disk " + string_bnao(n) + " from " + from + " to " + to)
    tower_of_hanoi(n - 1, aux, to, from, moves)
}

// Test algorithms
likho("GCD of 48 and 18:", gcd(48, 18))

sorted_array = [1, 3, 5, 7, 9, 11, 13, 15]
likho("Binary search for 7:", binary_search(sorted_array, 7))
likho("Binary search for 10:", binary_search(sorted_array, 10))

moves = []
tower_of_hanoi(3, "A", "C", "B", moves)
likho("\nTower of Hanoi (3 disks):")
har move mein moves {
    likho(move)
}
```

---

## 📅 Day 19: Design Patterns

### Morning Session (1.5 hours)

#### 1. Singleton Pattern
```codesi
class Database {
    static instance = khaali
    
    banao() {
        ye.connected = jhooth
    }
    
    static karya get_instance() {
        agar (Database.instance == khaali) {
            Database.instance = new Database()
        }
        vapas Database.instance
    }
    
    karya connect() {
        ye.connected = sach
        likho("✅ Database connected")
    }
    
    karya query(sql) {
        agar (!ye.connected) {
            likho("❌ Not connected")
            vapas
        }
        likho("Executing:", sql)
    }
}

// Always get same instance
db1 = Database.get_instance()
db2 = Database.get_instance()

db1.connect()
db2.query("SELECT * FROM users")  // Uses same connection
```

#### 2. Factory Pattern
```codesi
class Shape {
    karya area() {
        vapas 0
    }
}

class Circle extends Shape {
    banao(radius) {
        ye.radius = radius
    }
    
    karya area() {
        vapas 3.14159 * ye.radius * ye.radius
    }
}

class Rectangle extends Shape {
    banao(length, width) {
        ye.length = length
        ye.width = width
    }
    
    karya area() {
        vapas ye.length * ye.width
    }
}

class ShapeFactory {
    static karya create_shape(type, ...params) {
        agar (type == "circle") {
            vapas new Circle(params[0])
        } ya_phir (type == "rectangle") {
            vapas new Rectangle(params[0], params[1])
        }
        vapas khaali
    }
}

// Use factory
circle = ShapeFactory.create_shape("circle", 5)
rectangle = ShapeFactory.create_shape("rectangle", 10, 5)

likho("Circle area:", circle.area())
likho("Rectangle area:", rectangle.area())
```

### Afternoon Session (2 hours)

#### Practice Exercise
Create `day19_game_engine.cds`:
```codesi
// Simple Game Engine with Design Patterns

// Component Pattern
class GameObject {
    banao(naam, x, y) {
        ye.naam = naam
        ye.x = x
        ye.y = y
        ye.components = []
    }
    
    karya add_component(component) {
        ye.components.push(component)
    }
    
    karya update() {
        har component mein ye.components {
            component.update(ye)
        }
    }
}

// Components
class MovementComponent {
    banao(speed) {
        ye.speed = speed
    }
    
    karya update(gameObject) {
        // Move logic
        likho(gameObject.naam, "moving at speed", ye.speed)
    }
}

class HealthComponent {
    banao(max_health) {
        ye.max_health = max_health
        ye.current_health = max_health
    }
    
    karya update(gameObject) {
        likho(gameObject.naam, "health:", ye.current_health, "/", ye.max_health)
    }
    
    karya take_damage(amount) {
        ye.current_health = ye.current_health - amount
        agar (ye.current_health < 0) {
            ye.current_health = 0
        }
    }
}

// Game Manager (Singleton)
class GameManager {
    static instance = khaali
    
    banao() {
        ye.game_objects = []
        ye.running = jhooth
    }
    
    static karya get_instance() {
        agar (GameManager.instance == khaali) {
            GameManager.instance = new GameManager()
        }
        vapas GameManager.instance
    }
    
    karya add_game_object(obj) {
        ye.game_objects.push(obj)
    }
    
    karya start() {
        ye.running = sach
        likho("🎮 Game Started!")
    }
    
    karya update() {
        agar (!ye.running) vapas
        
        likho("\n--- Game Update ---")
        har obj mein ye.game_objects {
            obj.update()
        }
    }
}

// Create game
game = GameManager.get_instance()

// Create player
player = new GameObject("Player", 0, 0)
player.add_component(new MovementComponent(5))
player.add_component(new HealthComponent(100))

// Create enemy
enemy = new GameObject("Enemy", 10, 10)
enemy.add_component(new MovementComponent(3))
enemy.add_component(new HealthComponent(50))

game.add_game_object(player)
game.add_game_object(enemy)

game.start()
game.update()
game.update()
```

---

## 📅 Day 20-21: Final Project

### Project: E-Commerce System

Create `week3_project_ecommerce.cds`:

```codesi
// Complete E-Commerce System

// Product Class
class Product {
    banao(id, naam, price, stock) {
        ye.id = id
        ye.naam = naam
        ye.price = price
        ye.stock = stock
        ye.reviews = []
    }
    
    karya is_available() {
        vapas ye.stock > 0
    }
    
    karya reduce_stock(quantity) {
        agar (quantity > ye.stock) vapas jhooth
        ye.stock = ye.stock - quantity
        vapas sach
    }
    
    karya add_review(rating, comment) {
        ye.reviews.push({rating: rating, comment: comment})
    }
    
    karya get_average_rating() {
        agar (ye.reviews.lambai() == 0) vapas 0
        
        total = 0
        har review mein ye.reviews {
            total = total + review.rating
        }
        vapas total / ye.reviews.lambai()
    }
}

// User Class
class User {
    banao(id, naam, email) {
        ye.id = id
        ye.naam = naam
        ye.email = email
        ye.cart = new ShoppingCart()
        ye.orders = []
    }
    
    karya add_to_cart(product, quantity) {
        vapas ye.cart.add_item(product, quantity)
    }
    
    karya checkout() {
        agar (ye.cart.items.lambai() == 0) {
            likho("❌ Cart is empty")
            vapas jhooth
        }
        
        order = new Order(ye.orders.lambai() + 1, ye, ye.cart.items)
        ye.orders.push(order)
        ye.cart.clear()
        
        likho("✅ Order placed successfully!")
        likho("Order ID:", order.id)
        vapas sach
    }
    
    karya show_orders() {
        likho("\n📦 Your Orders:")
        har order mein ye.orders {
            order.display()
        }
    }
}

// Shopping Cart
class ShoppingCart {
    banao() {
        ye.items = []
    }
    
    karya add_item(product, quantity) {
        agar (!product.is_available()) {
            likho("❌ Product out of stock")
            vapas jhooth
        }
        
        ye.items.push({
            product: product,
            quantity: quantity
        })
        likho("✅ Added to cart:", product.naam)
        vapas sach
    }
    
    karya calculate_total() {
        total = 0
        har item mein ye.items {
            total = total + (item.product.price * item.quantity)
        }
        vapas total
    }
    
    karya display() {
        likho("\n🛒 Shopping Cart:")
        agar (ye.items.lambai() == 0) {
            likho("   (Empty)")
            vapas
        }
        
        har item mein ye.items {
            subtotal = item.product.price * item.quantity
            likho("-", item.product.naam)
            likho("  Price:", item.product.price, "x", item.quantity)
            likho("  Subtotal:", subtotal)
        }
        likho("\nTotal:", ye.calculate_total())
    }
    
    karya clear() {
        ye.items = []
    }
}

// Order Class
class Order {
    banao(id, user, items) {
        ye.id = id
        ye.user = user
        ye.items = items
        ye.total = ye.calculate_total()
        ye.status = "Pending"
        ye.date = time_now()
    }
    
    karya calculate_total() {
        total = 0
        har item mein ye.items {
            total = total + (item.product.price * item.quantity)
        }
        vapas total
    }
    
    karya display() {
        likho("\nOrder #", ye.id)
        likho("Status:", ye.status)
        likho("Items:")
        har item mein ye.items {
            likho("-", item.product.naam, "x", item.quantity)
        }
        likho("Total:", ye.total)
    }
}

// Store Class (Singleton)
class Store {
    static instance = khaali
    
    banao() {
        ye.products = []
        ye.users = []
    }
    
    static karya get_instance() {
        agar (Store.instance == khaali) {
            Store.instance = new Store()
        }
        vapas Store.instance
    }
    
    karya add_product(product) {
        ye.products.push(product)
    }
    
    karya add_user(user) {
        ye.users.push(user)
    }
    
    karya show_products() {
        likho("\n🏪 Available Products:")
        har product mein ye.products {
            agar (product.is_available()) {
                likho("\n-", product.naam)
                likho("  Price:", product.price)
                likho("  Stock:", product.stock)
                likho("  Rating:", product.get_average_rating())
            }
        }
    }
}

// Initialize Store
store = Store.get_instance()

// Add products
p1 = new Product(1, "Laptop", 50000, 10)
p2 = new Product(2, "Mouse", 500, 50)
p3 = new Product(3, "Keyboard", 1500, 30)

p1.add_review(5, "Excellent!")
p1.add_review(4, "Good product")

store.add_product(p1)
store.add_product(p2)
store.add_product(p3)

// Create user
user = new User(1, "Rishaank", "rishaank@codesi.dev")
store.add_user(user)

// Shopping flow
store.show_products()

user.add_to_cart(p1, 1)
user.add_to_cart(p2, 2)
user.add_to_cart(p3, 1)

user.cart.display()

user.checkout()

user.show_orders()

likho("\n✅ E-Commerce System Demo Complete!")
```

---

## 📊 Week 3 Checklist

### Advanced Concepts Mastered
- [ ] Classes and objects
- [ ] Inheritance (single and multi-level)
- [ ] Method overriding
- [ ] Static methods
- [ ] Design patterns
- [ ] Recursion
- [ ] Complex applications

### Projects Completed
- [ ] Student management
- [ ] Employee system
- [ ] Library management
- [ ] Recursive algorithms
- [ ] Game engine basics
- [ ] E-commerce system

---

## 🎉 Congratulations!

You've completed the 3-week Codesi learning path!

### What You've Learned
- ✅ All programming basics
- ✅ Data structures (arrays, objects)
- ✅ Functions (including lambda)
- ✅ Object-Oriented Programming
- ✅ File operations
- ✅ Error handling
- ✅ Real-world applications

### Next Steps
1. **Explore Advanced Features**: [ADVANCED_FEATURES.md](ADVANCED_FEATURES.md)
2. **Build Your Own Projects**
3. **Contribute to Codesi**
4. **Help Others Learn**

---

**You're now a Codesi Developer! 🚀**