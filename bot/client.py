import os
import logging
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()

TESTNET_URL = "https://testnet.binancefuture.com"


class BinanceClient:
    def __init__(self):
        api_key = os.getenv("API_KEY")
        api_secret = os.getenv("API_SECRET")

        if not api_key or not api_secret:
            raise Exception("API keys missing in .env file")

        self.client = Client(api_key, api_secret)
        self.client.FUTURES_URL = TESTNET_URL

        logging.info("Connected to Binance Futures Testnet")

    def create_order(self, params):
        try:
            logging.info(f"API Request: {params}")
            response = self.client.futures_create_order(**params)
            logging.info(f"API Response: {response}")
            return response

        except Exception as e:
            logging.error(f"API Error: {e}")
            raise
