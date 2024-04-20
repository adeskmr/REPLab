#CRUD App

# create
# first, last, and email

from flask import request, jsonify
from config import app, db
from models import Contact
from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient
import os
import urllib.parse


@app.route("/contacts", methods=["GET"])
def get_contacts():
    contacts = Contact.query.all()
    json_contacts = list(map(lambda x: x.to_json(), contacts))
    return jsonify({"Contacts": json_contacts})

@app.route("/create_contact", methods=["POST"])
def create_contact():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    if not first_name or not last_name or not email:
        return (
            jsonify({"message": "You must include a first name, last name and email"}),
            400
        )
    
    new_contact = Contact(first_name=first_name, last_name=last_name, email=email)
    try:
        db.sesion.add(new_contact)
        db.sesion.commit()
    except Exception as e:
        return jsonify({"message": str(e)}), 400

    return jsonify({"message": "User created!"}), 201

@app.route("/update_contact/<int:user_ud>", methods=["PATCH"])
def update_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "User not found"})

    data = request.json
    contact.first_name = data.get("firstName", contact.first_name)
    contact.last_name = data.get("lastName", contact.last_name)
    contact.email = data.get("email", contact.email)

    db.sesion.commit()

    return jsonify({"message": "user updated"}), 200

@app.route("/delete_contact/<int:user_ud>", methods=["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "User not found"}), 404
    
    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message": "User deleted"}), 200


if __name__ == "__main__":
    # load_dotenv(find_dotenv())

    # # password = os.environ.get("MONGODB_PWD")
    # # password = "Pluto@3384"
    # password = urllib.parse.quote_plus("Pluto@3384")
    # password = urllib.parse.quote_plus("Pluto@3384")
    # connection_string = f"mongodb+srv://adesh9k:{password}@exploration.jehoooc.mongodb.net/?retryWrites=true&w=majority"
    # print(connection_string)
    # client = MongoClient(connection_string, connect=False)


    # # dbs = client.list_database_names()
    # # database_names = client.list_database_names()
    # test_db = client.test
    # collections = test_db.list_collection_names()

    # print(collections)
    with app.app_context():
        db.create_all()

    app.run(debug=True)
