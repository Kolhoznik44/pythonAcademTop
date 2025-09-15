"""
необходимо для создания базы данных заказчики-проекты-програмисты создать программу в python которая будет давать
возможность пользователю взаимодействовать с базой данных из интерфейса программы (создать crud)

"""

import psycopg2 as PyPG

def connect_to_database():
    connectBD = PyPG.connect(
        dbname="crud",
        user="postgres",
        password="2575",
        host="localhost",
        port="5432",


    )
    return connectBD

def create_tables(conn):
    with conn.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS programmers (
                id SERIAL PRIMARY KEY,
                name VARCHAR(100) NOT NULL
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS projects (
                id SERIAL PRIMARY KEY,
                title VARCHAR(100) NOT NULL,
                customer_id INT REFERENCES customers(id) ON DELETE SET NULL,
                programmer_id INT REFERENCES programmers(id) ON DELETE SET NULL
            );
        """)
        conn.commit()

def add_customer(conn):
    name = input("Введите имя заказчика: ")
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO customers (name) VALUES (%s)", (name,))
        conn.commit()
        print("Заказчик добавлен.")

def add_programmer(conn):
    name = input("Введите имя программиста: ")
    with conn.cursor() as cursor:
        cursor.execute("INSERT INTO programmers (name) VALUES (%s)", (name,))
        conn.commit()
        print("Программист добавлен.")

def add_project(conn):
    title = input("Название проекта: ")
    customer_id = input("ID заказчика: ")
    programmer_id = input("ID программиста: ")
    with conn.cursor() as cursor:
        cursor.execute(
            "INSERT INTO projects (title, customer_id, programmer_id) VALUES (%s, %s, %s)",
            (title, customer_id if customer_id else None, programmer_id if programmer_id else None)
        )
        conn.commit()
        print("Проект добавлен.")

def list_customers(conn):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM customers")
        for row in cursor.fetchall():
            print(row)

def list_programmers(conn):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM programmers")
        for row in cursor.fetchall():
            print(row)

def list_projects(conn):
    with conn.cursor() as cursor:
        cursor.execute("""
            SELECT projects.id, projects.title, customers.name, programmers.name
            FROM projects
            LEFT JOIN customers ON projects.customer_id = customers.id
            LEFT JOIN programmers ON projects.programmer_id = programmers.id
        """)
        for row in cursor.fetchall():
            print(f"ID:{row[0]} | Название:{row[1]} | Заказчик:{row[2]} | Программист:{row[3]}")

def update_customer(conn):
    id = input("ID заказчика для изменения: ")
    name = input("Новое имя: ")
    with conn.cursor() as cursor:
        cursor.execute("UPDATE customers SET name=%s WHERE id=%s", (name, id))
        conn.commit()
        print("Изменено.")

def update_programmer(conn):
    id = input("ID программиста для изменения: ")
    name = input("Новое имя: ")
    with conn.cursor() as cursor:
        cursor.execute("UPDATE programmers SET name=%s WHERE id=%s", (name, id))
        conn.commit()
        print("Изменено.")

def update_project(conn):
    id = input("ID проекта для изменения: ")
    title = input("Новое название: ")
    customer_id = input("Новый ID заказчика: ")
    programmer_id = input("Новый ID программиста: ")
    with conn.cursor() as cursor:
        cursor.execute(
            "UPDATE projects SET title=%s, customer_id=%s, programmer_id=%s WHERE id=%s",
            (title, customer_id if customer_id else None, programmer_id if programmer_id else None, id)
        )
        conn.commit()
        print("Изменено.")

def delete_customer(conn):
    id = input("ID заказчика для удаления: ")
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM customers WHERE id=%s", (id,))
        conn.commit()
        print("Удалено.")

def delete_programmer(conn):
    id = input("ID программиста для удаления: ")
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM programmers WHERE id=%s", (id,))
        conn.commit()
        print("Удалено.")

def delete_project(conn):
    id = input("ID проекта для удаления: ")
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM projects WHERE id=%s", (id,))
        conn.commit()
        print("Удалено.")

def menu():
    print("""
1. Добавить заказчика
2. Добавить программиста
3. Добавить проект
4. Показать всех заказчиков
5. Показать всех программистов
6. Показать все проекты
7. Изменить заказчика
8. Изменить программиста
9. Изменить проект
10. Удалить заказчика
11. Удалить программиста
12. Удалить проект
0. Выход
""")

def main():
    conn = connect_to_database()
    create_tables(conn)
    while True:
        menu()
        choice = input("Выберите действие: ")
        if choice == "1":
            add_customer(conn)
        elif choice == "2":
            add_programmer(conn)
        elif choice == "3":
            add_project(conn)
        elif choice == "4":
            list_customers(conn)
        elif choice == "5":
            list_programmers(conn)
        elif choice == "6":
            list_projects(conn)
        elif choice == "7":
            update_customer(conn)
        elif choice == "8":
            update_programmer(conn)
        elif choice == "9":
            update_project(conn)
        elif choice == "10":
            delete_customer(conn)
        elif choice == "11":
            delete_programmer(conn)
        elif choice == "12":
            delete_project(conn)
        elif choice == "0":
            print("Выход.")
            conn.close()
            break
        else:
            print("Нет такого пункта меню.")

if __name__ == "__main__":
    main()
