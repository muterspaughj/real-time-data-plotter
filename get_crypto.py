"""
get_crypto.py
----------------------------------------
Contains the GetCrypto class, which gets
real-time cryptocurrency prices from the Coinbase API.
Author: Jack Muterspaugh
"""

import requests

class GetCrypto:
    def __init__(self, coin="BTC"):
        self.coin = coin.upper()

    def get_price(self):
        url = f"https://api.coinbase.com/v2/prices/{self.coin}-USD/spot"

        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return float(data["data"]["amount"])
        except Exception as e:
            print(f"Error getting price for {self.coin}: {e}")
            return None
        
