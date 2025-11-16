import random
import string

def generate_random_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def generate_user_data():
    return {
        "email": "mroizo@mail.ru",
        "password": "password",
        "name": "Quentin Dupieux"
    }
