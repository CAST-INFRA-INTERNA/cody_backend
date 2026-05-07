"""Simple JWT tests - no dependency on application configuration"""

import os
import sys
from datetime import UTC, datetime, timedelta

import pytest

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from schemas.login import JWTPayload  # noqa: E402
from utils.jwt import create_access_token, create_token_pair, verify_token  # noqa: E402


class TestSimpleJWT:
    """Simple JWT test class"""

    def test_create_token_pair(self):
        """Test creating a token pair"""
        user_id = 1

        access_token, refresh_token = create_token_pair(user_id=user_id)

        assert isinstance(access_token, str)
        assert isinstance(refresh_token, str)
        assert len(access_token) > 0
        assert len(refresh_token) > 0
        assert access_token != refresh_token

    def test_verify_access_token(self):
        """Test verifying an access token"""
        user_id = 1

        access_token, _ = create_token_pair(user_id)

        # Verify access token
        payload = verify_token(access_token, token_type="access")

        assert payload.user_id == user_id
        assert payload.token_type == "access"

    def test_verify_refresh_token(self):
        """Test verifying a refresh token"""
        user_id = 2

        _, refresh_token = create_token_pair(user_id)

        # Verify refresh token
        payload = verify_token(refresh_token, token_type="refresh")

        assert payload.user_id == user_id
        assert payload.token_type == "refresh"

    def test_token_type_validation(self):
        """Test token type validation"""
        user_id = 3

        access_token, refresh_token = create_token_pair(user_id)

        # Verifying an access token as a refresh token should fail
        with pytest.raises(Exception):  # noqa: B017
            verify_token(access_token, token_type="refresh")

        # Verifying a refresh token as an access token should fail
        with pytest.raises(Exception):  # noqa: B017
            verify_token(refresh_token, token_type="access")

    def test_expired_token(self):
        """Test expired token"""
        # Create an already-expired token
        expire = datetime.now(UTC) - timedelta(minutes=1)  # Expired 1 minute ago

        payload = JWTPayload(
            user_id=4,
            exp=expire,
            token_type="access",
        )

        expired_token = create_access_token(data=payload)

        # Verifying an expired token should fail
        with pytest.raises(Exception):  # noqa: B017
            verify_token(expired_token, token_type="access")

    def test_invalid_token(self):
        """Test invalid token"""
        invalid_token = "invalid.token.here"

        with pytest.raises(Exception):  # noqa: B017
            verify_token(invalid_token, token_type="access")
