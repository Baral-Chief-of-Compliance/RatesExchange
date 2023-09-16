import requests, os
from dotenv import load_dotenv


load_dotenv()

FIXER_KEY = os.getenv('FIXER_KEY')


def get_exchange_rates(from_currency, to_currency):
    url = f"https://api.apilayer.com/fixer/convert?to={to_currency}&from={from_currency}&amount=1"
    print(url)

    response = requests.request("GET", url, headers={
        "apikey": FIXER_KEY
    }, data={})

    result = response.json()

    return result['info']['rate']