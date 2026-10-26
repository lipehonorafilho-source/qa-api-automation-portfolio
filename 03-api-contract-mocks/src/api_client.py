"""Small example client with validation and clear errors."""
from typing import Any
import requests


class ApiClientError(Exception):
    """Raised when an API response is invalid or unsuccessful."""


def normalize_user(payload: dict[str, Any]) -> dict[str, Any]:
    """Validate and return only the public fields expected by our app."""
    required = ("id", "name", "email")
    missing = [field for field in required if field not in payload]
    if missing:
        raise ApiClientError(f"Missing required fields: {', '.join(missing)}")

    if not isinstance(payload["id"], int):
        raise ApiClientError("Field 'id' must be an integer")
    if not isinstance(payload["name"], str) or not payload["name"].strip():
        raise ApiClientError("Field 'name' must be a non-empty string")
    if not isinstance(payload["email"], str) or "@" not in payload["email"]:
        raise ApiClientError("Field 'email' must be a valid-looking email")

    return {"id": payload["id"], "name": payload["name"].strip(), "email": payload["email"].lower()}


def fetch_user(user_id: int, http_get=requests.get) -> dict[str, Any]:
    """Fetch a user from a demo endpoint and validate the response."""
    if user_id <= 0:
        raise ValueError("user_id must be greater than zero")

    try:
        response = http_get(
            f"https://jsonplaceholder.typicode.com/users/{user_id}",
            timeout=5,
        )
    except requests.RequestException as exc:
        raise ApiClientError(f"Network request failed: {exc}") from exc

    if response.status_code != 200:
        raise ApiClientError(f"Unexpected HTTP status: {response.status_code}")

    try:
        payload = response.json()
    except ValueError as exc:
        raise ApiClientError("Response body is not valid JSON") from exc

    if not isinstance(payload, dict):
        raise ApiClientError("Response body must be a JSON object")

    return normalize_user(payload)
