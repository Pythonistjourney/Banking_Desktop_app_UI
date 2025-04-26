import requests

class APIClient:
    def __init__(self, base_url="https://aut-bank-backend.up.railway.app"):
        self.base_url = base_url
        self.session = requests.Session()
        self.token = None

    def set_token(self, token):
        self.token = token
        if token:
            self.session.headers.update({"Authorization": f"Bearer {token}"})
        else:
            self.session.headers.pop("Authorization", None)

    def signup(self, user_data):
        response = self.session.post(f"{self.base_url}/auth/signup", json=user_data)
        return response.json()

    def login(self, username, password):
        response = self.session.post(
            f"{self.base_url}/auth/login",
            json={"username": username, "password": password}
        )
        if response.status_code == 200:
            data = response.json()
            self.set_token(data.get("token"))
        return response.json()

    def logout(self):
        self.set_token(None)