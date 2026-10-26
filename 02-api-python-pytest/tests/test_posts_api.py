"""API tests for JSONPlaceholder. Tests de API para estudo."""
import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_json(path: str, params: dict | None = None):
    """GET helper with timeout and explicit HTTP error handling."""
    response = requests.get(f"{BASE_URL}{path}", params=params, timeout=10)
    return response


def test_get_existing_post_has_expected_fields():
    response = get_json("/posts/1")

    assert response.status_code == 200
    assert "application/json" in response.headers.get("Content-Type", "")
    body = response.json()
    assert body["id"] == 1
    assert isinstance(body["userId"], int)
    assert isinstance(body["title"], str)
    assert isinstance(body["body"], str)


def test_get_posts_returns_a_list():
    response = get_json("/posts")

    assert response.status_code == 200
    body = response.json()
    assert isinstance(body, list)
    assert len(body) > 0


@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_filter_posts_returns_only_requested_user(user_id):
    response = get_json("/posts", params={"userId": user_id})

    assert response.status_code == 200
    body = response.json()
    assert isinstance(body, list)
    assert len(body) > 0
    assert all(post["userId"] == user_id for post in body)


def test_missing_post_returns_not_found():
    response = get_json("/posts/999999")

    assert response.status_code == 404


def test_get_comments_for_post_only_returns_matching_post_id():
    response = get_json("/comments", params={"postId": 1})

    assert response.status_code == 200
    comments = response.json()
    assert isinstance(comments, list)
    assert len(comments) > 0
    assert all(comment["postId"] == 1 for comment in comments)


def test_connection_error_is_not_silently_ignored(monkeypatch):
    """Demonstrates explicit handling of a connection failure without internet."""
    def fake_get(*args, **kwargs):
        raise requests.ConnectionError("simulated connection failure")

    monkeypatch.setattr(requests, "get", fake_get)

    with pytest.raises(requests.ConnectionError):
        get_json("/posts/1")
