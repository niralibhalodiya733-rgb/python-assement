class ClinicAppointment:
    def __init__(self):
        # Fixed time slots
        self.time_slots = ["10am", "11am", "12pm", "2pm", "3pm"]
        self.appointments = {}



    # BOOK APPOINTMENT
    def book_appointment(self):
        name = input("Enter patient name: ")
        age = input("Enter age: ")
        mobile = input("Enter mobile number: ")
        doctor = input("Enter preferred doctor name: ")

        # Initialize doctor schedule if not exists
        if doctor not in self.appointments:
            self.appointments[doctor] = {slot: [] for slot in self.time_slots}

        print("\nAvailable Time Slots:")
        for slot in self.time_slots:
            booked = len(self.appointments[doctor][slot])
            print(f"{slot} ({3 - booked} slots available)")

        slot = input("Select time slot: ")

        if slot not in self.time_slots:
            print(" Invalid time slot")
            return

        # Check slot availability (max 3)
        if len(self.appointments[doctor][slot]) >= 3:
            print(" Slot is full. Please choose another slot.")
            return

        # Prevent duplicate booking using same mobile number
        if self._mobile_exists(mobile):
            print(" This mobile number already has an appointment.")
            return




     # Create appointment
        appointment = {
            "name": name,
            "age": age,
            "mobile": mobile,
            "slot": slot}

        self.appointments[doctor][slot].append(appointment)
        print(" Appointment booked successfully!")




    # VIEW APPOINTMENT
    def view_appointment(self, mobile):
        for doctor, slots in self.appointments.items():
            for slot, patients in slots.items():
                for appt in patients:
                    if appt["mobile"] == mobile:
                        print("\n Appointment Details")
                        print(f"Patient Name : {appt['name']}")
                        print(f"Age          : {appt['age']}")
                        print(f"Mobile       : {appt['mobile']}")
                        print(f"Doctor       : {doctor}")
                        print(f"Time Slot    : {slot}")
                        return
        print(" No appointment found for this mobile number.")




    # CANCELING APPOINTMENT
    def cancel_appointment(self, mobile):
        for doctor, slots in self.appointments.items():
            for slot, patients in slots.items():
                for appt in patients:
                    if appt["mobile"] == mobile:
                        patients.remove(appt)
                        print(" Appointment cancelled successfully!")
                        return
        print(" No appointment found to cancel.")




    # HELPER METHOD
    def _mobile_exists(self, mobile):
        for slots in self.appointments.values():
            for patients in slots.values():
                for appt in patients:
                    if appt["mobile"] == mobile:
                        return True
        return False


clinic = ClinicAppointment()

while True:
    print("\n Clinic Appointment System")
    print("1. Book Appointment")
    print("2. View Appointment")
    print("3. Cancel Appointment")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        clinic.book_appointment()
    elif choice == "2":
        mobile = input("Enter mobile number: ")
        clinic.view_appointment(mobile)
    elif choice == "3":
        mobile = input("Enter mobile number: ")
        clinic.cancel_appointment(mobile)
    elif choice == "4":
        print("Thank you for using the system ")
        break
    else:
        print(" Invalid choice. Please try again.")
