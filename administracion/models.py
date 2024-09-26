#from django.db import models
import requests
from django.conf import settings
"""
class APIClient:
    BASE_URL = settings.API_URL

    def __init__(self, table_name):
        self.table_name = table_name

    def _make_request(self, where_condition=None, order_by=None, limit_clause=None, json_data=None, select_columns=None):
        url = self.BASE_URL
        payload = {
            "procedure": "select_json_entity",
            "parameters": {
                "table_name": self.table_name,
                "where_condition": where_condition,
                "order_by": order_by,
                "limit_clause": limit_clause,
                "json_data": json_data if json_data else {},
                "select_columns": select_columns
            }
        }
        response = requests.post(url, json=payload)
        response.raise_for_status()  
        return response.json()

    def get_data(self, where_condition=None, order_by=None, limit_clause=None, json_data=None, select_columns=None):
        data = self._make_request(where_condition, order_by, limit_clause, json_data, select_columns)
        return data.get('outputParams', {}).get('result', [])

"""