from pydantic import BaseModel, EmailStr, constr, validator

class UserCreateSchema(BaseModel):
    Username: EmailStr
    FullName: constr(min_length=2, max_length=50)
    Password: constr(min_length=8)

    @validator('Password')
    def password_strength(cls, v):
        if not any(c.isupper() for c in v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not any(c.islower() for c in v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not any(c.isdigit() for c in v):
            raise ValueError('Password must contain at least one number')
        return v

class UserLoginSchema(BaseModel):
    Username: EmailStr
    Password: constr(min_length=8)

    @validator('Password')
    def password_strength(cls, v):
        if not any(c.isupper() for c in v):
            raise ValueError('Password must contain at least one uppercase letter')
        if not any(c.islower() for c in v):
            raise ValueError('Password must contain at least one lowercase letter')
        if not any(c.isdigit() for c in v):
            raise ValueError('Password must contain at least one number')
        return v