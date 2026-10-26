import requests
import pytest
from unittest.mock import Mock

from src.api_client import ApiClientError, fetch_user, normalize_user


def test_normalize_user_trims_name_and_lowercases_email():
    result = normalize_user({"id": 7, "name": "  Ana QA  ", "email": "ANA@EXAMPLE.COM"})

    assert result == {"id": 7, "name": "Ana QA", "email": "ana@example.com"}


@pytest.mark.parametrize(
    "payload",
    [
        {"name": "Ana", "email": "ana@example.com"},
        {"id": 1, "email": "ana@example.com"},
        {"id": 1, "name": "Ana"},
    ],
)
def test_normalize_user_rejects_missing_required_fields(payload):
    with pytest.raises(ApiClientError, match="Missing required fields"):
        normalize_user(payload)


def test_normalize_user_rejects_invalid_email():
    with pytest.raises(ApiClientError, match="valid-looking email"):
        normalize_user({"id": 1, "name": "Ana", "email": "invalid"})


def test_fetch_user_returns_normalized_data_using_mock():
    fake_response = Mock()
    fake_response.status_code = 200
    fake_response.json.return_value = {
        "id": 2,
        "name": "Leanne Graham",
        "email": "SINCERE@APRI.NET",
    }
    fake_get = Mock(return_value=fake_response)

    result = fetch_user(2, http_get=fake_get)

    assert result["id"] == 2
    assert result["email"] == "sincere@apri.net"
    fake_get.assert_called_once_with(
        "https://jsonplaceholder.typicode.com/users/2",
        timeout=5,
    )


def test_fetch_user_raises_for_non_200_status():
    fake_response = Mock()
    fake_response.status_code = 500
    fake_get = Mock(return_value=fake_response)

    with pytest.raises(ApiClientError, match="Unexpected HTTP status: 500"):
        fetch_user(3, http_get=fake_get)


def test_fetch_user_wraps_connection_error():
    fake_get = Mock(side_effect=requests.ConnectionError("network down"))

    with pytest.raises(ApiClientError, match="Network request failed"):
        fetch_user(1, http_get=fake_get)


def test_fetch_user_rejects_non_positive_id():
    with pytest.raises(ValueError, match="greater than zero"):
        fetch_user(0)
