import requests

class AuthClient:
    def __init__(self, base_url: str):
        self._base_url = base_url
        self._access_token = None
        self._refresh_token = None
        self._user_id = None

    def register(self, email: str, password: str):
        r = requests.post(f"{self._base_url}/auth/register", json={
            "email": email, "password": password
        })
        r.raise_for_status()
        self._user_id = r.json()["user_id"]

    def login(self, email: str, password: str):
        r = requests.post(f"{self._base_url}/auth/login", json={
            "email": email, "password": password
        })
        r.raise_for_status()
        data = r.json()
        self._access_token = data["access_token"]
        self._refresh_token = data["refresh_token"]
        self._user_id = self._user_id or data.get("user_id")

        if not self._user_id:
            self._user_id = data.get("user_id")

    def save(self, data: dict):
        r = requests.patch(f"{self._base_url}/progress/{self._user_id}",
            json=data,
            headers={"Authorization": f"Bearer {self._access_token}"}
        )
        r.raise_for_status()

    def load(self) -> dict:
        r = requests.get(f"{self._base_url}/progress/{self._user_id}",
            headers={"Authorization": f"Bearer {self._access_token}"}
        )
        r.raise_for_status()
        return r.json()

    def logout(self):
        requests.post(f"{self._base_url}/auth/logout", json={
            "refresh_token": self._refresh_token
        })
        self._access_token = None
        self._refresh_token = None
        self._user_id = None
    def create(self, data: dict):
        r = requests.post(
            f"{self._base_url}/progress/{self._user_id}",
            json=data,
            headers={"Authorization": f"Bearer {self._access_token}"}
        )
        r.raise_for_status()