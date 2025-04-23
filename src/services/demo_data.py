class DemoDataService:
    def __init__(self):
        # Demo user credentials
        self.users = {
            "demo_user": {
                "username": "demo_user",
                "password": "Demo123",
                "email": "demo@example.com",
                "first_name": "Demo",
                "last_name": "User",
                "balance": 5000.00,
                "transactions": [
                    {
                        "id": 1,
                        "type": "deposit",
                        "amount": 1000.00,
                        "date": "2024-01-15",
                        "description": "Salary deposit"
                    },
                    {
                        "id": 2,
                        "type": "withdrawal",
                        "amount": -50.00,
                        "date": "2024-01-16",
                        "description": "ATM withdrawal"
                    }
                ]
            }
        }
        self.current_user = None

    def login(self, username, password):
        user = self.users.get(username)
        if user and user["password"] == password:
            self.current_user = user
            return True
        return False

    def get_user_data(self):
        return self.current_user if self.current_user else None

    def get_balance(self):
        return self.current_user["balance"] if self.current_user else 0.00

    def get_transactions(self):
        return self.current_user["transactions"] if self.current_user else []

    def logout(self):
        self.current_user = None