# # наслідування
#
# # переведення числа в діапазон [0, 100]
#
# value = -10
#
# # варіант через if
# # if value > 100:
# #     value = 100
# # elif value < 0:
# #     value = 0
#
# # через min max
#
# value = -10
# new_value = min(value, 100)
# new_value = max(new_value, 0)
#
# new_value = max(0, min(100, value))  # clip
#
# print(new_value)

# використання методів батьківського класу
from abc import ABC, abstractmethod

class Animal(ABC):  # абстрактний клас(не можна створити об'єкт)
    @abstractmethod
    def __init__(self, name, age):
        self._check_name(name)
        self._check_age(age)
        self.name = name
        self.age = age

    def _check_name(self, name):
        # перевірка чи тип даних str
        if not isinstance(name, str):
            raise ValueError(f"Ім'я має бути рядком, отримано тип {type(name)}")

        # лише літери та символи ' ' '-'
        for sym in name:
            if not(sym.isalpha() or sym in ' -'):
                raise ValueError("Ім'я має складатися лише з літер та ' -'")

    def _check_age(self, age):
        # перевірка чи тип даних int float
        if not isinstance(age, (int, float)):
            raise ValueError(f"Вік має бути числом, отримано тип {type(age)}")

        if age <= 0 or age >= 20:
            raise ValueError(f"Вік має бути в діапазоні [0, 20]")


    def info(self):
        print(f"Ім'я: {self.name}, {self.age} років")


class Cat(Animal): # name, age, is_vaccinated
    def __init__(self, name, age, is_vaccinated=True):
        super().__init__(name, age)
        self.is_vaccinated = is_vaccinated

    def catch_mouse(self):
        print("Ловить мишу")

    def info(self):  # додатково писало що це кіт
        print("Кіт")
        # super() # super -- батьківський клас
        super().info() # info з класу Animal

        if self.is_vaccinated:
            print("Вакцинований")
        else:
            print("Потрібно вакцинувати")


# cat1 = Cat('Tom', 5)
# cat1.info()
# #cat1.catch_mouse()
# print()
#
# cat = Animal('Roger', 10)
# cat.info()

# приховані атрибути\методи

class Cat(Animal): # name, age, is_vaccinated
    def __init__(self, name, age, is_vaccinated=True):
        super().__init__(name, age)
        self._is_vaccinated = is_vaccinated  # прихований атрибут

    def catch_mouse(self):
        print("Ловить мишу")

    def info(self):  # додатково писало що це кіт
        print("Кіт")
        # super() # super -- батьківський клас
        super().info() # info з класу Animal

        if self._is_vaccinated:
            print("Вакцинований")
        else:
            print("Потрібно вакцинувати")

    def vaccinate(self):
        self._is_vaccinated = True

    def unvaccinate(self):
        self._is_vaccinated = False


class Kitten(Cat):
    pass


cat1 = Cat('Tom', 2.5)

cat1.info()

cat1.unvaccinate()

cat1.info()

# print(cat1._Cat__is_vaccinated)

kitten = Kitten("Murchyck", 1)
kitten.info()

# Завдання 1
# Створіть абстрактний клас Robot з атрибутами:
#  name – назва робота або id
#  battery_level – рівень заряду(за замовчуванням 100%)
#  status – поточний стан (один з on, off, working)
# Методи:
#  info() – виводить інформацію
#  charge() – відновлює заряд до 100%
#  turn_on() – змінює стан на on
#  turn_off() – змінює стан на off












# Завдання 2
# Створіть дочірній клас CleaningRobot
# Додаткові атрибути:
#  dust_capacity – ємність контейнеру для пилу(за
# замовчуванням 0%)
#  water_capacity – ємність контейнеру для води(за
# замовчуванням 100%)
#  cleaning_mode – тип прибирання(вологе або сухе)
# Методи:
#  info() – додатково виводить інформацію про робота
#  turn_on() – якщо контейнер для пилу повний або
# контейнер для води порожній то виводить повідомлення,
# інакше запускається turn_on() з класу Robot
#  empty_dustbin() – очищає контейнер для пилу
#  fill_water() – заповнює контейнер для води
#  swap_mode() – змінює тип прибирання на протилежний
#  clean(energy, dust, water=None) – чистить поверхню,
# якщо прибирання сухе, то просто перенести пил у
# контейнер(якщо місця не достатньо вивести помилку),
# якщо прибирання вологе то додатково витратити воду.
# Також зменшує рівень заряду на energy
# Завдання 3
# Створіть дочірній клас SecurityRobot
# Додаткові атрибути:
#  min_speed – мінімальна швидкість руху, щоб помітити
# об’єкт
#  alert_level – рівень небезпеки (low, middle, high)
#  dangerous_items – список небезпечних предметів(gun,
# knife, bat)
# Методи:
#  info() – додатково виводить інформацію про робота
#  turn_off() – перед виключенням змінює рівень небезпеки
# на low
#  add_dangerous_item(item) – додає небезпечний предмет
#  remove_dangerous_item(item) – видаляє небезпечний
# предмет
#  detect(speed, item) – виявляє загрозу
# o якщо швидкість занизька, то ігноруємо
# o якщо швидкість велика, то рівень небезпеки
# middle
# o якщо це небезпечний предмет, то рівень
# небезпеки high
# Рівень небезпеки не може стати нижчим
# Завдання 4
# Створіть дочірній клас AssistantRobot
# Додаткові атрибути:
#  tasks – список завдань(за замовчуванням порожній)
#  current_task – поточне завдання(за замовчуванням None)
# Методи:
#  info() – додатково виводить інформацію про робота
#  add_task(task) – додає завдання до списку
#  change_task() – змінює поточне завдання, виводить на
# екран список завдань та просить користувача вибрати
# одне з них
#  execute_task() – виконує поточне завдання, видяляє його
# зі списку, та змінює current_task на наступне