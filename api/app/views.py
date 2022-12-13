from app import app
from flask import jsonify
from flask_restful import Api, Resource
import json

api = Api(app)

# filename="./book.json"

# function to add to the JSON flat file
def write_json(data, filename="book.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


class AddressBook(Resource):
    def get(self):
        with open("app/book.json", "r+") as file:
            # read the content of the file
            file_data = json.load(file)
            print(file_data)

            for record in file_data:
                print(record)

            # details = [{"firstname":"Jim"}]

            print(file_data[0])
            # return a json with all the file details
            return jsonify(file_data)

    def post(self, new_details): 
        with open("app/book.json", "r+") as file:
            # read the content of the file
            file_data = json.load(file)

            # add new details to the
            file_data.append(new_details)

            # return a json with all the file details
            file.seek(0)
            json.dump(file_data, file, indent = 4)

            return "Added to file"

        pass
    
    def put(self, new_details, old_details):
        with open("app/book.json", "r+") as file:
            # read the content of the file
            file_data = json.load(file)

            for record in file_data:
                print(record)

            # file_data[old_details]

            # return a json with all the file details
            file.seek(0)
            json.dump(file_data, file, indent = 4)

            return "Added to file"
        pass

    def delete(self):
        pass


    
api.add_resource(AddressBook, "/", "/<new_details>", "/<new_details>/<old_details>")

@app.route('/')
def index():
    return "Hello World!!!"