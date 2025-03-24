# Використовуючи бінарні дерева, організуйте роботу
# автопарку, де зберігаються автомобілі,ідсортовані за
# маркою
# Клас Car
# Атрибути:
#  brand – модель автомобіля
#  model – марка автомобіля
#  year – рік випуску
# Клас CarPark
# Атрибути:
#  cars – дерево з автомобілями
# Методи:
#  add(car) – добавити автомобіль
#  remove(model) – видалити автомобіль
#  search(model) – пошук автомобіля за маркою, якщо є
# то повертає книгу інакше None
#  __len__() – кількість автомобілів
#  sell_car(client, model) – продати автомобіль клієнту,
# якщо така марка присутня
import bintrees
from bintrees import AVLTree


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


    def display_info(self):
        return f"{self.year} {self.brand} {self.model}"


class CarPark:
    def __init__(self):
        self.cars = AVLTree()

    def add(self, car):
        self.cars.insert(car.model, car)

    def remove_car(self, model):
        if model in self.cars:
            self.cars.remove(model)
        else:
            print('Car not in stock')

    def search(self, model):
        return self.cars.get(model, None)

    def __len__(self):
        return len(self.cars)

    def sell_car(self, client, model):
        car = self.search(model)
        if not car:
            print('Car not exist')
            return
        self.remove_car(model)
        print(f'{client} bought car {model}')

    def display_info(self, model):
        car = self.search(model)
        if car:
            print(f"""
            Brand = {car.brand}
            Model = {car.model}
            Year  = {car.year}
            """)
        else:
            print("Car not found")


# Приклад використання
cars_shop = CarPark()
cars_list = [
    Car("Toyota", "Corolla", 2020),
    Car("Honda", "Civic", 2018),
    Car("Ford", "Focus", 2019),
    Car("BMW", "X5", 2021),
    Car("Audi", "A4", 2017),
    Car("Mercedes", "C-Class", 2022),
    Car("Hyundai", "Elantra", 2016),
    Car("Nissan", "Altima", 2020),
    Car("Chevrolet", "Malibu", 2019),
    Car("Mazda", "CX-5", 2021)
]

for car in cars_list:
    cars_shop.add(car)

for car in cars_list:
    print(car.display_info())

cars_shop.search("X5")
number_of_cars = cars_shop.__len__()
print("Cars in stock: ", number_of_cars )
cars_shop.sell_car("jhon", "Altima")
cars_shop.search("Altima")
cars_shop.display_info("Altima")
number_of_cars = cars_shop.__len__()
print("Cars in stock: ", number_of_cars )

