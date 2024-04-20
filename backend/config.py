from flask import Flask, jsonify
# Flask-SQLAlchemy is a Flask extension that simplifies database integration by providing an ORM layer and database management tools through integration with SQLAlchemy.
from flask_sqlalchemy import SQLAlchemy
# Flask extension that enables Cross-Origin Resource Sharing (CORS) for handling requests from different origins in web applications.
from flask_cors import CORS

# app instance
app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
# # api/home/
# @app.route("/api/home", methods=['GET'])
# def return_home():
#     return jsonify({
#         "message": "hello world!"
#     })

# if __name__ == "__main__":
#     app.run(debug=True, port=8080)