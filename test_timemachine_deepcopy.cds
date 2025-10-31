// Test Time Machine Deep Copy Fix
// This tests nested arrays and objects restoration

time_machine_on(10)

likho("=== Test 1: Nested Arrays ===")
arr = [[1, 2], [3, 4]]
likho("Initial arr:", arr)

arr[0][0] = 999
likho("After modification:", arr)

peeche()
likho("After peeche():", arr)
likho("Expected: [[1, 2], [3, 4]]")
likho("")

likho("=== Test 2: Nested Objects ===")
time_machine_on(10)

obj = {
    person: {
        naam: "Raj",
        age: 25
    },
    scores: [90, 85, 88]
}
likho("Initial obj:", obj)

obj.person.naam = "Changed"
obj.scores[0] = 100
likho("After modification:", obj)

peeche()
likho("After peeche():", obj)
likho("Expected person.naam: Raj, scores[0]: 90")
likho("")

likho("=== Test 3: Multiple Levels Deep ===")
time_machine_on(10)

deep = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
likho("Initial deep:", deep)

deep[0][0][0] = 999
likho("After modification:", deep)

peeche()
likho("After peeche():", deep)
likho("Expected: [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]")
likho("")

likho("=== All Tests Complete ===")
