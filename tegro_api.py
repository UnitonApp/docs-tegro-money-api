"""
Общий модуль для работы с Tegro.money API
Этот модуль содержит базовую функциональность для подписи запросов и отправки данных
"""
import json
import hmac
import time
import requests
from hashlib import sha256


class TegroAPI:
    """Базовый класс для работы с Tegro.money API"""
    
    BASE_URL = 'https://tegro.money/api'
    
    def __init__(self, api_key, shop_id):
        """
        Инициализация API клиента
        
        Args:
            api_key (str): Секретный ключ API
            shop_id (str): Идентификатор магазина
        """
        self.api_key = api_key
        self.shop_id = shop_id
    
    def _create_signature(self, data):
        """
        Создание подписи для запроса
        
        Args:
            data (dict): Данные для подписи
            
        Returns:
            str: HEX строка подписи
        """
        body = json.dumps(data)
        signature = hmac.new(
            self.api_key.encode(), 
            body.encode(), 
            sha256
        ).hexdigest()
        return signature, body
    
    def _make_request(self, endpoint, data):
        """
        Выполнение запроса к API
        
        Args:
            endpoint (str): API endpoint (например, 'balance')
            data (dict): Данные запроса
            
        Returns:
            requests.Response: Ответ от сервера
        """
        # Добавляем обязательные поля
        request_data = {
            'shop_id': self.shop_id,
            'nonce': int(time.time()),
            **data
        }
        
        signature, body = self._create_signature(request_data)
        
        headers = {
            'Authorization': f'Bearer {signature}',
            'Content-Type': 'application/json',
        }
        
        url = f"{self.BASE_URL}/{endpoint}/"
        response = requests.post(url, data=body, headers=headers)
        
        return response


# Функции-обертки для совместимости с существующими примерами
def create_api_signature(api_key, data):
    """
    Создание подписи для данных (для обратной совместимости)
    
    Args:
        api_key (str): Секретный ключ API
        data (dict): Данные для подписи
        
    Returns:
        tuple: (подпись, JSON строка данных)
    """
    body = json.dumps(data)
    signature = hmac.new(api_key.encode(), body.encode(), sha256).hexdigest()
    return signature, body


def make_api_request(endpoint, api_key, data):
    """
    Выполнение запроса к API (для обратной совместимости)
    
    Args:
        endpoint (str): API endpoint
        api_key (str): Секретный ключ API
        data (dict): Данные запроса
        
    Returns:
        requests.Response: Ответ от сервера
    """
    signature, body = create_api_signature(api_key, data)
    
    headers = {
        'Authorization': f'Bearer {signature}',
        'Content-Type': 'application/json',
    }
    
    url = f"https://tegro.money/api/{endpoint}/"
    response = requests.post(url, data=body, headers=headers)
    
    return response