-- Кафедри (Departments)

--  ■ Ідентифікатор (Id). Унікальний ідентифікатор кафедри.
--  ▷ Тип даних — int.
--  ▷ Автоприріст.
--  ▷ Не містить null-значення.
--  ▷ Первинний ключ.
--  ■ Фінансування (Financing). Фонд фінансування кафедри.
--  ▷ Тип даних — money.
--  ▷ Не містить null-значення.
--  ▷ Не може бути менше, ніж 0.
--  ▷ Значення за замовчуванням — 0.
--  ■ Назва (Name). Назва кафедри.
--  ▷ Тип даних — varchar(100).
--  ▷ Не містить null-значення.
--  ▷ Не може бути порожньою.
 -- ▷ Має бути унікально
CREATE TABLE Departments (
    ID  SERIAL NOT NULL PRIMARY KEY,
    FINANCING MONEY NOT NULL ,
    NAME_DEPARTMENT VARCHAR(100) NOT NULL UNIQUE CHECK (NAME_DEPARTMENT != '')
)


INSERT INTO Departments (FINANCING, NAME_DEPARTMENT) VALUES (100000.00, 'Human Resources');
INSERT INTO Departments (FINANCING, NAME_DEPARTMENT) VALUES (250000.00, 'Finance');
INSERT INTO Departments (FINANCING, NAME_DEPARTMENT) VALUES (150000.00, 'Marketing');
INSERT INTO Departments (FINANCING, NAME_DEPARTMENT) VALUES (300000.00, 'Research and Development');
INSERT INTO Departments (FINANCING, NAME_DEPARTMENT) VALUES (120000.00, 'Customer Service');
INSERT INTO Departments (FINANCING, NAME_DEPARTMENT) VALUES (200000.00, 'Sales');
INSERT INTO Departments (FINANCING, NAME_DEPARTMENT) VALUES (175000.00, 'Legal');
INSERT INTO Departments (FINANCING, NAME_DEPARTMENT) VALUES (220000.00, 'IT Services');
INSERT INTO Departments (FINANCING, NAME_DEPARTMENT) VALUES (180000.00, 'Procurement');
INSERT INTO Departments (FINANCING, NAME_DEPARTMENT) VALUES (195000.00, 'Operations');
INSERT INTO Departments (FINANCING, NAME_DEPARTMENT) VALUES (210000.00, 'Engineering');
INSERT INTO Departments (FINANCING, NAME_DEPARTMENT) VALUES (160000.00, 'Quality Assurance');
INSERT INTO Departments (FINANCING, NAME_DEPARTMENT) VALUES (110000.00, 'Administration');
INSERT INTO Departments (FINANCING, NAME_DEPARTMENT) VALUES (145000.00, 'Public Relations');
INSERT INTO Departments (FINANCING, NAME_DEPARTMENT) VALUES (130000.00, 'Facilities Management');
INSERT INTO Departments (FINANCING, NAME_DEPARTMENT) VALUES (125000.00, 'Training and Development');
INSERT INTO Departments (FINANCING, NAME_DEPARTMENT) VALUES (140000.00, 'Security');
INSERT INTO Departments (FINANCING, NAME_DEPARTMENT) VALUES (155000.00, 'Product Management');
INSERT INTO Departments (FINANCING, NAME_DEPARTMENT) VALUES (135000.00, 'Data Analytics');
INSERT INTO Departments (FINANCING, NAME_DEPARTMENT) VALUES (165000.00, 'Business Development');


-- ¾Факультети (Faculties)
--  ■ Ідентифікатор (Id). Унікальний ідентифікатор факультету.
--  ▷ Тип даних — int.
--  ▷ Автоприріст.
--  ▷ Не містить null-значення.
--  ▷ Первинний ключ.
--  ■ Декан (Dean). Декан факультету.
--  ▷ Тип даних — varchar(255).
--  ▷ Не містить null-значення.
--  ▷ Не може бути порожнім.
 -- ■ Назва (Name). Назва факультету.
 -- ▷ Тип даних — varchar(100).
 -- ▷ Не містить null-значення.
 -- ▷ Не може бути порожньою.
 -- ▷ Має бути унікальною

 
CREATE TABLE FACULTIES(
ID  SERIAL PRIMARY KEY,
DEAN VARCHAR(255) NOT NULL CHECK(DEAN !=''),
NAME_FACULTIES VARCHAR(100) NOT NULL UNIQUE CHECK(NAME_FACULTIES !='')
)

