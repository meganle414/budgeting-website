import plaid
# from plaid import Client
from plaid.api import plaid_api
from .config import PLAID_CLIENT_ID, PLAID_SECRET, PLAID_ENV


configuration = plaid.Configuration(
    host=plaid.Environment.Sandbox,
    api_key={
        'clientId': PLAID_CLIENT_ID,
        'secret': PLAID_SECRET,
    }
)

api_client = plaid.ApiClient(configuration)
client = plaid_api.PlaidApi(api_client)

def get_plaid_client():
    # return Client(
    #     client_id=PLAID_CLIENT_ID,
    #     secret=PLAID_SECRET,
    #     environment=PLAID_ENV
    # )
    return api_client