import requests
import json
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64


class Credentials:
    consumer_key = '77bgGpmlOxlgJu6oEXhEgUgnu0j2WYxA'
    consumer_secret = 'viM8ejHgtEmtPTHd'
    passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'


class MpesaAccessToken:
    t = requests.get(Credentials.api_URL, auth=HTTPBasicAuth(Credentials.consumer_key,  Credentials.consumer_secret))
    access_token = json.loads(t.text)
    validated_access_token = access_token["access_token"]


class MpesaPpassword:
    pay_time = datetime.now().strftime('%Y%m%d%H%M%S')
    short_code = "174379"
    OffSetValue = '0'
    passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'

    encode = short_code + passkey + pay_time

    encoded = base64.b64encode(encode.encode())
    decoded = encoded.decode('utf-8')