INSERT INTO FACULTIES (DEAN, NAME_FACULTIES) VALUES ('Dr. Emily Carter', 'Faculty of Engineering');
INSERT INTO FACULTIES (DEAN, NAME_FACULTIES) VALUES ('Dr. John Smith', 'Faculty of Science');
INSERT INTO FACULTIES (DEAN, NAME_FACULTIES) VALUES ('Dr. Sarah Johnson', 'Faculty of Arts');
INSERT INTO FACULTIES (DEAN, NAME_FACULTIES) VALUES ('Dr. Michael Brown', 'Faculty of Business');
INSERT INTO FACULTIES (DEAN, NAME_FACULTIES) VALUES ('Dr. Laura Wilson', 'Faculty of Education');
INSERT INTO FACULTIES (DEAN, NAME_FACULTIES) VALUES ('Dr. James Davis', 'Faculty of Medicine');
INSERT INTO FACULTIES (DEAN, NAME_FACULTIES) VALUES ('Dr. Patricia Martinez', 'Faculty of Law');
INSERT INTO FACULTIES (DEAN, NAME_FACULTIES) VALUES ('Dr. Robert Garcia', 'Faculty of Computer Science');
INSERT INTO FACULTIES (DEAN, NAME_FACULTIES) VALUES ('Dr. Linda Rodriguez', 'Faculty of Architecture');
INSERT INTO FACULTIES (DEAN, NAME_FACULTIES) VALUES ('Dr. Charles Anderson', 'Faculty of Social Sciences');
INSERT INTO FACULTIES (DEAN, NAME_FACULTIES) VALUES ('Dr. Susan Lee', 'Faculty of Environmental Studies');
INSERT INTO FACULTIES (DEAN, NAME_FACULTIES) VALUES ('Dr. William Hernandez', 'Faculty of Pharmacy');
INSERT INTO FACULTIES (DEAN, NAME_FACULTIES) VALUES ('Dr. Karen Thomas', 'Faculty of Public Health');
INSERT INTO FACULTIES (DEAN, NAME_FACULTIES) VALUES ('Dr. Kevin Moore', 'Faculty of Theology');
INSERT INTO FACULTIES (DEAN, NAME_FACULTIES) VALUES ('Dr. Barbara Martin', 'Faculty of Fine Arts');
INSERT INTO FACULTIES (DEAN, NAME_FACULTIES) VALUES ('Dr. Jason Clark', 'Faculty of Veterinary Medicine');
INSERT INTO FACULTIES (DEAN, NAME_FACULTIES) VALUES ('Dr. Jennifer Lewis', 'Faculty of Journalism');
INSERT INTO FACULTIES (DEAN, NAME_FACULTIES) VALUES ('Dr. Matthew Walker', 'Faculty of Dentistry');
INSERT INTO FACULTIES (DEAN, NAME_FACULTIES) VALUES ('Dr. Angela Hall', 'Faculty of Agriculture');
INSERT INTO FACULTIES (DEAN, NAME_FACULTIES) VALUES ('Dr. Brian Allen', 'Faculty of Linguistics');


-- Групи (Groups)
--  ■ Ідентифікатор (Id). Унікальний ідентифікатор групи.
--  ▷ Тип даних — int.
--  ▷ Автоприріст.
--  ▷ Не містить null-значення.
--  ▷ Первинний ключ.
--  ■ Назва (Name). Назва групи.
--  ▷ Тип даних — varchar(10).
--  ▷ Не містить null-значення.
--  ▷ Не може бути порожньою.
--  ▷ Має бути унікальною.
--  ■ Рейтинг (Rating). Рейтинг групи.
--  ▷ Тип даних — int.
--  ▷ Не містить null-значення.
--  ▷ Має бути в діапазоні від 0 до 5.
--  ■ Курс (Year). Курс (рік), на якому навчається група.
--  ▷ Тип даних — int.
--  ▷ Не містить null-значення.
--  ▷ Має бути в діапазоні від 1 до 5

