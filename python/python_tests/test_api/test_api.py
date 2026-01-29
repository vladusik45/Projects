import requests

URL = "https://jsonplaceholder.typicode.com/posts"
def test_get():
    response = requests.get(f"{URL}/1")

    assert response.status_code == 200

    data = response.json()
    assert "id" in data
    assert "title" in data
    assert "body" in data
    assert "userId" in data

def test_post():
    payload = {
        "title": "test",
        "body": "test",
        "userId": 1
    }

    response = requests.post(URL, json=payload)

    assert response.status_code == 201

    data = response.json()
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]

def test_put():
    payload = {
        "id": 1,
        "title": "new",
        "body": "new",
        "userId": 1
    }

    response = requests.put(f"{URL}/1", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "new"
    assert data["body"] == "new"
