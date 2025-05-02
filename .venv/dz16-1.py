# добавити нову людину
#  вивести людей, ім’я яких починається на певну літеру
#  вивести людей, які народитись після певної дати
#  вивести скільки людей живе у певній країні
from sqlalchemy import create_engine, Column, Integer, String, Sequence, Date
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import text
from datetime import datetime

import json
with open('config.json', 'r') as file:
    data = json.load(file)
    login = data['login']
    password = data['password']
#
db_url = f"postgresql+pg8000://{login}:{password}@localhost:5432/people"
engine = create_engine(db_url)

Base = declarative_base()



class People(Base):
    __tablename__ = 'people'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name = Column(String(30))
    surname = Column(String(30))
    city = Column(String(30))
    country = Column(String(30))
    date_dr = Column(Date)

    def repr(self):
        return (f"ID =(id={self.id}, name={self.name}, surname={self.surname},"
                f" city={self.city}, country={self.country}, birthday ={self.date_dr})")

Base.metadata.create_all(engine)
from datetime import date

people_list = [
    People(name="Олександр", surname="Шевченко", city="Київ", country="Україна", date_dr=date(1990, 5, 15)),
    People(name="Ірина", surname="Коваленко", city="Харків", country="Україна", date_dr=date(1985, 3, 10)),
    People(name="Андрій", surname="Мельник", city="Львів", country="Україна", date_dr=date(1993, 7, 8)),
    People(name="Світлана", surname="Іванова", city="Одеса", country="Україна", date_dr=date(1992, 1, 21)),
    People(name="Віктор", surname="Петренко", city="Дніпро", country="Україна", date_dr=date(1988, 9, 30)),
    People(name="Марія", surname="Гриценко", city="Запоріжжя", country="Україна", date_dr=date(1995, 11, 5)),
    People(name="Євген", surname="Сидоренко", city="Полтава", country="Україна", date_dr=date(1989, 6, 12)),
    People(name="Анна", surname="Ткаченко", city="Чернігів", country="Україна", date_dr=date(1991, 2, 28)),
    People(name="Дмитро", surname="Кузьменко", city="Вінниця", country="Україна", date_dr=date(1994, 4, 17)),
    People(name="Олена", surname="Литвин", city="Івано-Франківськ", country="Україна", date_dr=date(1987, 8, 23))
]

Session = sessionmaker(engine)
session = Session()
# session.add_all(people_list)
session.commit()

def command1():
    user_inp = input('введіть запит: ')

    query_sql = text(user_inp)

    # виконуємо запит
    result = session.execute(query_sql)
    rows = result.fetchall()

    for row in rows:
        print(row)

def new_people():
    print("Добавити нову людину")
    name_user = input(" Enter name: ")
    surname_user = input("enter surname: ")
    city_user = input("Enter city: ")
    country_user = input("Enter country: ")
    date_user = input("Enter date of birth (year-month-day):")
    year, month, day = map(int, date_user.strip().split('-'))
    date_dr = date(year, month, day)

    new_person = People(
        name=name_user,
        surname=surname_user,
        city=city_user,
        country=country_user,
        date_dr=date_dr
    )

    session.add(new_person)
    session.commit()

    print(f"Додано нового користувача з ID: {new_person.id}")

def people_begin_from_letter():
    print('Вивести людей, ім’я яких починається на певну літеру')
    letter = input("Введіть літеру, на яку починається ім’я: ").strip()
    if not letter:
        print("Ви не ввели літеру.")
        return

    query_sql = text("""
        SELECT *
        FROM people
        WHERE name ILIKE :pattern
    """)
    query_sql = text(user_inp)

    # виконуємо запит
    result = session.execute(query_sql)
    rows = result.fetchall()

    for row in rows:
        print(row)
    result = session.execute(query_sql, {"pattern": f"{letter}%"})
    rows = result.fetchall()

    if rows:
        for row in rows:
            print(row)
    else:
        print(f"Не знайдено людей, чиє ім’я починається на '{letter}'.")


def people_born_from():
    print('Вивести людей, які народилися після певної дати')
    date_input = input("Введіть дату у форматі YYYY-MM-DD: ").strip()

    date_obj = datetime.strptime(date_input, '%Y-%m-%d').date()
    print(date_obj)

    people = session.query(People).filter(People.date_dr >= date_obj).all()

    if people:
        print(f"Люди, народжені після {date_obj}:")
        for person in people:
            print(f"{person.id}: {person.name} {person.surname}, {person.city}, {person.country}, {person.date_dr}")
    else:
        print(f"Не знайдено людей, які народилися після {date_obj}.")
def people_leave_in_country():
    country_input = input("Введіть назву країни: ").strip()

    query_sql = text("""
           SELECT COUNT(*) 
           FROM people
           WHERE country = :country
       """)

    result = session.execute(query_sql, {'country': country_input})
    count = result.scalar()

    print(f"Кількість людей у {country_input}: {count}")

while True:
    print('1 - виконати запит')
    print('2 - добавити нову людину')
    print('3 - вивести людей, ім’я яких починається на певну літеру')
    print('4 - вивести людей, які народитись після певної дати')
    print('5 - вивести скільки людей живе у певній країні')
    command = input('введіть номер команди: ')

    if command == '1':
        command1()
    elif command == '2':
        new_people()
    elif command == '3':
        people_begin_from_letter()
    elif command == '4':
        people_born_from()
    elif command == '5':
        people_leave_in_country()

    else:
        break
#
#
