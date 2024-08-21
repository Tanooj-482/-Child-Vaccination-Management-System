import datetime

class VaccinationManagementSystem:
    def __init__(self):
        self.users = {}
        self.vaccination_records = []
        self.reminders = []

    def register_user(self):
        username = input("Enter your username: ")
        if username in self.users:
            print(f"User {username} already registered.")
        else:
            child_name = input("Enter your child's name: ")
            child_dob = input("Enter your child's date of birth (YYYY-MM-DD): ")
            self.users[username] = {"child_name": child_name, "child_dob": child_dob}
            print(f"User {username} registered successfully.")

    def book_appointment(self):
        username = input("Enter your username: ")
        if username in self.users:
            vaccine_name = input("Enter the vaccine name: ")
            date = input("Enter the appointment date (YYYY-MM-DD): ")
            appointment = {
                "username": username,
                "child_name": self.users[username]["child_name"],
                "vaccine_name": vaccine_name,
                "date": date
            }
            self.vaccination_records.append(appointment)
            self.reminders.append(appointment)
            print(f"Appointment for {vaccine_name} on {date} booked successfully for {self.users[username]['child_name']}.")
        else:
            print(f"User {username} not found.")

    def view_appointments(self):
        username = input("Enter your username: ")
        if username in self.users:
            print(f"Appointments for {self.users[username]['child_name']}:")
            for record in self.vaccination_records:
                if record["username"] == username:
                    print(f"  {record['vaccine_name']} on {record['date']}")
        else:
            print(f"User {username} not found.")

    def send_reminders(self):
        today = datetime.date.today()
        print("Sending reminders:")
        for reminder in self.reminders:
            reminder_date = datetime.datetime.strptime(reminder["date"], "%Y-%m-%d").date()
            days_left = (reminder_date - today).days
            if days_left >= 0:
                print(f"Reminder: {reminder['child_name']} has a vaccination appointment for {reminder['vaccine_name']} in {days_left} days on {reminder['date']}.")

if __name__ == "__main__":
    system = VaccinationManagementSystem()

    while True:
        print("\n1. Register User")
        print("2. Book Appointment")
        print("3. View Appointments")
        print("4. Send Reminders")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            system.register_user()
        elif choice == '2':
            system.book_appointment()
        elif choice == '3':
            system.view_appointments()
        elif choice == '4':
            system.send_reminders()
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")
