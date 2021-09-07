import os
import sqlite3


with open(os.path.join(os.getcwd(), 'test.db'), 'w+', encoding='utf-8') as f:
    f.write('\n')

db_path = os.path.join(os.getcwd(), 'test.db')

conn = sqlite3.connect(db_path)

cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS categories(
    id INTEGER PRIMARY KEY,
    category_name TEXT NOT NULL,
    category_description TEXT NOT NULL);
""")

conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS units(
    unit_id INTEGER PRIMARY KEY,
    unit TEXT NOT NULL);
""")

conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS positions(
    position_id INTEGER PRIMARY KEY,
    position TEXT NOT NULL);
""")

conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS employees(
    employee_id INTEGER PRIMARY KEY,
    employee_fio TEXT NOT NULL,
    employee_position INTEGER NOT NULL,
    FOREIGN KEY (employee_position) REFERENCES positions(position_id)
    );
""")

conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS goods(
    good_id INTEGER PRIMARY KEY,
    good_name TEXT NOT NULL,
    good_unit INTEGER NOT NULL,
    good_cat INTEGER NOT NULL,
    FOREIGN KEY (good_cat) REFERENCES categories(id),
    FOREIGN KEY (good_unit) REFERENCES units(unit_id)
    );
""")

conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS vendors(
    vendor_id INTEGER PRIMARY KEY,
    vendor_name TEXT NOT NULL,
    vendor_ownerchipform TEXT NOT NULL,
    vendor_address TEXT NOT NULL,
    vendor_phone TEXT NOT NULL,
    vendor_email TEXT NOT NULL);
""")

conn.commit()

conn.close()

