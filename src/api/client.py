import requests
import os
from dotenv import load_dotenv
from keyring import set_password, get_password
from src.utils.logger import setup_logger

class APIClient:
    def __init__(self):
        load_dotenv()
        self.base_url = os.getenv("API_BASE_URL")
        self.logger = setup_logger()
        self.access_token = None
        self.refresh_token = None
    
    def set_tokens(self, access_token, refresh_token):
        self.access_token = access_token
        self.refresh_token = refresh_token
        set_password("BankingApp", "access_token", access_token)
        set_password("BankingApp", "refresh_token", refresh_token)
    
    def get_headers(self):
        if self.access_token:
            return {"Authorization": f"Bearer {self.access_token}"}
        return {}
    
    def post(self, endpoint, data):
        try:
            response = requests.post(
                f"{self.base_url}{endpoint}",
                json=data,
                headers=self.get_headers()
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            self.logger.error(f"API request failed: {str(e)}")
            return {"success": False, "message": str(e)}