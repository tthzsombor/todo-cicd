import pytest
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json() == {"status": "ok"}


def test_add_and_list(client):
    r = client.post("/api/todos", json={"title": "Tanulás"})
    assert r.status_code == 201
    assert r.get_json()["title"] == "Tanulás"
    assert len(client.get("/api/todos").get_json()) == 1


def test_add_empty_title_rejected(client):
    assert client.post("/api/todos", json={"title": "  "}).status_code == 400


def test_toggle(client):
    tid = client.post("/api/todos", json={"title": "x"}).get_json()["id"]
    assert client.put(f"/api/todos/{tid}/toggle").get_json()["done"] is True


def test_delete(client):
    tid = client.post("/api/todos", json={"title": "x"}).get_json()["id"]
    assert client.delete(f"/api/todos/{tid}").status_code == 204
    assert client.delete(f"/api/todos/{tid}").status_code == 404


def test_index_page(client):
    assert client.get("/").status_code == 200
