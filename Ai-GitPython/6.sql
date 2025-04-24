CREATE TABLE Curators(
	ID SERIAL NOT NULL PRIMARY KEY,
	Name VARCHAR NOT NULL CHECK(Name !=''),
	Surname VARCHAR NOT NULL CHECK(Surname !='')
	)

-- Кафедри (Departments)
--  ■ Ідентифікатор (Id). Унікальний ідентифікатор кафедри.
--  ▷ Тип даних — int.
--  ▷ Автоприріст.
--  ▷ Не містить null-значення.
--  ▷ Первинний ключ.
--  ■ Фінансування (Financing). Фонд фінансування кафедри.
--  ▷ Тип даних — DECIMAL(10, 2).
--  ▷ Не містить null-значення.
--  ▷ Не може бути менше, ніж 0.
--  ▷ Значення за замовчуванням — 0.
--  ■ Назва (Name). Назва кафедри.
--  ▷ Тип даних — varchar(100).
--  ▷ Не містить null-значення.
--  ▷ Не може бути порожньою.
--  ▷ Має бути унікальною.
--  ■ Ідентифікатор факультету (FacultyId). Факультет, до складу 
-- якого належить кафедра.
--  ▷ Тип даних — int.
--  ▷ Не містить null-значення.
--  ▷ Зовнішній ключ.


CREATE TABLE Departments (
    ID SERIAL NOT NULL PRIMARY KEY,
    Financing DECIMAL(10, 2) NOT NULL DEFAULT 0 CHECK (Financing >= 0), 
    Name VARCHAR(100) NOT NULL UNIQUE CHECK (Name != ''),
    FacultyId INT NOT NULL, 
    FOREIGN KEY (FacultyId) REFERENCES Faculties(Id)
	);

INSERT INTO Departments (Financing, Name, FacultyId) VALUES
(10000.00, 'Department of Mathematics', 1),
(12000.00, 'Department of Physics', 2),
(15000.00, 'Department of Computer Science', 3),
(11000.00, 'Department of Biology', 4),
(13000.00, 'Department of English Literature', 5),
(9000.00, 'Department of Philosophy', 6),
(14000.00, 'Department of Chemistry', 7),
(16000.00, 'Department of Economics', 8),
(8000.00, 'Department of Political Science', 9),
(11000.00, 'Department of History', 10);

UPDATE Departments
SET Financing = 120000.00
WHERE Name = 'Department of Biology';


-- Факультети (Faculties)
--  ■ Ідентифікатор (Id). Унікальний ідентифікатор 
-- факультету.
--  ▷ Тип даних — int.
--  ▷ Автоприріст.
--  ▷ Не містить null-значення.
--  ▷ Первинний ключ.
--  ■ Фінансування (Financing). Фонд фінансування факультету.
--  ▷ Тип даних — DECIMAL(10, 2).
--  ▷ Не містить null-значення.
--  ▷ Не може бути менше, ніж 0.
--  ▷ Значення за замовчуванням — 0.
--  ■ Назва (Name). Назва факультету.
--  ▷ Тип даних — varchar(100).
--  ▷ Не містить null-значення.
--  ▷ Не може бути порожньою.
--  ▷ Має бути унікальною.


ALTER TABLE Faculties
   ADD COLUMN Financing DECIMAL(10, 2) NOT NULL CHECK (Financing >= 0) DEFAULT 0;

UPDATE Faculties
SET Financing = 70000.00
WHERE NAME_FACULTIES = 'Faculty of Engineering';

-- Update Financing for Faculty of Science
UPDATE Faculties
SET Financing = 65000.00
WHERE NAME_FACULTIES = 'Faculty of Science';

-- Update Financing for Faculty of Arts
UPDATE Faculties
SET Financing = 50000.00
WHERE NAME_FACULTIES = 'Faculty of Arts';

-- Update Financing for Faculty of Business
UPDATE Faculties
SET Financing = 60000.00
WHERE NAME_FACULTIES = 'Faculty of Business';

