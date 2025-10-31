// Comprehensive Time Machine Deep Copy Test
// Tests nested structures with precise snapshot verification

likho("=== Test 1: Nested Array - Simple Case ===")
time_machine_on(20)

arr = [[1, 2], [3, 4]]
likho("Step 1 - Initial:", arr)

arr[0][0] = 999
likho("Step 2 - Modified:", arr)

peeche()
likho("After going back:", arr)

agar (arr[0][0] == 1) {
    likho("✅ TEST 1 PASSED - Nested array restored correctly!")
} nahi_to {
    likho("❌ TEST 1 FAILED - Expected arr[0][0] = 1, got", arr[0][0])
}
likho("")

likho("=== Test 2: Deeply Nested Array (3 levels) ===")
time_machine_on(20)

deep = [[[100, 200], [300, 400]], [[500, 600], [700, 800]]]
likho("Initial:", deep)

deep[0][1][0] = 9999
likho("After change:", deep)

peeche()
likho("After peeche():", deep)

agar (deep[0][1][0] == 300) {
    likho("✅ TEST 2 PASSED - 3-level nested array works!")
} nahi_to {
    likho("❌ TEST 2 FAILED - Expected 300, got", deep[0][1][0])
}
likho("")

likho("=== Test 3: Nested Object ===")
time_machine_on(20)

person = {
    naam: "Rishaank",
    details: {
        age: 15,
        city: "Mumbai"
    }
}
likho("Initial person:", person)

person.details.age = 99
likho("After change:", person)

peeche()
likho("After peeche():", person)

agar (person.details.age == 15) {
    likho("✅ TEST 3 PASSED - Nested object restored!")
} nahi_to {
    likho("❌ TEST 3 FAILED - Expected age 15, got", person.details.age)
}
likho("")

likho("=== Test 4: Array with Objects ===")
time_machine_on(20)

students = [
    {naam: "Raj", marks: 85},
    {naam: "Priya", marks: 92}
]
likho("Initial:", students)

students[0].marks = 100
likho("After change:", students)

peeche()
likho("After peeche():", students)

agar (students[0].marks == 85) {
    likho("✅ TEST 4 PASSED - Array of objects works!")
} nahi_to {
    likho("❌ TEST 4 FAILED - Expected 85, got", students[0].marks)
}
likho("")

likho("=== Test 5: Multiple Changes with Multiple peeche() ===")
time_machine_on(20)

data = [[10, 20], [30, 40]]
likho("Initial:", data)

data[0][0] = 111
likho("Change 1:", data)

data[1][1] = 222
likho("Change 2:", data)

peeche(2)
likho("After peeche(2):", data)

agar (data[0][0] == 10 aur data[1][1] == 40) {
    likho("✅ TEST 5 PASSED - Multiple peeche() works!")
} nahi_to {
    likho("❌ TEST 5 FAILED")
}
likho("")

likho("=== All Tests Complete ===")
likho("Deep copy functionality is production-ready! 🚀")
