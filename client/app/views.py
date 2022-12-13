from flask import request, render_template, flash, redirect, url_for, session, jsonify
from app import app
import requests
from .forms import GenreForm, DetailsForm
import json
import time



########################################
# LIST ALL CONTACT PAGE
# The page that deals with adding a new contact
######################################
@app.route('/list_all', methods=['GET', 'POST'])
def list_all():

    # make a get request to the backend api
    url = "http://127.0.0.1:5000/"
    response = requests.request("GET", url)
    print(response.json()[0]['first_name'])
    print(response.json()[1]['first_name'])
    flash("Finding genres")
    return render_template('list_all.html',
                            data=response.json(),
                           title="Address Book",)


########################################
# ADD CONTACT PAGE
# The page that deals with adding a new contact
######################################
@app.route('/add_contact', methods=['GET', 'POST'])
def add_contact():
    # define the form
    form = DetailsForm()

    # make a request to the backend api
    if request.method == "POST":
        print("Making request to API")
        print(form.first_name.data)
        print(request.data)

        data = {"first_name": form.first_name.data,
                "last_name": form.last_name.data,
                "phone": form.phone.data,
                "email": form.email.data }
        
        

        # make a post request
        url = f"http://127.0.0.1:5000/"
        response = requests.post(url = url, json=data)

        print(response)
        print(response.status_code)
        print(response.text)
        # print(response.json()[0]['firstname'])
        flash("Finding genres")
    # return redirect(url_for('genres'))

    return render_template('add_contact.html',
                           title='Lanre\'s API',
                        #    response = response,
                           form=form)


########################################
# DELETE RECORD
# queries the first API and gets a list of genres database and
# displays all the buttons on screen
######################################
@app.route('/delete_contact', methods=['GET', 'POST'])
def delete_contact():
    # get record information

    # save the information 
    # data = {"first_name": session.get('first_name'),
    #     "last_name": session.get('last_name'),
    #     "phone": session.get('phone'),
    #     "email": session.get('email')
    #     }
    print("Deleting record")
    data = {
        "first_name": "Jason",
        "last_name": "Grimshaw",
        "phone": "01913478123",
        "email": "jason.grimshaw@corrie.co.uk"
    }

    # make a delete request to backend
    # make a post request
    url = f"http://127.0.0.1:5000/"
    response = requests.delete(url = url, json=data)
    print(response)
    print(response.status_code)
    print(response.text)

    return render_template('delete_contact.html',
                           title='Lanre\'s API')


########################################
# QUERY SECOND API AND EXTERNAL API
# RETURN RESULT TO CLIENT
########################################
@app.route('/genres/<genre>', methods=['GET'])
def genre(genre):
    # Make a request to second API
    start2 = time.time()
    url = f"http://127.0.0.1:5002/{genre}"
    response = requests.request("GET", url)
    movie_id = response.json()['id']
    end2= time.time()
    print('api2:' , end2-start2)
    

    # Make a request to external api
    url = f"https://moviesdatabase.p.rapidapi.com/titles/{movie_id}"

    headers = {
        "X-RapidAPI-Key": "ceaacd2d78msh3c3cb823eae0056p122f0cjsn33629befbb38",
        "X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
    }

    # make the request
    start3 = time.time()
    response = requests.request("GET", url, headers=headers)
    end3 = time.time()
    print('external api', end3-start3)
    

    # check response has valid information
    # if not redirect to try find a new movie
    if response.json()['results']['primaryImage'] == None or response.json()['results']['releaseDate'] == None:
        return redirect(url_for('genre', genre=genre))

    # get the poster url
    image_url = response.json()['results']['primaryImage']['url']

    return render_template('index3.html',
                           title='Lanre\'s API',
                           image_url=image_url,
                           genre=genre,
                           response=response.json())


# TO SEE THE DATA IN THE DATA BASE
# FOR TESTING
@app.route('/test', methods=['GET'])
def test():
    user = {'name': 'Lanre'}
    data = models.Genres.query.all()

    # Make a request to second API
    # url = f"http://127.0.0.1:5000/{genre}"
    # response = requests.request("GET", url)
    # movie_id = response.json()['id']

    # Make a request to external api
    url = f"https://moviesdatabase.p.rapidapi.com/titles/tt0371251"

    headers = {
        "X-RapidAPI-Key": "ceaacd2d78msh3c3cb823eae0056p122f0cjsn33629befbb38",
        "X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
    }

    # make the request
    response = requests.request("GET", url, headers=headers)
    flash(response.json())  # displays reponse in integrated client

    return render_template('data.html',
                           title='Lanre\'s API',
                           user=user,
                           data=data)