-- Update Financing for Faculty of Education
UPDATE Faculties
SET Financing = 55000.00
WHERE NAME_FACULTIES = 'Faculty of Education';

-- Update Financing for Faculty of Medicine
UPDATE Faculties
SET Financing = 70000.00
WHERE NAME_FACULTIES = 'Faculty of Medicine';

-- Update Financing for Faculty of Law
UPDATE Faculties
SET Financing = 45000.00
WHERE NAME_FACULTIES = 'Faculty of Law';

-- Update Financing for Faculty of Computer Science
UPDATE Faculties
SET Financing = 75000.00
WHERE NAME_FACULTIES = 'Faculty of Computer Science';

-- Update Financing for Faculty of Architecture
UPDATE Faculties
SET Financing = 50000.00
WHERE NAME_FACULTIES = 'Faculty of Architecture';

-- Update Financing for Faculty of Social Sciences
UPDATE Faculties
SET Financing = 48000.00
WHERE NAME_FACULTIES = 'Faculty of Social Sciences';

-- Update Financing for Faculty of Environmental Studies
UPDATE Faculties
SET Financing = 46000.00
WHERE NAME_FACULTIES = 'Faculty of Environmental Studies';

-- Update Financing for Faculty of Pharmacy
UPDATE Faculties
SET Financing = 62000.00
WHERE NAME_FACULTIES = 'Faculty of Pharmacy';

-- Update Financing for Faculty of Public Health
UPDATE Faculties
SET Financing = 55000.00
WHERE NAME_FACULTIES = 'Faculty of Public Health';

-- Update Financing for Faculty of Theology
UPDATE Faculties
SET Financing = 40000.00
WHERE NAME_FACULTIES = 'Faculty of Theology';

-- Update Financing for Faculty of Fine Arts
UPDATE Faculties
SET Financing = 38000.00
WHERE NAME_FACULTIES = 'Faculty of Fine Arts';

-- Update Financing for Faculty of Veterinary Medicine
UPDATE Faculties
SET Financing = 70000.00
WHERE NAME_FACULTIES = 'Faculty of Veterinary Medicine';

-- Update Financing for Faculty of Journalism
UPDATE Faculties
SET Financing = 45000.00
WHERE NAME_FACULTIES = 'Faculty of Journalism';

-- Update Financing for Faculty of Dentistry
UPDATE Faculties
SET Financing = 65000.00
WHERE NAME_FACULTIES = 'Faculty of Dentistry';

-- Update Financing for Faculty of Agriculture
UPDATE Faculties
SET Financing = 50000.00
WHERE NAME_FACULTIES = 'Faculty of Agriculture';

-- Update Financing for Faculty of Linguistics
UPDATE Faculties
SET Financing = 47000.00
WHERE NAME_FACULTIES = 'Faculty of Linguistics';

SELECT *
FROM Faculties 

--  ¾Групи (Groups)
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
--  ■ Курс (Year). Курс (рік), на якому навчається група.
--  ▷ Тип даних — int.
--   ▷ Не містить null-значення.
--  ▷ Має бути в діапазоні від 1 до 5.
--  ■ Ідентифікатор кафедри (DepartmentId). Кафедра, до складу
--  якої належить група.
--  ▷ Тип даних — int.
--  ▷ Не містить null-значення.
--  ▷ Зовнішній ключ.
DROP TABLE GROUPS_ACAD

CREATE TABLE Groups (
    ID SERIAL NOT NULL PRIMARY KEY,
    Name VARCHAR(10) NOT NULL UNIQUE CHECK (Name != ''), 
    Year INT NOT NULL CHECK (Year >= 1 AND Year <= 5),
    DepartmentId INT NOT NULL, 
    FOREIGN KEY (DepartmentId) REFERENCES Departments(Id) 
);

INSERT INTO Groups (Name, Year, DepartmentId) VALUES
('Group1', 1, 1),
('Group2', 2, 1),
('Group3', 3, 2),
('Group4', 4, 2),
('Group5', 5, 3),
('Group6', 1, 3),
('Group7', 2, 4),
('Group8', 3, 4),
('Group9', 4, 5),
('Group10', 5, 5);




