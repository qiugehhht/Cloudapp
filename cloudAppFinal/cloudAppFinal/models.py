from flask_login import UserMixin

class User(UserMixin):
    pass
#Due to lack of time we didn't put login info in to a database, we just created dicts to prove ID and password to support login 
users = [
    {'id':'Tom', 'username': 'Tom', 'password': '111111'},
    {'id':'Michael', 'username': 'Michael', 'password': '123456'}
]

def query_user(user_id):
    for user in users:
        if user_id == user['id']:
            return user
