#Question 5: Contact Book (Dictionaries - Basic Operations)
contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Charlie": "555-9999"
}
print(f"Alice's Number: {contacts["Alice"]}")

contacts["Diana"] = "555-4321"
print(f"Contacts After Adding Diana: {contacts}")

contacts["Bob"] = "555-0000"
print(f"Contacts After Updating Bob: {contacts}")

del contacts["Charlie"]
print(f"Contacts After Deleting Charlie: {contacts}")
print(f"All Names: {contacts.keys()}")
print(f"All Numbers: {contacts.values()}")
print(f"Total Cont  acts: {len(contacts)}")