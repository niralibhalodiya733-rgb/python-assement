class BusReservation:
    def __init__(self):
        self.routes = {
            "Mumbai to Pune": 500,
            "Delhi to Jaipur": 600,
            "Bangalore to Chennai": 700,
            "Kolkata to Patna": 550}

        self.tickets = {}

        # Seat tracking per route
        # route : seats_booked
        self.seats = {route: 0 for route in self.routes}

        self.next_ticket_id = 10001  # auto-generated ticket ID
        self.max_seats = 40



    # SHOW ROUTES
    def show_routes(self):
        print("\n🛣 Available Routes")
        for route, price in self.routes.items():
            available = self.max_seats - self.seats[route]
            print(f"{route} - ₹{price} | Seats Available: {available}")



    # BOOK TICKET
    def book_ticket(self):
        name = input("Enter passenger name: ")

        try:
            age = int(input("Enter age: "))
        except ValueError:
            print(" Age must be a number")
            return

        mobile = input("Enter mobile number: ")
        if not (mobile.isdigit() and len(mobile) == 10):
            print(" Mobile number must be 10 digits")
            return

        self.show_routes()
        route = input("Enter route exactly as shown: ")

        if route not in self.routes:
            print(" Invalid route selection")
            return

        if self.seats[route] >= self.max_seats:
            print(" Bus is full for this route")
            return



        # Assigning seat number
        seat_number = self.seats[route] + 1
        self.seats[route] += 1

        # Generating ticket ID
        ticket_id = self.next_ticket_id
        self.next_ticket_id += 1

        # Storing ticket details
        self.tickets[ticket_id] = {
            "name": name,
            "age": age,
            "mobile": mobile,
            "route": route,
            "price": self.routes[route],
            "seat": seat_number}

        print("\n Ticket Booked Successfully!")
        print(f" Ticket ID : {ticket_id}")
        print(f" Seat No   : {seat_number}")
        print(f" Fare      : ₹{self.routes[route]}")



    # VIEW TICKET
    def view_ticket(self):
        try:
            ticket_id = int(input("Enter ticket ID: "))
        except ValueError:
            print(" Invalid ticket ID")
            return

        if ticket_id not in self.tickets:
            print(" Ticket not found")
            return

        ticket = self.tickets[ticket_id]
        print("\n Ticket Details")
        print(f"Ticket ID : {ticket_id}")
        print(f"Name      : {ticket['name']}")
        print(f"Age       : {ticket['age']}")
        print(f"Mobile    : {ticket['mobile']}")
        print(f"Route     : {ticket['route']}")
        print(f"Seat No   : {ticket['seat']}")
        print(f"Fare      : ₹{ticket['price']}")



    # CANCEL TICKET
    def cancel_ticket(self):
        try:
            ticket_id = int(input("Enter ticket ID to cancel: "))
        except ValueError:
            print(" Invalid ticket ID")
            return

        if ticket_id not in self.tickets:
            print(" Ticket not found")
            return

        route = self.tickets[ticket_id]["route"]
        self.seats[route] -= 1
        del self.tickets[ticket_id]

        print(" Ticket cancelled successfully")


bus = BusReservation()

while True:
    print("\n Bus Reservation System")
    print("1. Show Available Routes")
    print("2. Book Ticket")
    print("3. View Ticket")
    print("4. Cancel Ticket")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        bus.show_routes()
    elif choice == "2":
        bus.book_ticket()
    elif choice == "3":
        bus.view_ticket()
    elif choice == "4":
        bus.cancel_ticket()

