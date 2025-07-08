-- DROP TABLE groups;
-- CREATE TABLE groups
-- (
-- 	id uuid NOT NULL,
-- 	name text,
-- 	form_ed text,

-- 	PRIMARY KEY(id)
-- );

-- INSERT INTO groups VALUES
-- 	('f689ef08-8d53-435f-8e93-40ea7080f717','Py42', 'очная'),
-- 	('760bdec6-3121-4451-91a3-d7f9c744a34c','P111', 'очная'),
-- 	('8e4c1d3f-0d51-4e5e-9fd2-ac4687a16e7f','BV12', 'очная'),
-- 	('19324a02-118a-4260-8a7d-dfad733779dd','GR15', 'очная');

-- select * from groups;

-- DROP TABLE students;
-- CREATE TABLE students 
-- (
-- 	id uuid NOT NULL,
-- 	name text, 
-- 	age int,
-- 	grade float,
-- 	gr uuid,

-- 	PRIMARY KEY(id),
-- 	FOREIGN KEY (gr)
-- 	REFERENCES groups (id) 
-- 	ON DELETE SET NULL
-- 	ON UPDATE CASCADE
-- );

-- INSERT INTO students VALUES
-- 	('2bada6e3-3d47-452c-b9a3-ee04bae70d4d','Дима',14,4.5,'760bdec6-3121-4451-91a3-d7f9c744a34c'),
-- 	('3a5d96c9-52a9-4c62-ab0f-e9cfda186f91','Лена',15,4.5,'f689ef08-8d53-435f-8e93-40ea7080f717'),
-- 	('da9e8e61-f91d-4b65-9980-8a8d9e8b48a9','Кирилл',16,4.5,'8e4c1d3f-0d51-4e5e-9fd2-ac4687a16e7f'),
--  ('f74b2a81-234e-4b61-be83-78eed1dc8b86','Маша',17,4.5,'19324a02-118a-4260-8a7d-dfad733779dd'),
-- 	('65cec917-427c-460c-b948-32e17fda5b76','Вася',18,4.5,'f689ef08-8d53-435f-8e93-40ea7080f717'),
-- 	('7798e403-5fd4-42d1-ae17-b6bfbbf206d7','Вика',17,4.5,'760bdec6-3121-4451-91a3-d7f9c744a34c'),
-- 	('61ec86c0-34b0-482f-9050-38ed832369fb','Настя',16,4.5,'8e4c1d3f-0d51-4e5e-9fd2-ac4687a16e7f'),
--  ('97f2511a-69c9-43ed-b556-587e643e4e23','Егор',15,4.5,'19324a02-118a-4260-8a7d-dfad733779dd'),
-- 	('542f1f23-2d82-4866-94d4-8c057278aaa3','Яков',14,4.5,'f689ef08-8d53-435f-8e93-40ea7080f717'),
--  ('0260fd33-543e-4456-b709-bfa7375d3b87','Наташа',19,4.5,'760bdec6-3121-4451-91a3-d7f9c744a34c'),
--  ('58d27133-dec2-4749-9e91-0bc25175c5c6','Леон',20,4.5,'8e4c1d3f-0d51-4e5e-9fd2-ac4687a16e7f')
--  ON CONFLICT (id)
--  DO UPDATE SET gr=EXCLUDED.gr;

-- select * from students;

-- select name,age,grade from students where age = 15 OR age = 17;
-- select students.name, age, grade, groups.name as group from students, groups 
-- 	where students.gr = groups.id;
-- select students.name as student, age, grade, groups.name as group 
-- 	from groups, students 
-- 	where groups.id = students.gr;

-- SELECT * FROM students;
-- SELECT * FROM groups;



-- ___________________________________________________________
-- 1 таблица customers  содержит: имя, контакты, номер телефона
-- [customers] --------< [проекты]
-- 2 таблица проекты содержит заказчика, начало и конец проекта,  название проекта
-- [проекты] --------< [tasks]
-- 3 таблица tasks содержит проеты начала и конец, ответсвенное лицо
-- [tasks] >-------< [програмисты]
-- 4 таблица програмисты содержит ФИО, день рождение, уровень навыков, номер телефона
-- 5 таблица project.man содержит ФИО, день рождение, номер телефона
-- [проекты] >------- [project.man]

-- запрос на вывод: заказчик, проект,project_man, tasks проекта,ФИО прогамиста,телефон програмиста
-- _________________________________________________________________________

-- CREATE TABLE customers (
--     id SERIAL PRIMARY KEY,
--     name VARCHAR(50) NOT NULL,
--     contact_info VARCHAR(50),
--     phone_number VARCHAR(50)
-- );


-- CREATE TABLE projects (
--     id SERIAL PRIMARY KEY,
--     customer_id INT NOT NULL,
--     name VARCHAR(50) NOT NULL,
--     start_date DATE,
--     end_date DATE,
--     project_manager_id INT,      
--     FOREIGN KEY (customer_id) REFERENCES customers(id),
--     FOREIGN KEY (project_manager_id) REFERENCES project_man(id)
-- );

-- CREATE TABLE tasks (
--     id SERIAL PRIMARY KEY,
--     project_id INT NOT NULL,
--     name VARCHAR(50) NOT NULL,
--     start_date DATE,
--     end_date DATE,
--     responsible_programmer_id INT,
--     FOREIGN KEY (project_id) REFERENCES projects(id),
--     FOREIGN KEY (responsible_programmer_id) REFERENCES programmers(id)
-- );

