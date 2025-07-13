students_marks={
    "Alice":85,
    "Bob": 78,
    "Maggie": 55,
    "Charlie": 64
}
name = input("Enter the student's name: ")
if name in students_marks:
    print(f"{name}'s, marks: {students_marks[name]}")
else:
    print("student not found")


