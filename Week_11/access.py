def check_access(registered, lab_open, computer):

    if registered == "Y" and lab_open == "Y" and computer == "Y":
        return "Access Granted"
    else:
        return "Access Denied"


def get_reason(registered, lab_open, computer):

    if registered != "Y":
        return "Student is not registered"

    elif lab_open != "Y":
        return "Computer lab is closed"

    elif computer != "Y":
        return "No available computer"

    else:
        return "Welcome to the lab"
    