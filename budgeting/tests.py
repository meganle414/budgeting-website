import unittest
from .utils import get_plaid_client
from .tasks import get_public_token, get_access_token, get_transactions, get_accounts
from time import sleep

class TestPlaidClient(unittest.TestCase):
    def setUp(self):
        self.client = get_plaid_client()

    def test_get_public_token(self):
        institution_id = 'ins_109512'
        response = get_public_token(institution_id)

        print("Public Token, Integration Test: ", response['public_token'])
        self.assertIn('public_token', response)

    def test_get_access_token(self):
        institution_id = 'ins_109512'
        public_token = get_public_token(institution_id)['public_token']
        response = get_access_token(public_token)

        print("Access Token, Integration Test: ", response)

        self.assertIsInstance(response, str)
    
    def test_get_transactions(self):
        institution_id = 'ins_109512'
        public_token = get_public_token(institution_id)['public_token']
        access_token = get_access_token(public_token)
        start_date = '2024-06-01'
        end_date = '2024-06-30'

       # Adding delay to wait for the transactions to be ready
        sleep(2)

        response = get_transactions(access_token, start_date, end_date)
        
        print("Get Transactions, Integration Test: ", start_date, "-", end_date, " ", [(transaction['name'], transaction['amount'], transaction['transaction_id']) for transaction in response['transactions']])

        self.assertIn('transactions', response)

    def test_get_accounts(self):
        institution_id = 'ins_127287'
        public_token = get_public_token(institution_id)['public_token']
        access_token = get_access_token(public_token)

        # Adding delay to wait for the accounts to be ready
        sleep(2)

        response = get_accounts(access_token)

        print("Get Accounts, Integration Test: ", [account['name'] for account in response['accounts']])

        self.assertIn('accounts', response)