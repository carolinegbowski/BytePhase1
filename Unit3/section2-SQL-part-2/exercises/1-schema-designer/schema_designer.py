import sqlite3 

CREATE_SNACKS_SQL = """
CREATE TABLE snacks(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    brand VARCHAR(100),
    type VARCHAR(50),
    price FLOAT,
    quantity_avail INTEGER)
    """

DROP_SQL = "DROP TABLE IF EXISTS snacks"

with sqlite3.connect("snacks.db") as conn:
    cursor = conn.cursor() # cursor executes statements, connect connects the statements
    cursor.execute(DROP_SQL) # deletes table: accounts if already exists
    cursor.execute(CREATE_SNACKS_SQL)

CREATE_SCHOOL_SQL = """
CREATE TABLE students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first VARCHAR(200),
    last VARCHAR(200),
    student_id INTEGER NOT NULL,
    )
CREATE TABLE teachers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first VARCHAR(200),
    last VARCHAR(200),
    employee_id INTEGER NOT NULL,
    )
CREATE TABLE classes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(200),
    course_code INTEGER NOT NULL, 
    teacher_id INTEGER
    FOREIGN KEY ("teacher_id") REFERENCES teachers(id)
    )
CREATE TABLE students_classes(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    student_id INTEGER,
    class_id INTEGER,
    FOREIGN KEY ("student_id") REFERENCES students(id),
    FOREIGN KEY ("class_id") REFERENCES classes(id),
)
"""

DROP_SQL = """DROP TABLE IF EXISTS school;
DROP TABLE IF EXISTS classes;
DROP TABLE IF EXISTS teachers;
DROP TABLE IF EXISTS classes_students;
""" 
# how do i add 3 tables to this line?

with sqlite3.connect("school.db") as conn:
    cursor = conn.cursor() 
    cursor.execute(DROP_SQL) 
    cursor.execute(CREATE_SCHOOL_SQL)

CREATE_COMPANY_SQL = """
CREATE TABLE employees(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ssn INTEGER NOT NULL,
    salary FLOAT, 
    phone_num INTEGER NOT NULL,
    department_id INTEGER,
    FOREIGN KEY ("department_id") REFERENCES departments(id)
    )

CREATE TABLE departments(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    department_id INTEGER NOT NULL,
    name VARCHAR(200),
    budget FLOAT
    )
"""
DROP_SQL = "DROP TABLE IF EXISTS employees" # how do i add 2 tables to this line?

with sqlite3.connect("company.db") as conn:
    cursor = conn.cursor()
    cursor.execute(DROP_SQL) 
    cursor.execute(CREATE_COMPANY_SQL)

# # NEED TO WORK ON THIS ONE
# CREATE_SUBREDDIT_SQL = """
# """
# DROP_SQL = "DROP TABLE IF EXISTS subreddit" # how do i add 2 tables to this line?

# with sqlite3.connect("subreddit.db") as conn:
#     cursor = conn.cursor()
#     cursor.execute(DROP_SQL) 
#     cursor.execute(CREATE_SUBREDDIT_SQL)

CREATE_GALLERY_SQL = """
CREATE TABLE artists(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(200),
    birthplace VARCHAR(200),
    age INTEGER NOT NULL,
    style VARCHAR(200)
)
CREATE TABLE art_pieces(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    year INTEGER NOT NULL,
    title VARCHAR(300),
    type VARCHAR(200),
    price FLOAT,
    purchased_by_id INTEGER,
    artist_id INTEGER,
    FOREIGN KEY ("artist_id") REFERENCES artists(id),
    FOREIGN KEY ("purchased_by_id") REFERENCES customers(id)
)
CREATE TABLE customers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(200),
    phone INTEGER NOT NULL,
    address VARCHAR(200)
)
"""
DROP_SQL = "DROP TABLE IF EXISTS gallery" # how do i add 2 tables to this line?

with sqlite3.connect("gallery.db") as conn:
    cursor = conn.cursor()
    cursor.execute(DROP_SQL) 
    cursor.execute(CREATE_GALLERY_SQL)


