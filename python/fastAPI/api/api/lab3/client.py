import requests
from typing import Optional, List, Dict

class APIError(Exception):
    pass

class LibraryClient:
    def __init__(self, api_url: str, token: Optional[str] = None):
        self.api_url = api_url.rstrip("/")
        self.token = token
        self.headers = {"Content-Type": "application/json"}
        if token:
            self.headers["Authorization"] = f"Bearer {token}"

    #Пользователи
    def create_user(self, email: str, password: str, idempotency_key: Optional[str] = None) -> Dict:
        headers = self.headers.copy()
        if idempotency_key:
            headers["Idempotency-Key"] = idempotency_key

        data = {"email": email, "password": password}
        response = requests.post(f"{self.api_url}/api/v1/users", json=data, headers=headers)
        return self._handle_response(response)

    def list_users(self, limit: int = 10, offset: int = 0) -> List[Dict]:
        params = {"limit": limit, "offset": offset}
        response = requests.get(f"{self.api_url}/api/v1/users", headers=self.headers, params=params)
        return self._handle_response(response)

    def delete_user(self, user_id: str) -> Dict:
        response = requests.delete(f"{self.api_url}/api/v1/users/{user_id}", headers=self.headers)
        return self._handle_response(response)

    #Книги
    def create_book(self, title: str, author: str, idempotency_key: Optional[str] = None) -> Dict:
        headers = self.headers.copy()
        if idempotency_key:
            headers["Idempotency-Key"] = idempotency_key

        data = {"title": title, "author": author}
        response = requests.post(f"{self.api_url}/api/v1/books", json=data, headers=headers)
        return self._handle_response(response)

    def list_books(self, limit: int = 10, offset: int = 0, include: Optional[str] = None) -> List[Dict]:
        params = {"limit": limit, "offset": offset}
        if include:
            params["include"] = include
        response = requests.get(f"{self.api_url}/api/v1/books", headers=self.headers, params=params)
        return self._handle_response(response)

    def update_book(self, book_id: str, title: Optional[str] = None, author: Optional[str] = None) -> Dict:
        data = {}
        if title: data["title"] = title
        if author: data["author"] = author
        response = requests.put(f"{self.api_url}/api/v1/books/{book_id}", json=data, headers=self.headers)
        return self._handle_response(response)

    def delete_book(self, book_id: str) -> Dict:
        response = requests.delete(f"{self.api_url}/api/v1/books/{book_id}", headers=self.headers)
        return self._handle_response(response)

    def internal_stats(self, secret_key: str) -> Dict:
        params = {"secret_key": secret_key}
        response = requests.get(f"{self.api_url}/api/v1/internal/stats", headers=self.headers, params=params)
        return self._handle_response(response)

    def _handle_response(self, response: requests.Response):
        if response.status_code >= 400:
            try:
                detail = response.json()
            except:
                detail = response.text
            raise APIError(f"Error {response.status_code}: {detail}")
        try:
            return response.json()
        except:
            return response.text

if __name__ == "__main__":
    client = LibraryClient(api_url="https://gitverse.ru/leof/library-rest-api/content/master")

    user = client.create_user("test@example.com", "password123", idempotency_key="user-001")
    print("Создан пользователь:", user)

    users = client.list_users(limit=5, offset=0)
    print("Пользователи:", users)

    book = client.create_book("Python для новичков", "Иван Иванов", idempotency_key="book-001")
    print("Создана книга:", book)

    books = client.list_books(limit=5, offset=0, include="id,title")
    print("Книги:", books)

    stats = client.internal_stats(secret_key="INTERNAL_SECRET")
    print("Статистика:", stats)
