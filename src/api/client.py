import os
import requests
from dotenv import load_dotenv
from keyring import set_password, get_password
from pydantic import BaseModel
from typing import Optional, Dict, Any, List
from src.schemas.schemas import (
    AnalyticsSummary, CardCreate, CardResponse, CardUpdate,
    LoanApply, LoanPaymentCreate, LoanPaymentResponse, LoanResponse,
    LoanTypeResponse, LoginResponse, PaginatedResponse, TokenRefresh,
    TransferCreate, TransferResponse, UserCreate, UserLogin,
    UserpasswordUpdate, UserResponse, UserUpdate,
)
from src.utils.logger import setup_logger

class APIClient:
    def __init__(self):
        load_dotenv()
        self.base_url = os.getenv("API_BASE_URL", "https://aut-bank-backend.up.railway.app")
        self.logger = setup_logger()
        self.session = requests.Session()
        self.access_token = get_password("BankingApp", "access_token")
        self.refresh_token = get_password("BankingApp", "refresh_token")

        self.skip_auth_routes = [
            "/api/v1/users/check_uniqueness",
            "/api/v1/users/send_verification",
            "/api/v1/users/register",
            "/api/v1/users/login",
            "/api/v1/users/refresh",
        ]

    def set_tokens(self, access_token: str, refresh_token: str):
        self.access_token = access_token
        self.refresh_token = refresh_token
        set_password("BankingApp", "access_token", access_token)
        set_password("BankingApp", "refresh_token", refresh_token)

    def _request(
        self,
        method: str,
        endpoint: str,
        data: Optional[BaseModel] = None,
        params: Optional[Dict[str, Any]] = None,
        json_body: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        url = f"{self.base_url}{endpoint}"

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        if endpoint not in self.skip_auth_routes and self.access_token:
            headers["Authorization"] = f"Bearer {self.access_token}"

        json_payload = json_body or (data.dict(exclude_unset=True) if data else None)

        # Terminal and logger debug log
        log_message = f"\n📤 SENDING REQUEST 📤\n" \
                      f"➡️ Method: {method.upper()}\n" \
                      f"➡️ URL: {url}\n" \
                      f"➡️ Headers: {headers}\n" \
                      f"➡️ Params: {params}\n" \
                      f"➡️ Body: {json_payload}\n"
        print(log_message)
        self.logger.debug(log_message)

        try:
            response = self.session.request(
                method=method,
                url=url,
                headers=headers,
                params=params,
                json=json_payload
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            self.logger.error(f"API request failed: {method} {endpoint} - {str(e)}")
            if e.response is not None:
                self.logger.error(f"Response Body: {e.response.text}")
            raise Exception(f"API request failed: {str(e)}")

    # Authentication
    def login(self, login_data: UserLogin) -> LoginResponse:
    # Ensure you send the correct field names as per the API specs
        response = self._request("POST", "/api/v1/users/login", data=login_data)
        data = response["data"]
        self.set_tokens(data["access_token"], data["refresh_token"])
        return LoginResponse(**data)


    def register(self, user_data: UserCreate) -> UserResponse:
        response = self._request("POST", "/api/v1/users/register", data=user_data)
        return UserResponse(**response["data"])

    def refresh_token(self) -> Dict:
        data = TokenRefresh(token=self.refresh_token)
        response = self._request("POST", "/api/v1/users/refresh", data=data)
        new_tokens = response["data"]
        self.set_tokens(new_tokens["access_token"], new_tokens["refresh_token"])
        return new_tokens

    # Profile Management
    def get_profile(self) -> UserResponse:
        response = self._request("GET", "/api/v1/users/me")
        return UserResponse(**response["data"])

    def update_profile(self, update_data: UserUpdate) -> UserResponse:
        response = self._request("PUT", "/api/v1/users/me", data=update_data)
        return UserResponse(**response["data"])

    def update_password(self, password_data: UserpasswordUpdate) -> Dict:
        return self._request("PUT", "/api/v1/users/me/password", data=password_data)

    # Transactions
    def get_transactions(self, page: int = 1, per_page: int = 10, **filters) -> PaginatedResponse:
        params = {"page": page, "per_page": per_page, **filters}
        response = self._request("GET", "/api/v1/users/transactions", params=params)
        return PaginatedResponse(**response)

    def export_transactions(self, **filters) -> bytes:
        params = filters
        url = f"{self.base_url}/api/v1/users/transactions/export"
        headers = {
            "Accept": "application/json",
        }
        if self.access_token:
            headers["Authorization"] = f"Bearer {self.access_token}"

        response = self.session.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.content

    # Transfers
    def create_transfer(self, transfer_data: TransferCreate) -> TransferResponse:
        response = self._request("POST", "/api/v1/users/transfer", data=transfer_data)
        return TransferResponse(**response["data"])

    # Cards
    def get_cards(self, page=1, per_page=10, sort_by="CardID", order="asc") -> PaginatedResponse:
        params = {"page": page, "per_page": per_page, "sort_by": sort_by, "order": order}
        response = self._request("GET", "/api/v1/users/cards", params=params)
        return PaginatedResponse(
            items=[CardResponse(**item) for item in response["items"]],
            **response
        )

    def create_card(self, card_data: CardCreate) -> CardResponse:
        response = self._request("POST", "/api/v1/users/cards", data=card_data)
        return CardResponse(**response["data"])

    def update_card(self, card_id: int, update_data: CardUpdate) -> CardResponse:
        response = self._request("PUT", f"/api/v1/users/cards/{card_id}", data=update_data)
        return CardResponse(**response["data"])

    def delete_card(self, card_id: int) -> Dict:
        return self._request("DELETE", f"/api/v1/users/cards/{card_id}")

    # Loans
    def apply_loan(self, loan_data: LoanApply) -> LoanResponse:
        response = self._request("POST", "/api/v1/users/loans/apply", data=loan_data)
        return LoanResponse(**response["data"])

    def get_loan_types(self) -> List[LoanTypeResponse]:
        response = self._request("GET", "/api/v1/users/loans/types")
        return [LoanTypeResponse(**item) for item in response["data"]]

    def make_loan_payment(self, payment_data: LoanPaymentCreate) -> LoanPaymentResponse:
        response = self._request("POST", "/api/v1/users/loans/payments", data=payment_data)
        return LoanPaymentResponse(**response["data"])

    def get_loans(self, page=1, per_page=10, status=None, sort_by="CreatedAt", order="desc") -> PaginatedResponse:
        params = {"page": page, "per_page": per_page, "status": status, "sort_by": sort_by, "order": order}
        response = self._request("GET", "/api/v1/users/loans", params=params)
        return PaginatedResponse(
            items=[LoanResponse(**item) for item in response["items"]],
            **response
        )

    def get_loan_payments(self, loan_id: int, page=1, per_page=10) -> PaginatedResponse:
        params = {"page": page, "per_page": per_page}
        response = self._request("GET", f"/api/v1/users/loans/{loan_id}/payments", params=params)
        return PaginatedResponse(
            items=[LoanPaymentResponse(**item) for item in response["items"]],
            **response
        )

    # Analytics
    def get_analytics_summary(self) -> AnalyticsSummary:
        response = self._request("GET", "/api/v1/users/analytics/summary")
        return AnalyticsSummary(**response["data"])
