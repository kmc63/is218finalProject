import os
from app.db.models import User
from flask_login import FlaskLoginClient

def test_csv_processed(application, client, add_user):
    application.test_client_class = FlaskLoginClient
    test_user = User.query.get(1)

    with application.test_client(user=test_user) as client:
        response = client.get('/transactions/upload')
        assert response.status_code == 200

        root = os.path.dirname(os.path.abspath(__file__))
        test_csv_file = os.path.join(root, '../uploads/transactions2.csv')
        test_csv_file_data = open(test_csv_file, 'rb')
        test_data = {'file': (test_csv_file_data, 'transactions2.csv')}
        response2 = client.post('/transactions/upload', data=test_data)
        assert response2.status_code == 302
        assert response2.headers["Location"] == "/transactions"

