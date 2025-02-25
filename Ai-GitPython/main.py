# наслідування

# class Parent:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def show_info(self):
#         print(f"клас Parent")
#         print(f'{self.name}, {self.age} років')
#
#
# class Child(Parent):
#     def play(self):   # новий метод
#         print('клас Child')
#         print(f'{self.name} грається')
#
#     def show_info(self):  # перевизначений метод
#         print(f"клас Child")
#         print(f'{self.name}, {self.age} років')
#
#
# class Daughter(Parent):
#     def __init__(self, name, age, dream):
#         self.name = name
#         self.age = age
#         self.dream = dream
#
#
# # mother = Parent('Marry', 36)
# # mother.show_info()
# #
# # print()
# #
# # child = Child('Rony', 8)
# # child.show_info()
# # child.play()
#
# # daughter = Daughter("Linda", 10, 'became a doctor')
# # daughter.show_info()
#
# # код з класом Parent
# mother = Parent('Marry', 36)
# mother.show_info()



# класи для Транспортні засоби

class Vehicle:
    def __init__(self, owner,  # власник
                 max_fuel_level,  # максимальний рівень пального
                 milliage  # км / 1 літр пального
                 ):
        self.owner = owner
        self.max_fuel_level = max_fuel_level
        self.fuel_level = max_fuel_level # бак повний
        self.milliage = milliage

    def move(self, speed, distance):
        need_fuel = distance / self.milliage

        if self.fuel_level < need_fuel: # не хватає пального
            print('не хватає пального')
        else:
            self.fuel_level -= need_fuel
            time = distance / speed

            print(f"Проїхали {distance}км за {time}год")


    def add_fuel(self, fuel):
        self.fuel_level += fuel

class Car(Vehicle):
    pass


class Bicycle(Vehicle):
    def __init__(self, owner, max_fuel_level, milliage):
        self.owner = owner
        self.max_fuel_level = max_fuel_level
        self.fuel_level = max_fuel_level  # бак повний
        self.milliage = milliage

        self.used_motor = False # мотор виключений


    def move(self, speed, distance):  # теж рухається але не трабе пального
        if not self.used_motor:
            time = distance / speed
            print("Без пального")
            print(f"Проїхали {distance}км за {time}год")
            return

        # мотор вклюсений(код з Vehicle.move)

        need_fuel = distance / self.milliage

        if self.fuel_level < need_fuel:  # не хватає пального
            print('не хватає пального')
        else:
            self.fuel_level -= need_fuel
            time = distance / speed

            print("З пальним")
            print(f"Проїхали {distance}км за {time}год")

    def turn_on(self):
        self.used_motor = True

    def turn_off(self):
        self.used_motor = False


class Plane(Vehicle):
    pass



# bike = Bicycle('John', 100, 50)
# bike.move(20, # швидкість
#          15  # кілометри
#          )
#
# bike.turn_on()
#
# bike.move(40,
#           100)
#
#
#
#
# car = Vehicle('John', 100, 50 )
# car.move(80,200)

#  Завдання 1
# Створіть абстрактний клас Character, атрибути
#  name – ім’я
#  max_hp – максимальний рівень здоров’я
#  hp – нинішній рівень здоров’я
#  level – рівень персонажа(від 1 до 20)
#  intelligence – стат інтелекту
#  strength – стат сили
#  dexterity – стат спритності
#  mana – стат мани
#  defense –  стат захисту
# Методи:
#  attack() – абстрактний метод
#  take_damage(damage) – отримує урон, зменшений на
# захист
#  level_up() – збільшує рівень
#  increase_stat(stat) – збільшує один з статів на 1
#  rest() – відпочинок(відновлює hp до максимального)
#  heal(heal_hp) – збільшує hp на heal_hp

class Character():
    def __init__(self, name, max_hp, level, intelligence, strength, dexterity, mana, defense):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.level = level
        self.intelligence = intelligence
        self.strength = strength
        self.dexterity = dexterity
        self.mana = mana
        self.defense = defense

    def attack(self):
        pass

    def take_damage(self, damage):
        if damage > self.defense:
            self.hp -= damage - self.defense

        if self.hp <= 0:
            self.hp = 0
            print(f"{self.name} загинув!")

    def level_up(self):
        if self.level < 20:
            self.level += 1

    def increase_stat(self, stat):
        if stat == 'intelligence':
            self.intelligence += 1
        elif stat == 'strength':
            self.strength += 1
        elif stat == "dexterity":
            self.dexterity += 1
        elif stat == "mana":
            self.mana += 1
        else:
            self.defense += 1

    def rest(self):
        self.hp = self.max_hp

    def heal(self, heal_hp):
        self.hp += heal_hp
        if self.hp > self.max_hp:
            self.hp = self.max_hp


# Завдання 2
# Створіть дочірній клас Paladin
# Методи:
#  attack() – наносить 4*strength урону та зменшує mana на
# 5, якщо недостатньо, то наносить strength урону
#  shield() – збільшує стат defense на 4+level
#  unshield() – зменшує стат defense на 4+level
#  heal_ally(ally) – лікує союзника на 5 + 2*level + 0.5*mana

class Paladin(Character):
    def attack(self):
        if self.mana >= 5:
            dam = 4 * self.strength
            self.mana -= 5
        else:
            dam = self.strength
        return dam


    def shield(self):
        self.defense += 4 + self.level

    def unshield(self):
        self.defense -= 4 + self.level

    def heal_ally(self, ally):
        heal_hp = 5 + 2*self.level + 0.5*self.mana

        ally.heal(heal_hp)

paladin1 = Paladin("Ivan", 100, 6, 5, 5, 3, 6, 5)
paladin2 = Character("Igor", 100, 6, 5, 5, 3, 6, 5)

paladin2.take_damage(10)

print(paladin2.hp)

paladin1.heal_ally(paladin2)

print(paladin2.hp)

# Завдання 3
# Створіть дочірній клас Mage
# Методи:
#  attack() – наносить 3*intelligence+4 урону та зменшує
# mana на 3, якщо недостатньо, то не наносить урону
#  fireball() – наносить 2*intelligence+3 урону по області та
# зменшує mana на 5, якщо недостатньо, то не наносить
# урону
#  heal_ally(ally) – лікує союзника на 3 + level +
# 3*intelligence
class Mage(Character):

    def attack(self):
        if self.mana >= 3:
            dem = 4 +3* self.intelligence
            self.mana -= 3
            return  dem
        else:
            return 0


    def fireball(self):
        if self.mana >= 5:
            dem = 3 +2 * self.intelligence
            self.mana -= 5
            return  dem
        else:
            return 0

    def heal_ally(self, ally):
        heal.hp = 3 + self.level + 3*self.intelligence
        ally.heal(heal_hp)






# Завдання 4
# Створіть дочірній клас Warrior
# Методи:
#  attack() – наносить 4*strength+3 урону
#  power_strike(enemies) – проходить по списку ворогів:
# якщо їхній рівень менший за рівень персонажа, то
# знищує його повністю
# Завдання 5
# Створіть дочірній клас Rogue
# Методи:
#  attack() – наносить strength+level урону

