from datetime import date
from pydantic import BaseModel, EmailStr, constr, validator

class UserLogin(BaseModel):
    login_id: str
    Password: constr(min_length=8)

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: constr(min_length=8)
    first_name: str
    last_name: str
    DateOfBirth: date
    CNIC: str  # Changed from constr with pattern to str

    @validator('CNIC')
    def validate_cnic(cls, v):
        import re
        if not re.match(r'^\d{5}-\d{7}-\d{1}$', v):
            raise ValueError('CNIC must be in format: XXXXX-XXXXXXX-X')
        return v

    @validator('password')
    def password_strength(cls, v):
        if not any(c.isupper() for c in v):
            raise ValueError('password must contain at least one uppercase letter')
        if not any(c.islower() for c in v):
            raise ValueError('password must contain at least one lowercase letter')
        if not any(c.isdigit() for c in v):
            raise ValueError('password must contain at least one number')
        return v

class UserUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr | None = None

class UserpasswordUpdate(BaseModel):
    current_password: str
    new_password: constr(min_length=8)

    @validator('new_password')
    def password_strength(cls, v):
        if not any(c.isupper() for c in v):
            raise ValueError('password must contain at least one uppercase letter')
        if not any(c.islower() for c in v):
            raise ValueError('password must contain at least one lowercase letter')
        if not any(c.isdigit() for c in v):
            raise ValueError('password must contain at least one number')
        return v

class TokenRefresh(BaseModel):
    token: str

class LoginResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    first_name: str
    last_name: str
    is_active: bool
    created_at: date

class PaginatedResponse(BaseModel):
    items: list
    total: int
    page: int
    per_page: int
    total_pages: int

class TransferCreate(BaseModel):
    recipient_account: str
    amount: float
    description: str | None = None

class TransferResponse(BaseModel):
    id: int
    sender_account: str
    recipient_account: str
    amount: float
    description: str | None = None
    status: str
    created_at: date

class CardCreate(BaseModel):
    card_type: str
    currency: str

class CardUpdate(BaseModel):
    is_active: bool | None = None
    daily_limit: float | None = None

class CardResponse(BaseModel):
    id: int
    card_number: str
    card_type: str
    currency: str
    is_active: bool
    daily_limit: float
    created_at: date

class LoanApply(BaseModel):
    loan_type_id: int
    amount: float
    term_months: int
    purpose: str

class LoanResponse(BaseModel):
    id: int
    loan_type: str
    amount: float
    term_months: int
    interest_rate: float
    monthly_payment: float
    total_payment: float
    remaining_balance: float
    status: str
    created_at: date

class LoanTypeResponse(BaseModel):
    id: int
    name: str
    min_amount: float
    max_amount: float
    min_term: int
    max_term: int
    interest_rate: float
    requirements: list[str]

class LoanPaymentCreate(BaseModel):
    loan_id: int
    amount: float

class LoanPaymentResponse(BaseModel):
    id: int
    loan_id: int
    amount: float
    payment_date: date
    status: str

class AnalyticsSummary(BaseModel):
    total_balance: float
    total_income: float
    total_expenses: float
    loan_summary: dict
    recent_transactions: list
