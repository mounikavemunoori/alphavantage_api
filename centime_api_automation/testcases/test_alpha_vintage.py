import requests
import random
import os
import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
from alphavintage import read_config

class TestCentime(object):

    def setup(self):
        self.key=read_config.read_config_data('alphavantage_data.config', 'keys', 'api_key')

    def test_key_none(self):
        """Raise an error when a key has not been given
        """
        key_None = read_config.read_config_data('alphavantage_data.config')
        try:
            if key_None is None:
                raise ValueError('The AlphaVantage API key must be provided '
                                 'either through the key parameter or '
                                 'through the environment variable '
                                 'ALPHAVANTAGE_API_KEY. Get a free key '
                                 'from the alphavantage website: '
                                 'https://www.alphavantage.co/support/#api-key')
        except ValueError as e:
            print(e)
            raise e

    def test_handle_api_call(self):
        """ Test that api call returns a json file as requested
        """
        url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=MSFT&interval=1min&apikey='+self.key
        print("hhdfjhdf-------->", url)
        response=requests.get(url)
        assert response.status_code == 200, 'status code be 200'
        data=response.json()
        assert isinstance(data, dict), 'Data must be a dictionary'

    def test_foreign_exchange_rate(self):
        """
        Test that api call returns the Realtime Currency Exchange Rate

        :return:
        """
        url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=JPY&apikey='+self.key
        response = requests.get(url)
        data = response.json()
        assert response.status_code==200
        assert isinstance(data, dict), 'Data must be a dictionary'
        assert  data['Realtime Currency Exchange Rate']['1. From_Currency Code']=='USD', 'Currency code should be in USD'
        assert data['Realtime Currency Exchange Rate']['3. To_Currency Code'] == 'JPY', 'Currency code should be in USD'


    def test_Digital_Crypto_Currencies(self):
        """
        Test that this API returns the realtime exchange rate for any pair of digital currency
        (e.g., Bitcoin) or physical currency (e.g., USD).
        :return:
        """
        url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=CNY&apikey='+self.key
        response = requests.get(url)
        data = response.json()
        assert response.status_code == 200
        assert isinstance(data, dict), 'Data must be a dictionary'
        assert data['Realtime Currency Exchange Rate']['1. From_Currency Code'] == 'BTC', 'From Currency code should be in BTC'
        assert data['Realtime Currency Exchange Rate'][
                   '3. To_Currency Code'] == 'CNY', 'To Currency code should be in CNY '

    def test_technical_indicator_sma_python3(self):
        """
        Test that this API returns the simple moving average (SMA) values
        :return:
        """
        url = 'https://www.alphavantage.co/query?function=SMA&symbol=IBM&interval=weekly&time_period=10&series_type=open&apikey='+self.key
        response = requests.get(url)
        data = response.json()
        assert response.status_code==200, 'Status code should be 200'
        random_key=random.choice(list(data['Technical Analysis: SMA'].keys()))
        assert isinstance(data['Technical Analysis: SMA'][random_key], dict), \
            'SMA values should be return in dictionary format'