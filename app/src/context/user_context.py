class UserContext:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.user = None
            cls._instance.token = None
        return cls._instance
    
    def set_user(self, user_data, token):
        self.user = user_data
        self.token = token
    
    def get_user(self):
        return self.user
    
    def get_token(self):
        return self.token
    
    def clear(self):
        self.user = None
        self.token = None