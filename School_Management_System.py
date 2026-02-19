class SchoolManagement:
    def __init__(self):
        self.students = {}
        self.next_student_id = 1001  # auto-increment ID

    
    # NEW ADMISSION
    def new_admission(self):
        name = input("Enter student name: ")

        try:
            age = int(input("Enter age: "))
        except ValueError:
            print(" Age must be a number")
            return

        if age < 5 or age > 18:
            print(" Age must be between 5 and 18")
            return

        try:
            student_class = int(input("Enter class (1–12): "))
        except ValueError:
            print(" Class must be a number")
            return

        if student_class < 1 or student_class > 12:
            print(" Class must be between 1 and 12")
            return

        mobile = input("Enter guardian mobile number: ")

        if not (mobile.isdigit() and len(mobile) == 10):
            print(" Mobile number must be exactly 10 digits")
            return


        # Assign student ID
        student_id = self.next_student_id
        self.next_student_id += 1


        # Store student record
        self.students[student_id] = {
            "name": name,
            "age": age,
            "class": student_class,
            "mobile": mobile}

        print(f" Admission successful! Student ID: {student_id}")



    # VIEW STUDENT
    def view_student(self):
        try:
            student_id = int(input("Enter student ID: "))
        except ValueError:
            print(" Invalid student ID")
            return

        if student_id not in self.students:
            print(" Student record not found")
            return

        student = self.students[student_id]
        print("\n Student Details")
        print(f"Student ID : {student_id}")
        print(f"Name       : {student['name']}")
        print(f"Age        : {student['age']}")
        print(f"Class      : {student['class']}")
        print(f"Mobile     : {student['mobile']}")



    # UPDATE STUDENT
    def update_student(self):
        try:
            student_id = int(input("Enter student ID: "))
        except ValueError:
            print(" Invalid student ID")
            return

        if student_id not in self.students:
            print(" Student record not found")
            return

        print("\n1. Update Mobile Number")
        print("2. Update Class")
        choice = input("Enter choice: ")

        if choice == "1":
            new_mobile = input("Enter new mobile number: ")
            if not (new_mobile.isdigit() and len(new_mobile) == 10):
                print(" Mobile number must be exactly 10 digits")
                return
            self.students[student_id]["mobile"] = new_mobile
            print(" Mobile number updated successfully")

        elif choice == "2":
            try:
                new_class = int(input("Enter new class (1–12): "))
            except ValueError:
                print(" Class must be a number")
                return

            if new_class < 1 or new_class > 12:
                print(" Class must be between 1 and 12")
                return

            self.students[student_id]["class"] = new_class
            print(" Class updated successfully")

        else:
            print(" Invalid choice")



    # REMOVE STUDENT
    def remove_student(self):
        try:
            student_id = int(input("Enter student ID: "))
        except ValueError:
            print(" Invalid student ID")
            return

        if student_id in self.students:
            del self.students[student_id]
            print(" Student record removed successfully")
        else:
            print(" Student record not found")



school = SchoolManagement()

while True:
    print("\n School Management System")
    print("1. New Admission")
    print("2. View Student Details")
    print("3. Update Student Info")
    print("4. Remove Student Record")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        school.new_admission()
    elif choice == "2":
        school.view_student()
    elif choice == "3":
        school.update_student()
    elif choice == "4":
        school.remove_student()
    elif choice == "5":
        print("Exiting system...")
        break
    else:
        print(" Invalid choice. Try again.")
