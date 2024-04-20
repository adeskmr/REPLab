from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient
import os
import urllib.parse

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")
connection_string = f"mongodb+srv://adesh9k:{password}@exploration.jehoooc.mongodb.net/?retryWrites=true&w=majority"
print(connection_string)
client = MongoClient(connection_string)
print(client)

dbs = client.list_database_names()
database_names = client.list_database_names()
test_db = client.test
collections = test_db.list_collection_names()

print(collections)