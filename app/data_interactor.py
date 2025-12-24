from fastapi import FastAPI
from queries import Functions as f

app = FastAPI()


@app.get("/contacts")
def get_all_contacts():
    get_all = f.show_contacts()
    return {"message": "printed succesfully",
            "contacts": get_all}

@app.post("/contacts")
def creating_new_contact(first_name, last_name, phone):
    new_contact = f.insert_contact(first_name, last_name, phone)
    return {"message": "contact added succesfully",
            "new contact": new_contact.id}


@app.put("/contacts/{id}")
def update_contact(first_name, last_name, phone):
    contact_to_edit = f.update_contact(first_name, last_name, phone, id)
    return {"message": "contact edited succesfully",
            "contact edited": contact_to_edit}


@app.delete("/contacts/{id}")
def deleting_contact():
    message = f.delete_contact(id)
    if message == "succes":
        return "successfully deleted"
    else:
        return "something went wrong with the delete function"