-- CREATE TABLE programmers (
--     id SERIAL PRIMARY KEY,
--     full_name VARCHAR(50)NOT NULL,
--     birth_date DATE,
--     skill_level VARCHAR(50),
--     phone_number VARCHAR(50)
-- );

-- CREATE TABLE task_programmer (
--     task_id INT NOT NULL,
--     programmer_id INT NOT NULL,
--     PRIMARY KEY (task_id, programmer_id),
--     FOREIGN KEY (task_id) REFERENCES tasks(id),
--     FOREIGN KEY (programmer_id) REFERENCES programmers(id)
-- );


-- CREATE TABLE project_man (
--     id SERIAL PRIMARY KEY,
--     full_name VARCHAR(255) NOT NULL,
--     birth_date DATE,
--     phone_number VARCHAR(50)
-- );
-- INSERT INTO customers (name, contact_info, phone_number) VALUES
-- ('Альфа', 'alpha@mail.com', '+7 900 111-22-33'),
-- ('Бета', 'beta@mail.com', '+7 900 222-33-44'),
-- ('Гамма', 'gamma@mail.com', '+7 900 333-44-55'),
-- ('Дельта', 'delta@mail.com', '+7 900 444-55-66'),
-- ('Эпсилон', 'epsilon@mail.com', '+7 900 555-66-77');

-- SELECT * FROM customers;
-- INSERT INTO project_man (full_name, birth_date, phone_number) VALUES
-- ('Иванов Иван Иванович', '1980-01-01', '+7 901 000-11-12'),
-- ('Петров Петр Петрович', '1975-03-10', '+7 901 000-11-13'),
-- ('Сидоров Сидор Сидорович', '1982-07-21', '+7 901 000-11-14'),
-- ('Алексеев Алексей Алексеевич', '1981-05-18', '+7 901 000-11-15'),
-- ('Егоров Егор Егорович', '1987-11-30', '+7 901 000-11-16');

-- SELECT * FROM project_man;

-- INSERT INTO programmers (full_name, birth_date, skill_level, phone_number) VALUES
-- ('Васильев Василий Васильевич', '1990-04-12', 'Senior', '+7 902 111-22-21'),
-- ('Федоров Федор Федорович', '1992-09-24', 'Middle', '+7 902 111-22-22'),
-- ('Григорьев Григорий Григорьевич', '1995-01-06', 'Junior', '+7 902 111-22-23'),
-- ('Юрьев Юрий Юрьевич', '1991-12-31', 'Senior', '+7 902 111-22-24'),
-- ('Семенов Семен Семенович', '1996-06-14', 'Middle', '+7 902 111-22-25');

-- SELECT * FROM programmers;

-- INSERT INTO projects (customer_id, name, start_date, end_date, project_manager_id) VALUES
-- (1, 'Разработка CRM',        '2023-01-10', '2023-06-01', 1),
-- (2, 'Мобильное приложение',  '2023-02-15', '2023-08-15', 2),
-- (3, 'Веб-сайт для ИП',       '2023-03-20', '2023-05-25', 3),
-- (4, 'Автоматизация склада',  '2023-04-01', '2023-09-30', 4),
-- (5, 'Электронная очередь',   '2023-05-12', '2023-12-01', 5);

-- SELECT * FROM projects;

-- INSERT INTO tasks (project_id, name, start_date, end_date, responsible_programmer_id) VALUES
-- (1, 'Создание базы данных',   '2023-01-15', '2023-01-30', 1),
-- (1, 'Разработка бекенда',     '2023-02-01', '2023-02-28', 2),
-- (2, 'UI дизайн',              '2023-02-20', '2023-03-15', 3),
-- (3, 'Верстка сайта',          '2023-03-25', '2023-04-05', 4),
-- (4, 'Интеграция с 1С',        '2023-04-10', '2023-05-10', 5);

-- SELECT * FROM tasks;

-- INSERT INTO task_programmer (task_id, programmer_id) VALUES
-- (1, 1),
-- (1, 2),
-- (2, 1),
-- (2, 3),
-- (3, 3),
-- (4, 4),
-- (4, 2),
-- (5, 5),
-- (5, 1),
-- (5, 4);

-- SELECT * FROM task_programmer;

-- SELECT
--     c.name AS customer_name,
--     p.name AS project_name,
--     pm.full_name AS project_manager_name,
--     t.name AS task_name,
--     pr.full_name AS programmer_name,
--     pr.phone_number AS programmer_phone
-- FROM
--     projects p
--     INNER JOIN customers c ON p.customer_id = c.id
--     INNER JOIN project_man pm ON p.project_manager_id = pm.id
--     INNER JOIN tasks t ON t.project_id = p.id
--     INNER JOIN programmers pr ON t.responsible_programmer_id = pr.id
-- ORDER BY
--     p.id, t.id;

-- SELECT
--     c.name AS customer_name,
--     p.name AS project_name,
--     pm.full_name AS project_manager_name,
--     t.name AS task_name,
--     pr.full_name AS programmer_name,
--     pr.phone_number AS programmer_phone
-- FROM
--     projects p
--     INNER JOIN customers c ON p.customer_id = c.id
--     INNER JOIN project_man pm ON p.project_manager_id = pm.id
--     INNER JOIN tasks t ON t.project_id = p.id
--     INNER JOIN programmers pr ON t.responsible_programmer_id = pr.id
-- WHERE
--     c.id IN (1)
-- -- ORDER BY
-- --     p.id, t.id;