--  ¾Групи та куратори (GroupsCurators)
--  ■ Ідентифікатор (Id). Унікальний ідентифікатор групи та
--  куратора.
--  ▷ Тип даних — int.
--  ▷ Автоприріст.
--  ▷ Не містить null-значення.
--  ▷ Первинний ключ.
--  ■ Ідентифікатор куратора (CuratorId). Куратор.
--  ▷ Тип даних — int.
--  ▷ Не містить null-значення.
--  ▷ Зовнішній ключ.
--  ■ Ідентифікатор групи (GroupId). Група.
--  ▷ Тип даних — int.
--  ▷ Не містить null-значення.
--  ▷ Зовнішній ключ.
CREATE TABLE GroupsCurators(
    ID SERIAL NOT NULL PRIMARY KEY,
    CuratorId INT NOT NULL, 
    GroupId INT NOT NULL, 
    FOREIGN KEY (CuratorId) REFERENCES Curators(Id), 
    FOREIGN KEY (GroupId) REFERENCES Groups(Id) 
);


--  ¾Групи та лекції (GroupsLectures)
--  ■ Ідентифікатор (Id). Унікальний ідентифікатор групи та
--  лекції.
--  ▷ Тип даних — int.
--  ▷ Автоприріст.
--  ▷ Не містить null-значення.
--  ▷ Первинний ключ.
--   Ідентифікатор групи (GroupId). Група.
--  ▷ Тип даних — int.
--  ▷ Не містить null-значення.
--  ▷ Зовнішній ключ.
--  ■ Ідентифікатор лекції (LectureId). Лекція.
--  ▷ Тип даних — int.
--  ▷ Не містить null-значення.
--  ▷ Зовнішній ключ.
CREATE TABLE GroupsLectures(
	ID SERIAL NOT NULL PRIMARY KEY,
	GroupId INT NOT NULL,
	FOREIGN KEY (GroupId) REFERENCES Groups(Id),
	LectureId INT NOT NULL,
	FOREIGN KEY (LectureId) REFERENCES Lectures(Id)
)

SELECT *
FROM GroupsLectures

--  ¾Лекції (Lectures)
--  ■ Ідентифікатор (Id). Унікальний ідентифікатор лекції.
--  ▷ Тип даних — int.
--  ▷ Автоприріст.
--  ▷ Не містить null-значення.
--  ▷ Первинний ключ.
--  ■ Аудиторія (LectureRoom). Аудиторія, в якій проходить 
-- лекція.
--  ▷ Тип даних — varchar(max).
--  ▷ Не містить null-значення.
--  ▷ Не може бути порожньою.
--  ■ Ідентифікатор предмета (SubjectId). Предмет, з якого чи
-- тається лекція.
--  ▷ Тип даних — int.
--  ▷ Не містить null-значення.
--  ▷ Зовнішній ключ.
--  ■ Ідентифікатор викладача (TeacherId). Викладач, який веде 
-- лекцію.
--  ▷ Тип даних — int.
--  ▷ Не містить null-значення.
--  ▷ Зовнішній ключ.
CREATE TABLE Lectures(
	ID SERIAL NOT NULL PRIMARY KEY,
	LectureRoom VARCHAR NOT NULL CHECK(LectureRoom !=''),
	SubjectId INT NOT NULL,
	FOREIGN KEY (SubjectId) REFERENCES Subjects(Id),
	TeacherId INT NOT NULL,
	FOREIGN KEY (TeacherId) REFERENCES TEACHER(ID)
)

