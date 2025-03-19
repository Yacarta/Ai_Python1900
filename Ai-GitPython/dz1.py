from queue import PriorityQueue

class Passenger:
    def __init__(self, name, priority, baggage=None):
        if baggage is None:
            baggage = []
        self.name = name
        self.priority = priority
        self.baggage = baggage

class Zone:
    def __init__(self, name):
        self.name = name
        self.passengers = PriorityQueue()

    def add_passenger(self, passenger):
        self.passengers.put((passenger.priority, passenger))

    def serve_passenger(self):
        if not self.passengers.empty():
            _, passenger = self.passengers.get()
            return passenger
        return None

class RegistrationZone(Zone):
    def serve_passenger(self):
        if not self.passengers.empty():
            _, passenger = self.passengers.get()
            has_ticket = "ticket" in passenger.baggage
            return passenger, has_ticket
        return None, False

class SecurityZone(Zone):
    def serve_passenger(self):
        if not self.passengers.empty():
            _, passenger = self.passengers.get()
            danger_items = {"knife", "gun", "explosives"}
            is_safe = not any(item in danger_items for item in passenger.baggage)
            return passenger, is_safe
        return None, False

class BoardingZone(Zone):
    def serve_passenger(self):
        passenger = super().serve_passenger()
        return passenger, passenger is not None

class Airport:
    def __init__(self):
        self.zones = {
            "Registration": RegistrationZone("Реєстрація"),
            "Control": SecurityZone("Контроль"),
            "Board": BoardingZone("Посадка")
        }
        self.boarded_passengers = []

    def add(self, passenger):
        self.zones["Registration"].add_passenger(passenger)

    def serve_registration(self):
        passenger, has_ticket = self.zones["Registration"].serve_passenger()
        if passenger and has_ticket:
            self.zones["Control"].add_passenger(passenger)
        elif passenger:
            print(f"{passenger.name} cannot register due to missing ticket.")

    def serve_security_control(self):
        passenger, is_safe = self.zones["Control"].serve_passenger()
        if passenger and is_safe:
            self.zones["Board"].add_passenger(passenger)
        elif passenger:
            print(f"{passenger.name} failed security check due to prohibited items.")

    def serve_boarding(self):
        passenger, success = self.zones["Board"].serve_passenger()
        if success and passenger:
            self.boarded_passengers.append(passenger)

    def show_statistics(self):
        print(f"Total boarded passengers: {len(self.boarded_passengers)}")


# Passenger test cases
passengers = [
    Passenger("Alice", 2, ["ticket", "phone"]),
    Passenger("Bob", 1, ["ticket", "knife"]),
    Passenger("Charlie", 3, ["ticket"]),
    Passenger("David", 4, ["ticket", "laptop"]),
    Passenger("Eva", 2, ["bottle", "knife"]),
    Passenger("Frank", 3, ["book"]),
    Passenger("Grace", 1, ["ticket", "explosives"]),
    Passenger("Hannah", 5, ["phone", "tablet"]),
    Passenger("Ivy", 2, ["ticket", "earphones"]),
    Passenger("Jack", 1, ["ticket", "gun"]),
]

# Create airport
airport = Airport()

# Add passengers to registration
for passenger in passengers:
    airport.add(passenger)

# Process each passenger through all zones
for _ in range(len(passengers)):
    airport.serve_registration()
    airport.serve_security_control()
    airport.serve_boarding()

# Show statistics
airport.show_statistics()
