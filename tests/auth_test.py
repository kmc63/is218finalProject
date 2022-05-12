"""
from flask_login import FlaskLoginClient
from app.db.models import User
from app.auth import edit_profile
"""

def test_request_main_menu_links(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b'href="/login"' in response.data
    assert b'href="/register"' in response.data

def test_auth_page_dashboard(client):
    response = client.get("/dashboard")
    assert response.status_code == 302

def test_auth_page_register(client):
    response = client.get("/register")
    assert response.status_code == 200
    assert b"Register" in response.data

def test_auth_page_login(client):
    response = client.get("/login")
    assert response.status_code == 200
    assert b"Login" in response.data

"""
def test_auth_page_user_edit(application, client, add_user):
    application.test_client_class = FlaskLoginClient
    test_user = User.query.get(1)

    with application.test_client(user=test_user) as client:
        response = client.get('/auth/user_edit')
        assert response.status_code == 200
        assert b"User Edit" in response.data

def test_auth_page_user_new(application, client, add_user):
    application.test_client_class = FlaskLoginClient
    test_user = User.query.get(1)

    with application.test_client(user=test_user) as client:
        response = client.get('/auth/user_new')
        assert response.status_code == 200
        assert b"New User" in response.data

def test_auth_page_manage_account(application, client, add_user):
    application.test_client_class = FlaskLoginClient
    test_user = User.query.get(1)

    with application.test_client(user=test_user) as client:
        response = client.get('/auth/manage_account')
        assert response.status_code == 200
        assert b"Manage Account" in response.data

def test_auth_page_profile_view(application, client, add_user):
    application.test_client_class = FlaskLoginClient
    test_user = User.query.get(1)

    with application.test_client(user=test_user) as client:
        response = client.get('/auth/profile_view')
        assert response.status_code == 200
        assert b"User Email" in response.data

def test_auth_page_profile_edit(application, client, add_user):
    application.test_client_class = FlaskLoginClient
    test_user = User.query.get(1)

    with application.test_client(user=test_user) as client:
        response = client.get('/auth/profile_edit')
        assert response.status_code == 200
        assert b"Manage Profile" in response.data 
"""