CREATE TABLE GROUPS_ACAD(
	ID SERIAL NOT NULL PRIMARY KEY,
	NAME VARCHAR(10) NOT NULL CHECK(NAME !=''),
	RATING INT NOT NULL CHECK( RATING >=1 AND RATING <=5),
	YEAR_GROUP INT NOT NULL CHECK( YEAR_GROUP >=2020 AND YEAR_GROUP <=2025)
	) 

INSERT INTO GROUPS_ACAD (NAME, RATING, YEAR_GROUP) VALUES ('GA101', 4, 2023);
INSERT INTO GROUPS_ACAD (NAME, RATING, YEAR_GROUP) VALUES ('GA102', 5, 2022);
INSERT INTO GROUPS_ACAD (NAME, RATING, YEAR_GROUP) VALUES ('GA103', 3, 2024);
INSERT INTO GROUPS_ACAD (NAME, RATING, YEAR_GROUP) VALUES ('GA104', 2, 2021);
INSERT INTO GROUPS_ACAD (NAME, RATING, YEAR_GROUP) VALUES ('GA105', 1, 2025);
INSERT INTO GROUPS_ACAD (NAME, RATING, YEAR_GROUP) VALUES ('GA106', 5, 2020);
INSERT INTO GROUPS_ACAD (NAME, RATING, YEAR_GROUP) VALUES ('GA107', 3, 2023);
INSERT INTO GROUPS_ACAD (NAME, RATING, YEAR_GROUP) VALUES ('GA108', 4, 2022);
INSERT INTO GROUPS_ACAD (NAME, RATING, YEAR_GROUP) VALUES ('GA109', 2, 2024);
INSERT INTO GROUPS_ACAD (NAME, RATING, YEAR_GROUP) VALUES ('GA110', 1, 2025);
INSERT INTO GROUPS_ACAD (NAME, RATING, YEAR_GROUP) VALUES ('GA111', 5, 2021);
INSERT INTO GROUPS_ACAD (NAME, RATING, YEAR_GROUP) VALUES ('GA112', 4, 2020);
INSERT INTO GROUPS_ACAD (NAME, RATING, YEAR_GROUP) VALUES ('GA113', 3, 2023);
INSERT INTO GROUPS_ACAD (NAME, RATING, YEAR_GROUP) VALUES ('GA114', 2, 2022);
INSERT INTO GROUPS_ACAD (NAME, RATING, YEAR_GROUP) VALUES ('GA115', 1, 2024);
INSERT INTO GROUPS_ACAD (NAME, RATING, YEAR_GROUP) VALUES ('GA116', 5, 2025);
INSERT INTO GROUPS_ACAD (NAME, RATING, YEAR_GROUP) VALUES ('GA117', 4, 2021);
INSERT INTO GROUPS_ACAD (NAME, RATING, YEAR_GROUP) VALUES ('GA118', 3, 2020);
INSERT INTO GROUPS_ACAD (NAME, RATING, YEAR_GROUP) VALUES ('GA119', 2, 2023);
INSERT INTO GROUPS_ACAD (NAME, RATING, YEAR_GROUP) VALUES ('GA120', 1, 2022);


-- 	Викладачі (Teachers)
--  ■ Ідентифікатор (Id). Унікальний ідентифікатор
--  викладача.
--  ▷ Тип даних — int.
--  ▷ Автоприріст.
--   ▷ Не містить null-значення.
--  ▷ Первинний ключ.
--  ■ Дата працевлаштування (EmploymentDate). Дата працев
-- лаштування викладача.
--  ▷ Тип даних — date.
--  ▷ Не містить null-значення.
--  ▷ Не може бути менше 01.01.1990.
--  ■ Асистент (IsAssistant). Чи є викладач асистентом.
--  ▷ Тип даних — bit.
--  ▷ Не містить null-значення.
--  ▷ Значення за замовчуванням — 0.
--  ■ Професор (IsProfessor). Чи є викладач професором.
--  ▷ Тип даних — bit.
--  ▷ Не містить null-значення.
--  ▷ Значення за замовчуванням — 0.
--  ■ Ім’я (Name). Ім’я викладача.
--  ▷ Тип даних — nvarchar(max).
--  ▷ Не містить null-значення.
--  ▷ Не може бути порожнє.
--  ■ Посада (Position). Посада викладача.
--  ▷ Тип даних — varchar(max).
--  ▷ Не містить null-значення.
--  ▷ Не може бути порожньою.
--  ■ Надбавка (Premium). Надбавка викладача.
--  ▷ Тип даних — money.
--  ▷ Не містить null-значення.
--  ▷ Не може бути менше, ніж 0.
--  ▷ Значення за замовчуванням — 0.
--  ■ Ставка (Salary). Ставка викладача
--   ▷ Тип даних — money.
--  ▷ Не містить null-значення.
--  ▷ Не може бути меншою або дорівнювати 0.
--  ■ Прізвище (Surname). Прізвище викладача.
--  ▷ Тип даних — varchar(max).
--  ▷ Не містить null-значення.
--  ▷ Не може бути порожнє.

