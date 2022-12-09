from app import app
from flask_restful import Api, Resource
import json

api = Api(app)



class AddressBook(Resource):
    def get(self):
        pass

    def post(self):
        pass
    
    def put(self):
        pass

    def delete(self):
        pass


    
api.add_resource(AddressBook, "/", "/<genre>", "/<genre>/<new_genre>")

@app.route('/')
def index():
    return "Hello World!!!"