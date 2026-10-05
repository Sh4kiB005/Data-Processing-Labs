fare_table = {
    "Dhaka": 500,
    "Chittagong": 800,
    "Sylhet": 700,
    "Rajshahi": 600
}

name = input("Enter passenger name: ")
destination = input("Enter destination: ")
ticket_count = int(input("Enter number of tickets: "))
passenger_type = input("Enter passenger type (Adult/Child/Student/Senior): ").lower()

if destination not in fare_table:
    print("Destination not available.")
else:
    fare = fare_table[destination]

    if passenger_type == "child":
        discount = 0.50
    elif passenger_type == "student":
        discount = 0.20
    elif passenger_type == "senior":
        discount = 0.30
    else:
        discount = 0

    discounted_fare = fare * (1 - discount)
    total_fare = discounted_fare * ticket_count

    print("\n========== TICKET ==========")
    print("Passenger Name :", name)
    print("Destination    :", destination)
    print("Passenger Type :", passenger_type.title())
    print("Ticket Count   :", ticket_count)
    print("Fare per Ticket:", fare, "BDT")
    print("Discount       :", discount * 100, "%")
    print("Total Fare     :", total_fare, "BDT")
    print("============================")