students = []

# Function: Clear the terminal (EXTRA)

import os

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Function: Add student

def add_student():
    try:
        student_id = int(input("Enter ID: "))
        for student in students:
            if student['id'] == student_id:
                print("Error: This ID already exists.")
                return
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")
        active = input("Is the student active? (yes/no): ").lower()
    except ValueError:
        print("Error: Invalid data type")
        return

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "active": active
    }

    students.append(student)
    print("Student added succesfully!")

# Function: Show students

def show_students():
    if len(students) == 0:
        print("No students registered.")
        return
    else:
        for student in students:
            print("-" * 20)
            print(f"ID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Course: {student['course']}")
            print(f"Status: {"Active" if student['active'] == "yes" else "Inactive"}")
            print("-" * 20)

# Function: Search student

def search_student():
    try:
        search_id = int(input("Enter ID: "))
    except ValueError:
        print("Invalid ID")
        return

    for student in students:
        if student['id'] == search_id:
            print("-" * 20)
            print(f"ID: {student['id']}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Course: {student['course']}")
            print(f"Status: {"Active" if student['active'] == "yes" else "Inactive"}")
            print("-" * 20)
            return
    
    print("Student not found")

# Function: Update student

def update_student():
    try:
        search_id = int(input("Enter ID: "))
    except ValueError:
        print("Invalid ID")
        return
    
    for student in students:
        if student['id'] == search_id:
            student['name'] = input("New name: ")
            student['age'] = int(input("New age: "))
            student['course'] = input("New course: ")
            student['active'] = input("Is the student active? (yes/no): ").lower()
            print("Student updated succesfuly!")
            return
    
    print("Student not found")

# Function: Delete student

def delete_student():
    try:
        search_id = int(input("Enter ID: "))
    except ValueError:
        print("Invalid ID")
        return
    
    for student in students:
        if student['id'] == search_id:
            confirm = input("Are you sure you want to delete this student? (yes/no): ")
            if confirm.lower() == "yes":
                students.remove(student)
                print("Student deleted succesfully!")
                return
            else:
                print("Operation cancelled.")
                return
    print("Student not found")

# Menu

def menu():
    while True:
        print("\n1. Add student")
        print("2. Show students")
        print("3. Search student")
        print("4. Update student")
        print("5. Delete student")
        print("6. Exit")

        option = input("Choose option: ")

        if option == "1":
            clear_screen()
            add_student()
        elif option == "2":
            clear_screen()
            show_students()
        elif option == "3":
            clear_screen()
            search_student()
        elif option == "4":
            clear_screen()
            update_student()
        elif option == "5":
            clear_screen()
            delete_student()
        elif option == "6":
            clear_screen()
            print("Goodbye!")
            break
        else:
            print("Invalid option!")

menu()