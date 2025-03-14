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
        priority = passenger.priority
        self.passengers.put((priority, passenger))

    def serve_passenger(self):
        if not self.passengers.empty():
            priority, passenger = self.passengers.get()
            return passenger
        return None


class RegistrationZone(Zone):
    def registration(self):
        if not self.passengers.empty():
            passenger = self.serve_passenger()
            has_ticket = "ticket" in passenger.baggage
            return passenger, has_ticket
        return None, False


class SecurityZone(Zone):
    def serve_passenger(self):
        if not self.passengers.empty():
            passenger = super().serve_passenger()
            danger_items = ["knife", "gun", "explosives"]
            is_safe = not any(item in passenger.baggage for item in danger_items)
            return passenger, is_safe
        return None, False


class Airport:
    def __init__(self):
        self.zones = {
            "Registration": RegistrationZone("Реєстрація"),
            "Control": SecurityZone("Контроль"),
            "Board": Zone("Посадка")
        }
        self.passengers = []

    def add(self, passenger):
        self.zones["Registration"].add_passenger(passenger)

    def serve_registration(self):
        passenger, has_ticket = self.zones["Registration"].registration()
        if passenger and has_ticket:
            self.zones["Control"].add_passenger(passenger)
        else:
            print(f'Cannot register {passenger.name} due to missing ticket.')

    def serve_security_control(self):
        passenger, is_safe = self.zones["Control"].serve_passenger()
        if passenger and is_safe:
            self.zones["Board"].add_passenger(passenger)
        elif passenger:
            print(f'{passenger.name} failed security check due to prohibited items.')

    def serve_boarding(self):
        passenger = self.zones["Board"].serve_passenger()
        if passenger:
            self.passengers.append(passenger)

    def show_statistics(self):
        print(f'Total boarded passengers: {len(self.passengers)}')


# ==========================
# Example Usage
# ==========================
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

# Create airport and add passengers
airport = Airport()
for p in passengers:
    airport.add(p)

# Process each passenger through the airport
for _ in range(len(passengers)):
    airport.serve_registration()
    airport.serve_security_control()
    airport.serve_boarding()

# Show statistics
airport.show_statistics()
# Використання
passenger1 = Passenger("Alice", 2, ["ticket", "phone"])
passenger2 = Passenger("Bob", 1, ["ticket", "knife"])
passenger3 = Passenger("Charlie", 3, ["ticket"])
passenger4 = Passenger("David", 4, ["ticket", "laptop"])
passenger5 = Passenger("Eva", 2, ["bottle", "knife"])
passenger6 = Passenger("Frank", 3, ["book"])
passenger7 = Passenger("Grace", 1, ["ticket", "explosives"])
passenger8 = Passenger("Hannah", 5, ["phone", "tablet"])
passenger9 = Passenger("Ivy", 2, ["ticket", "earphones"])
passenger10 = Passenger("Jack", 1, ["ticket", "gun"])

# Створюємо аеропорт
airport = Airport()

# Додаємо пасажирів до реєстрації
airport.add(passenger1)
airport.add(passenger2)
airport.add(passenger3)
airport.add(passenger4)