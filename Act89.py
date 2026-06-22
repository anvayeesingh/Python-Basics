grade_book = {
    "Anya"(85,95,90),
    "Rahul"(89,85,80),
    "Meera"(89,90,95,),
    "Arjun"(85,95,88),
    "Riya"(80,90,85)
}

students = list(grade_book.keys())
grades = set()

print("Grade book\n")

for student in students:
    grading = grade_book[student]
    average = sum(grading)/len(grading)

    print("Name ", student)
    print("Grades ", grades)
    print("Average ", average)
    average = sum(grading)/len(grading)

    print("Name: ", student)
    print("Grades: ", grading)
    print("Average: ",average)
    print()

    grades.update(grading)
print(" Students list: ")
print(students)

print("Unique grades: ")
print(grades)