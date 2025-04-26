from typing import Dict, Optional

class UserService:
    def __init__(self):
        # Temporary mock data - replace with actual database/API calls
        self.mock_user = {
            "id": "12345",
            "username": "demo@example.com",
            "full_name": "Demo User",
            "balance": 5000.00,
            "account_number": "1234567890",
            "account_type": "Savings",
            "last_login": "2024-01-20 10:30:00"
        }

    def getUserDetails(self, user_id: str = "12345") -> Dict:
        """Get user details including account information"""
        return self.mock_user

    def updateUserDetails(self, user_id: str, details: Dict) -> bool:
        """Update user details"""
        self.mock_user.update(details)
        return True

    def validateCredentials(self, username: str, password: str) -> Optional[str]:
        """Validate user credentials and return user_id if valid"""
        # Mock validation - replace with actual authentication
        if username == "demo@example.com" and password == "Demo123!":
            return "12345"
        return None

# Create a singleton instance
user_service = UserService()

# Export functions for easy access
def getUserDetails(user_id: str = "12345") -> Dict:
    return user_service.getUserDetails(user_id)

def updateUserDetails(user_id: str, details: Dict) -> bool:
    return user_service.updateUserDetails(user_id, details)

def validateCredentials(username: str, password: str) -> Optional[str]:
    return user_service.validateCredentials(username, password)