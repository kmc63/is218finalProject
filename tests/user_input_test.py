from app.auth.forms import *
from flask_login import FlaskLoginClient
from app.db.models import User

def test_login_successful(application, client):
    test_login = login_form()
    test_login.email.data = "keith@njit.edu"
    test_login.password.data = "password"
    assert test_login.validate()

def test_login_unsuccessful(application, client):
    test_login = login_form()
    test_login.email.data = "keith@njit.edu"
    test_login.password.data = "pass"
    assert not test_login.validate()

def test_register_successful(application, client):
    test_register = register_form()
    test_register.email.data = "keith@njit.edu"
    test_register.password.data = "password"
    test_register.confirm.data = "password"
    assert test_register.validate()

def test_register_unsuccessful(application, client):
    test_register = register_form()
    test_register.email.data = "keith@njit.edu"
    test_register.password.data = "password"
    test_register.confirm.data = "password1"
    assert not test_register.validate()

def test_dashboard_successful(application, client, add_user):
    application.test_client_class = FlaskLoginClient
    test_user = User.query.get(1)
    with application.test_client(user=test_user) as client:
        response = client.get('/dashboard')
        assert response.status_code == 200

def test_dashboard_unsuccessful(application, client):
    application.test_client_class = FlaskLoginClient
    with application.test_client(user="") as client:
        response = client.get('/dashboard')
        assert response.status_code == 302

def test_csv_upload_successful(application, client, add_user):
    application.test_client_class = FlaskLoginClient
    test_user = User.query.get(1)
    with application.test_client(user=test_user) as client:
        response = client.get('/transactions/upload')
        assert response.status_code == 200

def test_csv_upload_unsuccessful(application, client):
    application.test_client_class = FlaskLoginClient
    with application.test_client(user="") as client:
        response = client.get('/transactions/upload')
        assert response.status_code == 302
