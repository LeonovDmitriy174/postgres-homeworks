"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import os
import csv

password = os.environ.get('MY_PASSWORD')


def open_file(file_name):
    with open(os.path.join("north_data", file_name), newline='', encoding='windows-1251') as csvfile:
        file = csv.DictReader(csvfile)
        new_list = []
        for i in file:
            new_list.append(i)
        return new_list


conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password=password
)
try:
    with conn.cursor() as cur:
        rows = open_file("employees_data.csv")
        for row in rows:
            cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", (row['employee_id'],
                                                                                  row['first_name'],
                                                                                  row['last_name'],
                                                                                  row['title'],
                                                                                  row['birth_date'],
                                                                                  row['notes']))
        conn.commit()

        rows = open_file("customers_data.csv")
        for row in rows:
            cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", (row['customer_id'],
                                                                      row['company_name'],
                                                                      row['contact_name']))
        conn.commit()

        rows = open_file("orders_data.csv")
        for row in rows:
            cur.execute(f"INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", (row['order_id'],
                                                                            row['employee_id'],
                                                                            row['customer_id'],
                                                                            row['order_date'],
                                                                            row['ship_city']))
        conn.commit()
finally:
    conn.close()
