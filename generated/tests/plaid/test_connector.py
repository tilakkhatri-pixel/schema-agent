# =============================================================================
# AUTO-GENERATED — DO NOT EDIT MANUALLY
# Partner : plaid
# =============================================================================
from __future__ import annotations

import pytest
from unittest.mock import AsyncMock, MagicMock, patch
from typing import Any, Dict, List

# Import the generated connector
from generated.connectors.plaid.connector import PlaidConnector


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def credentials() -> Dict[str, Any]:
    """Minimal credentials for testing — all values are mocked."""
    return {
        "api_key": "test-api-key-12345",
        "header_name": "X-Api-Key",
    }


@pytest.fixture
def connector(credentials) -> PlaidConnector:
    return PlaidConnector(firm_id="firm-001", credentials=credentials)


# ---------------------------------------------------------------------------
# Unit tests — one per entity
# ---------------------------------------------------------------------------

class TestTransactions:

    @pytest.mark.asyncio
    async def test_fetch_transactions_returns_list(self, connector):
        """fetch_transactions must return a list."""
        mock_response = {
            "data": [{"id": "1", "transaction_name": "Test Record"}],
        }
        with patch.object(connector.http, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = mock_response
            results = await connector.fetch_transactions()
        assert isinstance(results, list)
        assert len(results) >= 0

    @pytest.mark.asyncio
    async def test_fetch_transactions_handles_empty_response(self, connector):
        """fetch_transactions must handle empty pages without error."""
        mock_response = {"data": []}
        with patch.object(connector.http, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = mock_response
            results = await connector.fetch_transactions()
        assert results == []

    @pytest.mark.asyncio
    async def test_fetch_transactions_rate_limit_checked(self, connector):
        """fetch_transactions must call _check_rate_limit before any request."""
        with patch.object(connector, "_check_rate_limit", new_callable=AsyncMock) as mock_rl, \
             patch.object(connector.http, "get", new_callable=AsyncMock, return_value={"data": []}):
            await connector.fetch_transactions()
        mock_rl.assert_called_once()

class TestAccounts:

    @pytest.mark.asyncio
    async def test_fetch_accounts_returns_list(self, connector):
        """fetch_accounts must return a list."""
        mock_response = {
            "data": [{"id": "1", "account_name": "Test Record"}],
        }
        with patch.object(connector.http, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = mock_response
            results = await connector.fetch_accounts()
        assert isinstance(results, list)
        assert len(results) >= 0

    @pytest.mark.asyncio
    async def test_fetch_accounts_handles_empty_response(self, connector):
        """fetch_accounts must handle empty pages without error."""
        mock_response = {"data": []}
        with patch.object(connector.http, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = mock_response
            results = await connector.fetch_accounts()
        assert results == []

    @pytest.mark.asyncio
    async def test_fetch_accounts_rate_limit_checked(self, connector):
        """fetch_accounts must call _check_rate_limit before any request."""
        with patch.object(connector, "_check_rate_limit", new_callable=AsyncMock) as mock_rl, \
             patch.object(connector.http, "get", new_callable=AsyncMock, return_value={"data": []}):
            await connector.fetch_accounts()
        mock_rl.assert_called_once()

class TestPositions:

    @pytest.mark.asyncio
    async def test_fetch_positions_returns_list(self, connector):
        """fetch_positions must return a list."""
        mock_response = {
            "data": [{"id": "1", "position_name": "Test Record"}],
        }
        with patch.object(connector.http, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = mock_response
            results = await connector.fetch_positions()
        assert isinstance(results, list)
        assert len(results) >= 0

    @pytest.mark.asyncio
    async def test_fetch_positions_handles_empty_response(self, connector):
        """fetch_positions must handle empty pages without error."""
        mock_response = {"data": []}
        with patch.object(connector.http, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = mock_response
            results = await connector.fetch_positions()
        assert results == []

    @pytest.mark.asyncio
    async def test_fetch_positions_rate_limit_checked(self, connector):
        """fetch_positions must call _check_rate_limit before any request."""
        with patch.object(connector, "_check_rate_limit", new_callable=AsyncMock) as mock_rl, \
             patch.object(connector.http, "get", new_callable=AsyncMock, return_value={"data": []}):
            await connector.fetch_positions()
        mock_rl.assert_called_once()

class TestContacts:

    @pytest.mark.asyncio
    async def test_fetch_contacts_returns_list(self, connector):
        """fetch_contacts must return a list."""
        mock_response = {
            "data": [{"id": "1", "contact_name": "Test Record"}],
        }
        with patch.object(connector.http, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = mock_response
            results = await connector.fetch_contacts()
        assert isinstance(results, list)
        assert len(results) >= 0

    @pytest.mark.asyncio
    async def test_fetch_contacts_handles_empty_response(self, connector):
        """fetch_contacts must handle empty pages without error."""
        mock_response = {"data": []}
        with patch.object(connector.http, "get", new_callable=AsyncMock) as mock_get:
            mock_get.return_value = mock_response
            results = await connector.fetch_contacts()
        assert results == []

    @pytest.mark.asyncio
    async def test_fetch_contacts_rate_limit_checked(self, connector):
        """fetch_contacts must call _check_rate_limit before any request."""
        with patch.object(connector, "_check_rate_limit", new_callable=AsyncMock) as mock_rl, \
             patch.object(connector.http, "get", new_callable=AsyncMock, return_value={"data": []}):
            await connector.fetch_contacts()
        mock_rl.assert_called_once()


# ---------------------------------------------------------------------------
# Integration smoke test (requires live credentials — skipped by default)
# ---------------------------------------------------------------------------

@pytest.mark.skip(reason="Requires live credentials")
@pytest.mark.asyncio
async def test_live_fetch_accounts(credentials):
    connector = PlaidConnector(firm_id="live-firm", credentials=credentials)
    results = await connector.fetch_accounts()
    assert isinstance(results, list)
    print(f"Fetched {len(results)} accounts from plaid")