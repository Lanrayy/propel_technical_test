from flask import request, render_template, flash, redirect, url_for, session, jsonify
from app import app
import requests
from .forms import AddContactForm

########################################
# LIST ALL CONTACTS PAGE
# Lists all contacts
######################################
@app.route('/list_all', methods=['GET', 'POST'])
def list_all():
    # make a get request to the backend api to get all contacts
    url = "http://127.0.0.1:5000/"
    try:
        response = requests.request("GET", url)
        data = response.json()
    except: 
        data = {}

    # When a button is clicked on the page
    if request.method == "POST":
        print("BUTTON CLICKED")
        print(request.form)
        clicked = request.form['button']
        print(clicked)
        
        # check which button was clicked
        if 'delete-' in clicked:
            print("DELETE BUTTON CLICKED")

            # split the value and save it in a session
            user = clicked.split("-")
            session['contact_to_delete_first_name'] = user[1]
            session['contact_to_delete_last_name'] = user[2]
            session['contact_to_delete_email'] = user[3]

            # redirect to the page that deletes the contact
            return redirect(url_for('delete_contact'))
        elif clicked == 'add-contact-button':
            # if the add contact button is clicked redirect to that page
            return redirect(url_for('add_contact'))
    return render_template('list_all.html',
                            data=data,
                           title="Address Book",)


########################################
# ADD CONTACT PAGE
# The page that deals with adding a new contact
######################################
@app.route('/add_contact', methods=['GET', 'POST'])
def add_contact():
    # define the form
    form = AddContactForm()

    # make a request to the backend api
    if request.method == "POST":
        print(request.form)

        clicked = request.form['button']
        if clicked == 'back-button':
            return redirect(url_for('list_all'))
        else:
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


            print(response.ok)
            print(response.status_code)
            print(response.text)
            if response.ok == True:
                # flash message and redirect back to the list all page
                flash("Contact Added Successfully")
                return redirect(url_for('list_all'))
            else:
                flash('Try Again! Unable to Add contact!')

    return render_template('add_contact.html',
                           title='Address Book',
                           form=form)


########################################
# DELETE CONTACT
# deletes a contact
######################################
@app.route('/delete_contact', methods=['GET', 'POST'])
def delete_contact():
    # get record information
    # make a JSON out of the information 
    contact_to_delete_first_name = session.get('contact_to_delete_first_name')
    contact_to_delete_last_name = session.get('contact_to_delete_last_name')
    contact_to_delete_email = session.get('contact_to_delete_email')

    if contact_to_delete_first_name and contact_to_delete_last_name and contact_to_delete_email:
        print("Deleting record")
        data = {"first_name": contact_to_delete_first_name,
            "last_name": contact_to_delete_last_name,
            "email": contact_to_delete_email
            }

        # make a delete request to backend
        # make a post request
        url = f"http://127.0.0.1:5000/"
        response = requests.delete(url = url, json=data)
        print(response)
        print(response.status_code)
        print(response.text)

        if response.ok == True:
            # flash message and redirect back to the list all page
            flash("Contact Deleted")
            return redirect(url_for('list_all'))
        else:
            flash('Try Again! Unable to Delete!')

    return render_template('delete_contact.html',
                           title='Address Book')