INSERT INTO Lectures (LectureRoom, SubjectId, TeacherId) VALUES
('Room 101', 1, 1), -- Mathematics, Teacher 1
('Room 102', 2, 2), -- Physics, Teacher 2
('Room 103', 3, 3), -- Computer Science, Teacher 3
('Room 104', 4, 4), -- Biology, Teacher 4
('Room 105', 5, 5), -- English Literature, Teacher 5
('Room 106', 6, 6), -- Philosophy, Teacher 6
('Room 107', 7, 7), -- Chemistry, Teacher 7
('Room 108', 8, 8), -- Economics, Teacher 8
('Room 109', 9, 9), -- Political Science, Teacher 9
('Room 110', 10, 10), -- History, Teacher 10
('Room 111', 1, 11), -- Mathematics, Teacher 11
('Room 112', 2, 12), -- Physics, Teacher 12
('Room 113', 3, 13), -- Computer Science, Teacher 13
('Room 114', 4, 14), -- Biology, Teacher 14
('Room 115', 5, 15), -- English Literature, Teacher 15
('Room 116', 6, 16), -- Philosophy, Teacher 16
('Room 117', 7, 17), -- Chemistry, Teacher 17
('Room 118', 8, 18), -- Economics, Teacher 18
('Room 119', 9, 19), -- Political Science, Teacher 19
('Room 120', 10, 20); -- History, Teacher 20



SELECT *
FROM Subjects

-- ¾Предмети (Subjects)
--  ■ Ідентифікатор (Id). Унікальний ідентифікатор предмета.
--  ▷ Тип даних — int.
--  ▷ Автоприріст.
--  ▷ Не містить null-значення.
--  ▷ Первинний ключ.
--  ■ Назва (Name). Назва предмета.
--  ▷ Тип даних — varchar(100).
--  ▷ Не містить null-значення.
--  ▷ Не може бути порожньою.
--  ▷ Має бути унікальною.
CREATE TABLE Subjects(
	ID SERIAL NOT NULL PRIMARY KEY,
	Name VARCHAR NOT NULL UNIQUE
)

INSERT INTO Subjects (Name) VALUES
('Mathematics'),
('Physics'),
('Computer Science'),
('Biology'),
('English Literature'),
('Philosophy'),
('Chemistry'),
('Economics'),
('Political Science'),
('History');

--  ¾Викладачі (Teachers)
--  ■ Ідентифікатор (Id). Унікальний ідентифікатор 
-- викладача.
--  ▷ Тип даних — int.
--  ▷ Автоприріст.
--  ▷ Не містить null-значення.
--  ▷ Первинний ключ.
--  ■ Ім’я (Name). Ім’я викладача.
--  ▷ Тип даних — varchar(max).
--  ▷ Не містить null-значення.
--  ▷ Не може бути порожньою.
--  ■ Ставка (Salary). Ставка викладача.
--  ▷ Тип даних — DECIMAL(10, 2).
--  ▷ Не містить null-значення.
--  ▷ Не може бути меншою або дорівнювати 0.
--  ■ Прізвище (Surname). Прізвище викладача.
--  ▷ Тип даних — varchar(max).
--  ▷ Не містить null-значення.
--  ▷ Не може бути порожнє.

SELECT *
FROM TEACHER


-- Виведіть усі можливі пари рядків викладачів і груп.
SELECT
    T.Name, T.Surname, G.Name, G.Year
FROM TEACHER T, Groups G;

-- Виведіть назви факультетів, фонд фінансування кафедр
--  яких перевищує фонд фінансування факультету.
SELECT Facu.NAME_FACULTIES, D.Financing
FROM Faculties Facu JOIN Departments D ON Facu.ID = D.FacultyId
WHERE D.Financing > Facu.Financing;

-- Виведіть прізвища викладачів і назви факультетів, на яких
--  вони читають лекції.
SELECT T.Surname, F.NAME_FACULTIES
FROM Lectures L JOIN Teacher T ON L.TeacherId = T.ID
JOIN Departments D ON L.SubjectId = D.ID
JOIN Faculties F ON D.FacultyId = F.ID;


-- Виведіть назви кафедр і назви груп, які до них належать.
SELECT D.Name, G.Name
FROM Groups G JOIN Departments D ON G.DepartmentId = D.ID;

-- Виведіть назви предметів, які викладає викладач «Brown 
--  Alice».
SELECT S.Name
FROM Lectures L JOIN Teacher T ON L.TeacherId = T.ID
JOIN Subjects S ON L.SubjectId = S.ID
WHERE T.Name = 'Alice' AND T.Surname = 'Brown';
 