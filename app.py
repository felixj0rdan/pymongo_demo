from pymongo import MongoClient
from pw import PASSWORD as password

# password = pw.password
print(password)

client = MongoClient(
    'mongodb+srv://felix:'+password+'@cluster0.hco8cja.mongodb.net/?retryWrites=true&w=majority'
)

db = client.get_database("student_db")

records = db.student_records

print(records.count_documents({}))

new_student = {"name": "ram", "roll_no": 321, "branch": "it"}

new_students = [
    {"name": "ram2", "roll_no": 321, "branch": "it"},
    {"name": "ram3", "roll_no": 321, "branch": "it"},
]


# records.insert_many(new_students)

# print(list(records.find()))

# print(records.find_one({"roll_no": 321}))

student_updates = {"name": "Jordan"}

# records.update_one({"roll_no": "38"}, {"$set": student_updates})

records.delete_one({"name": "ram2"})

# from flask import Flask, jsonify
# from flask_restful import Api
# from flask_jwt_extended import JWTManager
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# if __name__ == "__main__":

#     app.run(port=8000, debug=True)
