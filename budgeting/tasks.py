from celery import shared_task
from .utils import get_plaid_client
from datetime import datetime
from plaid.model.sandbox_public_token_create_request import SandboxPublicTokenCreateRequest
from plaid.model.products import Products
from plaid.model.transactions_get_request import TransactionsGetRequest
from plaid.model.auth_get_request import AuthGetRequest
from plaid.model.item_public_token_exchange_request import ItemPublicTokenExchangeRequest


@shared_task
def get_public_token(institution_id):
    client = get_plaid_client()
    
    request = SandboxPublicTokenCreateRequest(
            institution_id=institution_id,
            initial_products=[Products('transactions')]
    )

    public_token = client.sandbox_public_token_create(request)

    return public_token


@shared_task
def get_transactions(access_token, start_date, end_date):
    client = get_plaid_client()
    
    request = TransactionsGetRequest(
            access_token=access_token,
            start_date=datetime.strptime(start_date, "%Y-%m-%d").date(),
            end_date=datetime.strptime(end_date, "%Y-%m-%d").date()
    )

    transactions = client.transactions_get(request)
    return transactions


@shared_task
def get_accounts(access_token):
    client = get_plaid_client()

    request = AuthGetRequest(
        access_token=access_token
    )

    accounts = client.auth_get(request)
    return accounts


@shared_task
def get_access_token(public_token):
    client = get_plaid_client()
    
    request = ItemPublicTokenExchangeRequest(
        public_token=public_token
    )

    exchange_response = client.item_public_token_exchange(request)
    
    access_token = exchange_response['access_token']

    return access_token