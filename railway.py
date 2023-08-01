available_trains = [
    {"train_number": "15017", "source": "LTT", "destination": "GKP", "departure_time": "06:30 AM", "seats": 5},
    {"train_number": "12165", "source": "KYN", "destination": "PRYG", "departure_time": "09:00 AM", "seats": 3},
    {"train_number": "11071", "source": "THANE", "destination": "BSB", "departure_time": "02:00 PM", "seats": 7}
]

booked_tickets = []

def display_available_trains():
    print("Available Trains:")
    print("-----------------")
    for train in available_trains:
        print("Train Number:", train["train_number"])
        print("Source:", train["source"])
        print("Destination:", train["destination"])
        print("Departure Time:", train["departure_time"])
        print("Available Seats:", train["seats"])
        print("-----------------")

def check_seat_availability(train_number):
    for train in available_trains:
        if train["train_number"] == train_number:
            return train["seats"]
    return 0

def book_ticket():
    train_number = input("Enter Train Number: ")
    seats_available = check_seat_availability(train_number)
    if seats_available == 0:
        print("Train not found or no seats available.")
        return
    passenger_name = input("Enter Passenger Name: ")
    source = input("Enter Source Station: ")
    destination = input("Enter Destination Station: ")
    seat_number = input("Enter Seat Number: ")
    booked_tickets.append({
        "passenger_name": passenger_name,
        "train_number": train_number,
        "source": source,
        "destination": destination,
        "seat_number": seat_number
    })
    for train in available_trains:
        if train["train_number"] == train_number:
            train["seats"] -= 1
            break
    print("Ticket booked successfully.")

def display_booked_tickets():
    print("Booked Tickets:")
    print("-----------------")
    for ticket in booked_tickets:
        print("Passenger Name:", ticket["passenger_name"])
        print("Train Number:", ticket["train_number"])
        print("Source:", ticket["source"])
        print("Destination:", ticket["destination"])
        print("Seat Number:", ticket["seat_number"])
        print("-----------------")

def cancel_ticket():
    ticket_index = int(input("Enter the index of the ticket to be canceled: "))
    if ticket_index < 0 or ticket_index >= len(booked_tickets):
        print("Invalid ticket index.")
        return
    ticket = booked_tickets[ticket_index]
    train_number = ticket["train_number"]
    seat_number = ticket["seat_number"]
    for train in available_trains:
        if train["train_number"] == train_number:
            train["seats"] += 1
            break
    del booked_tickets[ticket_index]
    print("Ticket canceled successfully.")

# Main menu loop
while True:
    print("Railway Reservation System")
    print("1. Display Available Trains")
    print("2. Check Seat Availability")
    print("3. Book a Ticket")
    print("4. Display Booked Tickets")
    print("5. Cancel a Ticket")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        display_available_trains()
    elif choice == "2":
        train_number = input("Enter Train Number: ")
        seats_available = check_seat_availability(train_number)
        print("Seats available:", seats_available)
    elif choice == "3":
        book_ticket()
    elif choice == "4":
        display_booked_tickets()
    elif choice == "5":
        cancel_ticket()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")
