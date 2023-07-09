import json
import hmac
import time
import requests
from hashlib import sha256

api_key = 'EEFA1913EA9D9351469B1E5D852A'

data = {
    "shop_id": "1913EA935149B1E5D852A",
    "nonce": 1613435880,
    "payment_id": "test order"
}

body = json.dumps(data)
sign = hmac.new(api_key.encode(), body.encode(), sha256).hexdigest()

headers = {
    'Authorization': f'Bearer {sign}',
    'Content-Type': 'application/json',
}

response = requests.post("https://tegro.money/api/order/", data=body, headers=headers)

print(response.text)
