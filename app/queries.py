from mysql-connector import connector
from config import get_connection
class Functions:
    def show_contacts():
        query = ("SELECT * FROM contacts")
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def insert_contact(tpl_contact):
        add_contact = (first_name, last_name, phone)
        query = 
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor.fetchall()
            

    def update_contact(first_name, last_name, phone, id)
    query = (f"UPDATE contacts"
             f"SET first_name = {first_name}, last_name = {last_name}, phone = {phone}"
             f"WHERE id = {id}")