import psycopg2 as PyPG

# connectBD = PyPG.connect(
#     dbname="fruits_vegetables",
#     user="postgres",
#     password="2575",
#     host="localhost",
#     port="5432",
# )

# cursor = connectBD.cursor()
#
# query = "SELECT * FROM customers  "
#
# cursor.execute(query)
#
# table = cursor.fetchall()
# for line in table:
#     for element in line:
#         print(element,end = " - ")
#     print()
#
# cursor.close()
# connectBD.close()

def connect_to_database():
    connectBD = PyPG.connect(
        dbname="fruits_vegetables",
        user="postgres",
        password="2575",
        host="localhost",
        port="5432",
    )
    return connectBD

def create_table(name_table : str, title_values : str, connect_db):
    cursor = connect_db.cursor()
    query = f"CREATE TABLE {name_table} ({title_values});"
    cursor.execute(query)
    connect_db.commit()
    cursor.close()
    return

def add_values(name_table : str, title_values : str, values : list, connect_db):
    cursor = connect_db.cursor()
    values_str = str()
    for elem in values:
        line = f"('{elem[0]}',{elem[1]}),"
                #('Дима'     ,   18    )
        values_str += line
    values_str = values_str.removesuffix(",")
    query = f"INSERT INTO {name_table} ({title_values}) VALUES {values_str};"
    cursor.execute(query)
    connect_db.commit()
    cursor.close()
    return

def get_table(name_table : str, connect_db):
    cursor = connect_db.cursor()
    query = f"SELECT * FROM {name_table};"
    cursor.execute(query)
    lst = cursor.fetchall()
    connect_db.commit()
    cursor.close()
    return lst

connectDB = connect_to_database()

table_create_values_title = (" id uuid DEFAULT gen_random_uuid(),"
                             " name text NOT NULL,              "
                             " age int,                         "
                             " primary key (id)                 ")
name_table = "example_table"

create_table(name_table, table_create_values_title, connectDB)
add_values(name_table,"name, age", (("Вася", 10),("Маша", 12),("Петя", 14)), connectDB)
lst = get_table(name_table, connectDB)
for line in lst:
    for element in line:
        print(element, end = " - ")
    print()

connectDB.close()