DROP TABLE TEACHER

CREATE TABLE TEACHER(
	ID SERIAL NOT NULL PRIMARY KEY,
	EmploymentDate DATE NOT NULL CHECK( EmploymentDate <='01.01.1990'),
	IsAssistant BIT NOT NULL DEFAULT '0',
	IsProfessor BIT NOT NULL DEFAULT '0',
	Name VARCHAR NOT NULL CHECK(Name !=''),
	Surname VARCHAR(50) NOT NULL CHECK(Surname !=''),
	Position_TEACHER  VARCHAR NOT NULL,
	Premium  MONEY NOT NULL CHECK(Premium >= 0::MONEY) DEFAULT 0,
	Salary MONEY NOT NULL CHECK(Salary > 0::MONEY)	  
	)

INSERT INTO TEACHER (EmploymentDate, IsAssistant, IsProfessor, Name, Surname, Position_TEACHER, Premium, Salary) 
VALUES ('1985-06-12', B'1', B'0', 'Alice', 'Brown', 'Lecturer', 500.00, 3000.00);
INSERT INTO TEACHER (EmploymentDate, IsAssistant, IsProfessor, Name, Surname, Position_TEACHER, Premium, Salary) 
VALUES ('1980-03-22', B'0', B'1', 'John', 'Smith', 'Professor', 1500.00, 5500.00);
INSERT INTO TEACHER (EmploymentDate, IsAssistant, IsProfessor, Name, Surname, Position_TEACHER, Premium, Salary) 
VALUES ('1979-11-30', B'1', B'0', 'Mary', 'Johnson', 'Assistant Lecturer', 300.00, 2800.00);
INSERT INTO TEACHER (EmploymentDate, IsAssistant, IsProfessor, Name, Surname, Position_TEACHER, Premium, Salary) 
VALUES ('1987-07-15', B'0', B'1', 'James', 'Williams', 'Professor', 1000.00, 5000.00);
INSERT INTO TEACHER (EmploymentDate, IsAssistant, IsProfessor, Name, Surname, Position_TEACHER, Premium, Salary) 
VALUES ('1983-12-01', B'0', B'0', 'Patricia', 'Jones', 'Lecturer', 0.00, 3200.00);
INSERT INTO TEACHER (EmploymentDate, IsAssistant, IsProfessor, Name, Surname, Position_TEACHER, Premium, Salary) 
VALUES ('1984-02-14', B'1', B'0', 'Robert', 'Garcia', 'Assistant Lecturer', 450.00, 2900.00);
INSERT INTO TEACHER (EmploymentDate, IsAssistant, IsProfessor, Name, Surname, Position_TEACHER, Premium, Salary) 
VALUES ('1988-05-20', B'0', B'0', 'Linda', 'Martinez', 'Senior Lecturer', 800.00, 4000.00);
INSERT INTO TEACHER (EmploymentDate, IsAssistant, IsProfessor, Name, Surname, Position_TEACHER, Premium, Salary) 
VALUES ('1989-01-01', B'0', B'1', 'Michael', 'Rodriguez', 'Professor', 2000.00, 6000.00);
INSERT INTO TEACHER (EmploymentDate, IsAssistant, IsProfessor, Name, Surname, Position_TEACHER, Premium, Salary) 
VALUES ('1981-09-05', B'1', B'0', 'Barbara', 'Lee', 'Assistant Lecturer', 250.00, 2700.00);
INSERT INTO TEACHER (EmploymentDate, IsAssistant, IsProfessor, Name, Surname, Position_TEACHER, Premium, Salary) 
VALUES ('1982-10-10', B'0', B'1', 'Thomas', 'Walker', 'Professor', 1200.00, 5200.00);
INSERT INTO TEACHER (EmploymentDate, IsAssistant, IsProfessor, Name, Surname, Position_TEACHER, Premium, Salary) 
VALUES ('1986-08-09', B'0', B'0', 'Susan', 'Hall', 'Lecturer', 350.00, 3100.00);
INSERT INTO TEACHER (EmploymentDate, IsAssistant, IsProfessor, Name, Surname, Position_TEACHER, Premium, Salary) 
VALUES ('1980-12-25', B'1', B'0', 'Steven', 'Allen', 'Assistant Lecturer', 400.00, 2850.00);
INSERT INTO TEACHER (EmploymentDate, IsAssistant, IsProfessor, Name, Surname, Position_TEACHER, Premium, Salary) 
VALUES ('1978-06-18', B'0', B'1', 'Karen', 'Young', 'Professor', 1800.00, 5400.00);
INSERT INTO TEACHER (EmploymentDate, IsAssistant, IsProfessor, Name, Surname, Position_TEACHER, Premium, Salary) 
VALUES ('1985-03-01', B'1', B'0', 'Brian', 'Hernandez', 'Assistant Lecturer', 150.00, 2500.00);
INSERT INTO TEACHER (EmploymentDate, IsAssistant, IsProfessor, Name, Surname, Position_TEACHER, Premium, Salary) 
VALUES ('1984-11-22', B'0', B'0', 'Laura', 'King', 'Lecturer', 600.00, 3500.00);
INSERT INTO TEACHER (EmploymentDate, IsAssistant, IsProfessor, Name, Surname, Position_TEACHER, Premium, Salary) 
VALUES ('1982-04-17', B'0', B'1', 'Daniel', 'Scott', 'Professor', 1600.00, 5300.00);
INSERT INTO TEACHER (EmploymentDate, IsAssistant, IsProfessor, Name, Surname, Position_TEACHER, Premium, Salary) 
VALUES ('1981-07-30', B'0', B'0', 'Nancy', 'Green', 'Senior Lecturer', 700.00, 3900.00);
INSERT INTO TEACHER (EmploymentDate, IsAssistant, IsProfessor, Name, Surname, Position_TEACHER, Premium, Salary) 
VALUES ('1989-12-31', B'1', B'0', 'Edward', 'Adams', 'Assistant Lecturer', 200.00, 2650.00);
INSERT INTO TEACHER (EmploymentDate, IsAssistant, IsProfessor, Name, Surname, Position_TEACHER, Premium, Salary) 
VALUES ('1987-05-08', B'0', B'1', 'Donna', 'Nelson', 'Professor', 1300.00, 5100.00);
INSERT INTO TEACHER (EmploymentDate, IsAssistant, IsProfessor, Name, Surname, Position_TEACHER, Premium, Salary) 
VALUES ('1983-10-02', B'0', B'0', 'George', 'Baker', 'Lecturer', 0.00, 3000.00);

 1. Вивести таблицю кафедр, але розташувати її поля у зво
