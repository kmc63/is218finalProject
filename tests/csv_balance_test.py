import os
from app import db
from app.db.models import User, transactionDB
from flask_login import FlaskLoginClient

def test_csv_processed(application, client, add_user):
    application.test_client_class = FlaskLoginClient
    test_user = User.query.get(1)

    with application.test_client(user=test_user) as client:
        response = client.get('/transactions/upload')
        assert response.status_code == 200

        root = os.path.dirname(os.path.abspath(__file__))
        test_csv_file = os.path.join(root, '../uploads2/transactions2.csv')
        test_csv_file_data = open(test_csv_file, 'rb')
        test_data = {'file': (test_csv_file_data, 'transactions2.csv')}
        response2 = client.post('/transactions/upload', data=test_data)

        totalBalance = 0
        userDebitBalance = 0
        userCreditBalance = 0

        assert totalBalance == 0
        assert userDebitBalance == 0
        assert userCreditBalance == 0

        userDebit = transactionDB.query.filter_by(user_id=1, type='DEBIT')
        for debit in userDebit:
            userDebitBalance = userDebitBalance + int(debit.amount)

        userCredit = transactionDB.query.filter_by(user_id=1, type='CREDIT')
        for credit in userCredit:
            userCreditBalance = userCreditBalance + int(credit.amount)

        assert userDebitBalance == -27000
        assert userCreditBalance == 25690

        totalBalance = userDebitBalance + userCreditBalance

        assert totalBalance == -1310
