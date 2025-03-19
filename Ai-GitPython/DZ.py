from queue import PriorityQueue

class Passenger:
    def __init__(self, name, priority, baggage):
        self.name = name
        self.priority = priority
        self.baggage = baggage



class Zone:
    def __init__(self, name):
        self.name = name
        self.passengers = PriorityQueue()

    def add_passanger(self, passenger):
        priority = passenger.priority
        pair = (priority, passenger)
        self.passengers.put(pair)

    def serve_passenger(self):
        priority, passenger = self.passengers.get()
        return passenger


class RegistrationZone(Zone):
     def serve_passenger(self):
        priority, passenger = self.passengers.get()
        if "ticket" in passenger.baggage:
            return passenger, True
        else:
            return passenger, False


class SecurityZone(Zone):
    def serve_passenger(self):
        if not self.passengers.empty():
            priority, passenger = self.passengers.get()
            if ("weapon" in passenger.baggage) or ("knife" in passenger.baggage):
                return passenger, True
            else:
                return passenger, False
        return None, True


class BoardingZone(Zone):
    def serve_passenger(self):
        if not self.passengers.empty():
            priority, passenger = self.passengers.get()
            return passenger, True
        return None, False


class Airport:
    def __init__(self):
        self.zones = {"Registration": RegistrationZone("Реєстрація"),
                      "Control": SecurityZone("Контроль"),
                      "Board": BoardingZone("Посадка")}
        self.passengers = []

    def add(self, passenger):
        self.zones["Registration"].add_passanger(passenger)

    def serve_registration(self):
        pas, bool = self.zones["Registration"].serve_passenger()
        # перевірка чи відповідає пасажир умові переходу в іншу зону
        if bool:
            self.zones["Control"].add_passanger(pas)
            print(f"{pas.name} пройшов в зону контролю безпеки.")
        else:
            print(f"{pas.name} не має квитка.")

    def serve_security_control(self):
        pas, bool = self.zones["Control"].serve_passenger()
        if pas and not bool:
            self.zones["Board"].add_passanger(pas)
            print(f"{pas.name} пройшов в зону посадки.")
        elif pas :
            print(f"{pas.name} має в багажі заборонені предмети.")

    def serve_boarding(self):
        pas, bool = self.zones["Board"].serve_passenger()
        if bool:
            self.passengers.append(pas)

    def show_statistics(self):
        print(len(self.passengers))
        for p in self.passengers:
            print(f"В літаку пасажир - {p.name}")



# # Тестування
airport = Airport()

passengers = [
    Passenger("Олег", 3, ["weapon", "clothes"]),
    Passenger("Анна", 5, ["ticket", "knife"]),
    Passenger("Марія", 4, ["clothes"]),  # немає квитка
    Passenger("Сергій", 2, ["ticket", "book"]),
    Passenger("Ігор", 1, ["ticket", "clothes"]),
]

for p in passengers:
    airport.add(p)

airport.serve_registration()
airport.serve_registration()
airport.serve_registration()
airport.serve_registration()
airport.serve_registration()

airport.serve_security_control()
airport.serve_security_control()
airport.serve_security_control()
airport.serve_security_control()
airport.serve_security_control()

airport.serve_boarding()
airport.serve_boarding()
airport.serve_boarding()
airport.serve_boarding()
airport.serve_boarding()

airport.show_statistics()