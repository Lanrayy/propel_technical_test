from app import app
from flask import jsonify, request
from flask_restful import Api, Resource
import json

api = Api(app)

# Address book class
class AddressBook(Resource):
    # get contact
    def get(self):
        with open("app/book.json", "r+") as file:
            # read the content of the file
            file_data = json.load(file)
            print(file_data)

            # return a json with all the file details
            return jsonify(file_data)
    # Add new contact
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

    # update contact
    def put(self):
        print(request.data)
        # convert request bytes into JSON
        data = json.loads(request.data.decode('utf-8'))
        update = []

        with open("app/book.json", "r") as file:
            # read the content of the file
            file_data = json.load(file)

            # find the contact, UPDATE it
            for contact in file_data:
                print(contact)
                if contact['first_name'] == data.get('contact_to_update_first_name') and contact['last_name'] == data.get('contact_to_update_last_name'):
                    print("MATCH found")
                    # update details here
                    contact['first_name'] = data.get('first_name')
                    contact['last_name'] = data.get('last_name')
                    contact['email'] = data.get('email')
                    contact['phone'] = data.get('phone')
                    update.append(contact)
                else:
                    update.append(contact)
                
        print("**************New info*******************")
        print(update)

        # Update the JSON flat file
        with open("app/book.json", "w") as file:
            json.dump(update, file, indent=4)
        
        return jsonify({"Success" : "Contact Updated"})

    # delete contact
    def delete(self):
        print(request.data)
        # convert request bytes into JSON
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