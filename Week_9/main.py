from ticket import create_ticket
from display import display_ticket

def main():

    student_name, student_id, issue, location, priority = create_ticket()

    if priority.lower() == "high":
        technician = "Ahmad"
    elif priority.lower() == "medium":
        technician = "Siti"
    else:
        technician = "Ali"

    status = "Pending"

    display_ticket(
        student_name,
        student_id,
        issue,
        location,
        priority,
        technician,
        status
    )

if __name__ == "__main__":
    main()
    