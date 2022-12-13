from flask import request, render_template, flash, redirect, url_for, session
from app import app
import requests
from .forms import GenreForm
import json
import time


########################################
# LANDING PAGE
# landing page of the Integrated Client
######################################
@app.route('/', methods=['GET', 'POST'])
def index():
    # define the form
    form = GenreForm

    url = "http://127.0.0.1:5000/"
    response = requests.request("GET", url)
    print(response.json()[0]['firstname'])


    if request.method == 'POST':
        flash("Finding genres")
        return redirect(url_for('genres'))

    return render_template('index.html',
                           title='Lanre\'s API',
                           response = response,
                           form=form)


########################################
# FIRST API
# queries the first API and gets a list of genres database and
# displays all the buttons on screen
######################################
@app.route('/genres', methods=['GET', 'POST'])
def genres():
    # define the form
    form = GenreForm()
    start1 = time.time()
    # Make a request to first API
    url = "http://127.0.0.1:5001/"
    response = requests.request("GET", url)
    end1 = time.time()
    print('api1:', end1-start1)
    

    # parse the response for data for the webpage
    data = response.json()["genres"]

    # If user clicks a button,
    # save user choice and redirect to the next page
    if request.method == 'POST':
        button = request.form['genre']
        flash(f'Genre picked: {button}')
        return redirect(url_for('genre', genre=f'{button}'))

    return render_template('index2.html',
                           title='Lanre\'s API',
                           data=data,
                           form=form)


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
