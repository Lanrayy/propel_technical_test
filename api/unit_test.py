import pytest, requests

# @pytest.mark.unit
def test1():
    assert 5 == 5

def test_GET():
    url = "http://127.0.0.1:5000/"
    response = requests.request("GET", url)
    print(response.json()[0]['firstname'] == "Jim")
    # assert(response.firstname == "Jim")


    # assert response[0].firstname == "Jim"
    # print(response.json())

# def test_login_database():
#     try:
#         # test for empty email
#         test_entry = models.User_Login(email="", password="password")
#         db.session.add(test_entry)
#     except AssertionError as e:
#         # nice the database raised an assertion error
#         error1 = str(e)

#     try:
#         # test for email without "@" symbol
#         test_entry = models.User_Login(email="nope", password="password")
#         db.session.add(test_entry)
#     except AssertionError as e:
#         # nice the database raised an assertion error
#         error2 = str(e)

#     try:
#         # test for already taken email
#         test_entry = models.User_Login(email="already@taken.com", password="password")
#         db.session.add(test_entry)
#         test_entry = models.User_Login(email="already@taken.com", password="password")
#         db.session.add(test_entry)
#     except AssertionError as e:
#         # nice the database raised an assertion error
#         error3 = str(e)

#     try:
#         # test for empty password
#         test_entry = models.User_Login(email="Pass@email.com", password="")
#         db.session.add(test_entry)
#     except AssertionError as e:
#         # nice the database raised an assertion error
#         error4 = str(e)

#     assert error1 == "No email provided" and error2 == 'Email address missing "@" symbol' and error3 == "Email is already in use" and error4 == "No password provided"