-- CREATE DATABASE Academy;

-- CREATE TABLE Departments (
--     Id SERIAL PRIMARY KEY,
--     Financing NUMERIC(18,2) NOT NULL CHECK (Financing >= 0),
--     Name VARCHAR(100) NOT NULL UNIQUE CHECK (length(Name) > 0)
-- );

-- CREATE TABLE Faculties (
--     Id SERIAL PRIMARY KEY,
--     Dean VARCHAR(100) NOT NULL CHECK (length(Dean) > 0),
--     Name VARCHAR(100) NOT NULL UNIQUE CHECK (length(Name) > 0)
-- );

-- CREATE TABLE Groups (
--     Id SERIAL PRIMARY KEY,
--     Name VARCHAR(100) NOT NULL UNIQUE CHECK (length(Name) > 0),
--     Rating NUMERIC(2,1) NOT NULL CHECK (Rating >= 0 AND Rating <= 5),
--     Year INTEGER NOT NULL CHECK (Year BETWEEN 1 AND 5)
-- );

-- CREATE TABLE Teachers (
--     Id SERIAL PRIMARY KEY,
--     EmploymentDate DATE NOT NULL CHECK (EmploymentDate >= DATE '1990-01-01'),
--     IsAssistant bit(1) NOT NULL DEFAULT B'0',
--     IsProfessor bit(1) NOT NULL DEFAULT B'0',
--     Name VARCHAR(100) NOT NULL CHECK (length(Name) > 0),
--     Position VARCHAR(100) NOT NULL CHECK (length(Position) > 0),
--     Premium NUMERIC(10,2) NOT NULL DEFAULT 0 CHECK (Premium >= 0),
--     Salary NUMERIC(10,2) NOT NULL CHECK (Salary > 0),
--     Surname VARCHAR(100) NOT NULL CHECK (length(Surname) > 0)
-- );



-- Departments
-- INSERT INTO Departments (Financing, Name) VALUES
--     (150000.00, 'Mathematics'),
--     (100000.00, 'Physics'),
--     (200000.00, 'Chemistry'),
--     (120000.00, 'Computer Science'),
--     (180000.00, 'Biology');

-- Faculties
-- INSERT INTO Faculties (Dean, Name) VALUES
--     ('Ivanov Ivan Ivanovich', 'Natural Sciences'),
--     ('Petrova Elena Sergeevna', 'Technical Sciences'),
--     ('Sidorov Alexey Petrovich', 'Liberal Arts'),
--     ('Smirnova Olga Dmitrievna', 'Medicine'),
--     ('Lebedev Oleg Yuryevich', 'Business and Economics');

-- Groups
-- INSERT INTO Groups (Name, Rating, Year) VALUES
--     ('CS-101', 4.5, 1),
--     ('BIO-201', 3.9, 2),
--     ('CHEM-301', 4.8, 3),
--     ('MATH-401', 5.0, 4),
--     ('PHY-501', 4.2, 5);

-- Teachers
-- INSERT INTO Teachers (EmploymentDate, IsAssistant, IsProfessor, Name, Position, Premium, Salary, Surname) VALUES
--     ('1992-03-15', B'1', B'0', 'Sergey',  'Assistant',       10000, 45000, 'Morozov'),
--     ('1995-09-11', B'0', B'1', 'Natalia', 'Professor',       12000, 70000, 'Popova'),
--     ('2001-02-20', B'1', B'0', 'Dmitry',  'Senior Lecturer',  8000, 50000, 'Petrov'),
--     ('2010-08-29', B'0', B'0', 'Anna',    'Lecturer',         5000, 35000, 'Ivanova'),
--     ('2015-05-12', B'0', B'1', 'Oleg',    'Head of Dept.',   15000, 80000, 'Smirnov');

-- 1. Вывести таблицу кафедр, но расположить её поля в обратном порядке
-- SELECT Name, Financing
-- FROM Departments;

-- Вывести названия групп и их рейтинги с уточнением имен полей именем таблицы
-- SELECT Groups.Name AS "Groups.Name", Groups.Rating AS "Groups.Rating"
-- FROM Groups;

-- Вывести для преподавателей их фамилию, процент ставки по отношению к надбавке и процент ставки
-- SELECT
--     Surname,
--     (Salary * 100.0 / Premium) AS "Salary_Percent_to_Premium",
--     (Salary * 100.0 / (Salary + Premium)) AS "Salary_Percent_of_Total"
-- FROM Teachers;

-- Вывести названия кафедр, фонд финансирования которых меньше 11000 или больше 25000.
-- SELECT Name
-- FROM Departments
-- WHERE Financing < 11000 OR Financing > 25000;

--  Вывести названия факультетов кроме факультета “Computer Science”.
-- SELECT Name
-- FROM Faculties
-- WHERE Name <> 'Computer Science';


--  Вывести фамилии и должности преподавателей, которые не являются профессорами.
-- SELECT Surname, Position
-- FROM Teachers
-- WHERE Position <> 'Professor';

-- Вывести фамилии, должности, ставки и надбавки ассистентов,
-- у которых надбавка в диапазоне от 160 до 550.
-- SELECT Surname, Position, Salary, Premium
-- FROM Teachers
-- WHERE Position = 'Assistant' AND Premium BETWEEN 160 AND 550;

-- Вывести фамилии и ставки ассистентов.
-- SELECT Surname, Salary
-- FROM Teachers
-- WHERE Position = 'Assistant'

-- Вывести фамилии и должности преподавателей, которые были приняты на работу до 01.01.2000.
-- SELECT Surname, Position
-- FROM Teachers
-- WHERE DateOfAppointment < '2000-01-01';


-- Вывести названия кафедр, которые в алфавитном порядке первыми идут до кафедры “Management”. Выводимое поле должно иметь название “Name of Department”.

-- SELECT Name AS "Name of Department"
-- FROM Departments
-- WHERE Name < 'Management';