ротному порядку
SELECT * 
FROM DEPARTMENTS

SELECT 
    NAME_DEPARTMENT, 
    FINANCING, 
    ID
FROM 
    DEPARTMENTS

-- Вивести прізвища професорів, ставка яких перевищує 5000
SELECT *
FROM TEACHER

SELECT SURNAME
FROM TEACHER
WHERE SALARY >=5000::MONEY

-- Вивести прізвища та посади викладачів, які були прийняті 
-- на роботу до 01.01.2000
SELECT SURNAME, POSITION_TEACHER
FROM TEACHER
WHERE EMPLOYMENTDATE <='1980-07-30'

-- Вивести прізвища асистентів із зарплатою (сума ставки 
-- та надбавки) не більше 3500
SELECT SURNAME, Premium + Salary AS TOTAL
FROM TEACHER
WHERE IsAssistant ='1' AND Premium + Salary <= 3200::MONEY 

-- Вивести прізвища асистентів зі ставкою менше, ніж 2800 
-- або надбавкою менше, ніж 200
SELECT SURNAME, SALARY, PREMIUM
FROM TEACHER
WHERE IsAssistant ='1' AND (PREMIUM <=200::MONEY OR SALARY<= 2800::MONEY )

-- Вивести назви факультетів, окрім факультету «Computer
--  Science».

SELECT * 
FROM FACULTIES
WHERE NAME_FACULTIES != 'Faculty of Computer Science'







