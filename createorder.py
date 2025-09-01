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
    "currency": "RUB",
    "amount": 1200,
    "order_id": "test order",
    "payment_system": 5,
    "fields": {
        "email": "user@email.ru",
        "phone": "79111231212"
    },
    "receipt": {
        "items": [
            {
                "name": "test item 1",
                "count": 1,
                "price": 600
            },
            {
                "name": "test item 2",
                "count": 1,
                "price": 600
            }
        ]
    }
}

body = json.dumps(data)
sign = hmac.new(api_key.encode(), body.encode(), sha256).hexdigest()

headers = {
    'Authorization': f'Bearer {sign}',
    'Content-Type': 'application/json',
}

response = requests.post("https://tegro.money/api/createOrder/", data=body, headers=headers)

print(response.text)
