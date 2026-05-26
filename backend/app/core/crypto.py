import os

from dotenv import load_dotenv

from cryptography.fernet import Fernet

load_dotenv()

KEY = os.getenv(
    "SECRET_KEY"
).encode()

fernet = Fernet(KEY)


def encrypt(text):

    return fernet.encrypt(
        text.encode()
    ).decode()


def decrypt(text):

    return fernet.decrypt(
        text.encode()
    ).decode()