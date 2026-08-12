def get_student():
    print("===== Computer Lab Access =====")

    name = input("Student Name : ")
    student_id = input("Student ID : ")
    registered = input("Registered for today's lab? (Y/N): ").upper()
    lab_open = input("Is the lab open? (Y/N): ").upper()
    computer = input("Computer Available? (Y/N): ").upper()

    return name, student_id, registered, lab_open, computer
