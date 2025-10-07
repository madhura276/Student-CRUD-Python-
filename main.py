from stu_crud import create_student, read_students, update_student, delete_student, exit_program

def menu():
    while True:
        print("\n--- Student CRUD Menu ---")
        print("1. Create Student")
        print("2. Read Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        
        choice = input("Enter choice (1-5): ")
        
        if choice == '1':
            id = int(input("Enter student ID: "))
            name = input("Enter student name: ")
            course = input("Enter student course: ")
            marks = int(input("Enter student marks: "))
            create_student(id, name, course, marks)
        
        elif choice == '2':
            read_students()
        
        elif choice == '3':
            id = int(input("Enter student ID to update: "))
            name = input("Enter new name (leave blank to skip): ")
            course = input("Enter new course (leave blank to skip): ")
            marks_input = input("Enter new marks (leave blank to skip): ")
            marks = int(marks_input) if marks_input else None
            update_student(id, name if name else None, course if course else None, marks)
        
        elif choice == '4':
            id = int(input("Enter student ID to delete: "))
            delete_student(id)
        
        elif choice == '5':
            exit_program()
        
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    menu()
