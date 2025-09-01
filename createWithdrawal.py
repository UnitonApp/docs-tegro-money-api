import json
import hmac
import time
import requests
from hashlib import sha256

# ВНИМАНИЕ: Замените на ваши реальные API данные!
# Никогда не оставляйте реальные ключи в коде!
api_key = 'YOUR_SECRET_API_KEY_HERE'  # Замените на ваш секретный ключ

data = {
    'shop_id': 'YOUR_SHOP_ID_HERE',  # Замените на ваш shop_id
    'nonce': int(time.time()),
    'currency': 'RUB',
    'account': 'killme',
    'amount': 1200,
    'payment_id': 'argr',
    'payment_system': 5
}

body = json.dumps(data)
sign = hmac.new(api_key.encode(), body.encode(), sha256).hexdigest()

headers = {
    'Authorization': f'Bearer {sign}',
    'Content-Type': 'application/json',
}

response = requests.post("https://tegro.money/api/createWithdrawal/", data=body, headers=headers)

print(response.text)
