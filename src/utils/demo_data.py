class DemoData:
    def __init__(self):
        self.users = {
            "user@example.com": {
                "password": "password123",
                "name": "John Doe",
                "address": "123 Main St",
                "balance": 5000.00
            }
        }
    
    def validate_login(self, email, password):
        user = self.users.get(email)
        if user and user["password"] == password:
            return {
                "success": True,
                "user": {
                    "name": user["name"],
                    "email": email,
                    "balance": user["balance"]
                }
            }
        return {"success": False, "message": "Invalid email or password"}
    
    def register_user(self, user_data):
        email = user_data.get("email")
        if email in self.users:
            return {"success": False, "message": "Email already registered"}
        
        self.users[email] = {
            "password": user_data.get("password"),
            "name": user_data.get("name"),
            "address": user_data.get("address"),
            "balance": 1000.00  # Starting balance for new users
        }
        
        return {
            "success": True,
            "user": {
                "name": user_data.get("name"),
                "email": email,
                "balance": 1000.00  # Starting balance for new users
            }
        } 