from fastapi import FastAPI
from queries import Functions as f
import dotenv

app = FastAPI()


@app.get("/contacts")
def get_all_contacts():
    get_all = f.show_contacts()
    return {"message": "printed succesfully",
            "contacts": get_all}

@app.post("/contacts")
def creating_new_contact(first_name, last_name, phone):
    new_contact = insert_contact(first_name, last_name, phone)
    return {"message": "contact added succesfully",
            "new contact": new_contact.id}


@app.put("/contacts/{id}")
def update_contact(first_name, last_name, phone):
    values_to_edit = [first_name, last_name, phone]
    edit_contact(id, contact_to_edit)
    return {"message": "contact edited succesfully",
            "contact edited": contact_to_edit}


@app.delete("/contacts/{id}")
def deleting_contact():
    query = ("DELETE FROM contacts"
             "WHERE id = %s")