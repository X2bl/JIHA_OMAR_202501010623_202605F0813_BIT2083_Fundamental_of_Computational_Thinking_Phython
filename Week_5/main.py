from utils import calculate_total, print_receipt

customer_name = input("Customer name: ")

coffee = int(input("Coffee quantity: "))
tea = int(input("Tea quantity: "))
sandwich = int(input("Sandwich quantity: "))

total = calculate_total(coffee, tea, sandwich)

print_receipt(customer_name, coffee, tea, sandwich, total)1