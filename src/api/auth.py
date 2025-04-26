from src.api.client import APIClient
import logging

logger = logging.getLogger(__name__)

class AuthAPI:
    def __init__(self):
        self.client = APIClient()

    async def login(self, email, password):
        logger.debug(f"AuthAPI login called with email: {email}")
        # Mock demo credentials
        if email == "user@example.com" and password == "password123":
            logger.info("Demo credentials matched, returning mock token")
            return {"data": {"access_token": "demo_token"}}
        else:
            logger.error("Invalid credentials")
            raise Exception("Invalid email or password")

    async def register(self, user_data):
        logger.debug(f"Registering user: {user_data['Email']}")
        # Mock registration for testing
        return {"data": {"user_id": "mock_user_id"}}

    async def request(self, method, endpoint, json=None):
        logger.debug(f"Mock API request: {method} {endpoint}")
        # Mock other requests if needed
        return {"data": {}}