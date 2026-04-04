#Question 4: Class Attendance (Sets - Uniqueness and Operations
mondayClass = {"Alice", "Bob", "Charlie", "Diana"}
wednesdayClass = {"Bob", "Diana", "Eve", "Frank"}

mondayClass.add("Grace")
print("MondayClass:", mondayClass)
print("Wednesday Class:", wednesdayClass)

bothClasses = mondayClass & wednesdayClass
print("Attended Both Classes:", bothClasses)

allStudents = mondayClass | wednesdayClass
print("Attended Either Class:", allStudents)

onlyOne = mondayClass ^ wednesdayClass
print("Only One Class:", onlyOne)
print("Is Monday a subset of all students?", mondayClass <= allStudents)