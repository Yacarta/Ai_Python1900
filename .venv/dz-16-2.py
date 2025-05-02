from sqlalchemy import create_engine, MetaData, insert, delete
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import text
import json

# завантажуємо логін та пароль
with open('config.json', 'r') as file:
    data = json.load(file)
    login = data['login']
    password = data['password']

# підключаємось до бд itstep
db_url = f"postgresql+pg8000://{login}:{password}@localhost:5432/academy"
engine = create_engine(db_url)

metadata = MetaData()
metadata.reflect(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

#вивести назви усіх кафедр
def  name_depart():
    query = f"""
    SELECT NAME
    FROM DEPARTMENTS
    """

    # виконати запит та обробити помилки
    try:
        query = text(query) #- закоментується для другого варіанту (делете)
        rows = session.execute(query)
        rows = rows.fetchall()
        session.commit()
    except Exception as err:
        print(f"Помилка {err}")

    for row in rows:
        print(row)

# вивести інформацію про всіх викладачів
def  show_teacher():
    query = f"""
    SELECT *
FROM TEACHER
    """
    try:
        query = text(query)
        rows = session.execute(query)
        rows = rows.fetchall()
        session.commit()
    except Exception as err:
        print(f"Помилка {err}")

    for row in rows:
        print(row)

##вивести назви предметів, які викладає конкретний  викладач
def  name_depart_teacher(name, surname):
    query = text("""
          SELECT s.Name AS subject_name
          FROM Subjects s
          JOIN Lectures l ON s.Id = l.SubjectId
          JOIN Teacher t ON l.TeacherId = t.ID
          WHERE t.Name = :name AND t.Surname = :surname
      """)

    result = session.execute(query, {'name': name, 'surname': surname})
    subjects = result.fetchall()

    if subjects:
        print(f"Предмети, які викладає {name} {surname}:")
        for row in subjects:
            print("-", row.subject_name)
    else:
        print(f"Викладач {name} {surname} не викладає жодного предмета або не знайдено.")

#вивести інформацію про всі навчальні групи
def  show_groups():
    query = f"""
    SELECT *
FROM GROUPS
    """
    try:
        query = text(query)
        rows = session.execute(query)
        rows = rows.fetchall()
        session.commit()
    except Exception as err:
        print(f"Помилка {err}")

    for row in rows:
        print(row)

def department_group():
    query = f"""
    SELECT D.Name, G.Name
    FROM Groups G JOIN Departments D
              ON G.DepartmentId = D.ID
      """

    # виконати запит та обробити помилки
    try:
        query = text(query)  # - закоментується для другого варіанту (делете)
        rows = session.execute(query)
        rows = rows.fetchall()
        session.commit()
    except Exception as err:
        print(f"Помилка {err}")

    for row in rows:
        print(row)

while True:
    print("1 - вивести назви усіх кафедр")
    print("2 - вивести назви предметів, які викладає конкретний  викладач")
    print("3 - вивести інформацію про всіх викладачів")
    print("4 -  вивести інформацію про всі навчальні групи")
    print("5 -  вивести назви кафедр і груп, які до них відносяться")


    command = input('Введіть номер команди: ')

    if command == '1':
        name_depart()
    elif command == '2':
        print('вивести назви предметів, які викладає конкретний  викладач')
        show_teacher()
        name = input("enter name: ")
        surname = input("enter surname: ")
        name_depart_teacher(name, surname)
    elif command == '3':
        show_teacher()
    elif command == '4':
        show_groups()
    elif command == '5':
        department_group()
    else:
        print('невірна команда')