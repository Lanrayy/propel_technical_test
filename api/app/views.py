from app import app
from flask import jsonify, request
from flask_restful import Api, Resource
import json

api = Api(app)

# Address book class
class AddressBook(Resource):
    def get(self):
        with open("app/book.json", "r+") as file:
            # read the content of the file
            file_data = json.load(file)
            print(file_data)

            # return a json with all the file details
            return jsonify(file_data)

    def post(self):
        with open("app/book.json", "r+") as file:
            print(request.data)
            # convert request bytes into json
            data = json.loads(request.data.decode('utf-8'))

            print(data)
            print(data.get('first_name'))

            # read the content of the file
            file_data = json.load(file)

            # add new details to the
            file_data.append(data)

            # return a json with all the file details and update JSON flat file
            file.seek(0)
            json.dump(file_data, file, indent = 4)

            # return success message
            return jsonify({"Success" : "Contact Added"})

    
    def put(self, new_details, old_details):
        with open("app/book.json", "r+") as file:
            # read the content of the file
            file_data = json.load(file)

            for record in file_data:
                print(record)

            file.seek(0)
            json.dump(file_data, file, indent = 4)

            return jsonify({"Success" : "Contact Updated"})

    def delete(self):
        print(request.data)
        data = json.loads(request.data.decode('utf-8'))
        update = []

        with open("app/book.json", "r") as file:
            # read the content of the file
            file_data = json.load(file)

            # find the contact, skip over it
            # append the rest to a new array
            for contact in file_data:
                print(contact)
                if contact['first_name'] == data.get('first_name') and contact['last_name'] == data.get('last_name') and contact['email'] == data.get('email') :
                    print("MATCH found")
                    pass
                else:
                    update.append(contact)
                
        print("**************New info*******************")
        print(update)

        # Update the JSON flat file
        with open("app/book.json", "w") as file:
            json.dump(update, file, indent=4)
        
        return jsonify({"Success" : "Contact Deleted"})
            
            
api.add_resource(AddressBook, "/")