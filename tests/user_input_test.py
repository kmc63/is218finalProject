from app import db
from app.auth.forms import *
from flask_login import FlaskLoginClient
from app.db.models import User

def test_login_success(application, client):
    test_login = login_form()
    test_login.email.data = "keith@njit.edu"
    test_login.password.data = "password"
    assert test_login.validate()

def test_login_unsuccessful(application, client):
    test_login = login_form()
    test_login.email.data = "keith@njit.edu"
    test_login.password.data = "pass"
    assert not test_login.validate()

def test_register_success(application, client):
    test_register = register_form()
    test_register.email.data = "keith@njit.edu"
    test_register.password.data = "password"
    test_register.confirm.data = "password"
    assert test_register.validate()

def test_register_unsuccessfull(application, client):
    test_register = register_form()
    test_register.email.data = "keith@njit.edu"
    test_register.password.data = "password"
    test_register.confirm.data = "password1"
    assert not test_register.validate()

