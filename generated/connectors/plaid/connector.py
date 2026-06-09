# =============================================================================
# AUTO-GENERATED — DO NOT EDIT MANUALLY
# Partner : plaid
# Auth    : ApiKeyHeaderStrategy
# Paging  : OffsetPagination
# =============================================================================
from __future__ import annotations

from typing import Any, AsyncIterator, Dict, List

from lolo.integrations_core import (
    BaseConnector,
    ApiKeyHeaderStrategy,
    OffsetPagination,
    BudgetAwareScheduler,
    SyncResult,
    SyncStatus,
)


class PlaidConnector(BaseConnector):
    """
    Generated connector for plaid.
    Base URL : https://raw.githubusercontent.com/plaid/plaid-openapi/refs/heads/master/2020-09-14.yml
    Entities : transactions, accounts, positions, contacts
    """

    BASE_URL = "https://raw.githubusercontent.com/plaid/plaid-openapi/refs/heads/master/2020-09-14.yml"

    def __init__(self, firm_id: str, credentials: Dict[str, Any]) -> None:
        auth = ApiKeyHeaderStrategy(**credentials)
        pagination = OffsetPagination()
        scheduler = BudgetAwareScheduler()
        super().__init__(
            base_url=self.BASE_URL,
            auth_strategy=auth,
            pagination_strategy=pagination,
            rate_limiter=scheduler,
            firm_id=firm_id,
        )

    async def fetch_transactions(self) -> List[Dict[str, Any]]:
        """Fetch all transactions records with automatic pagination."""
        await self._check_rate_limit()
        records: List[Dict[str, Any]] = []
        params = self.pagination_strategy.get_initial_params()

        while True:
            response = await self.http.get("/transactions", params=params)
            page = response.get("data", response.get("transactions", response.get("results", [])))
            if isinstance(page, list):
                records.extend(page)
            else:
                records.append(page)

            await self._consume_rate_limit()
            if not self.pagination_strategy.has_more(response):
                break
            params = self.pagination_strategy.get_next_params(response)

        return records

    async def fetch_accounts(self) -> List[Dict[str, Any]]:
        """Fetch all accounts records with automatic pagination."""
        await self._check_rate_limit()
        records: List[Dict[str, Any]] = []
        params = self.pagination_strategy.get_initial_params()

        while True:
            response = await self.http.get("/accounts", params=params)
            page = response.get("data", response.get("accounts", response.get("results", [])))
            if isinstance(page, list):
                records.extend(page)
            else:
                records.append(page)

            await self._consume_rate_limit()
            if not self.pagination_strategy.has_more(response):
                break
            params = self.pagination_strategy.get_next_params(response)

        return records

    async def fetch_positions(self) -> List[Dict[str, Any]]:
        """Fetch all positions records with automatic pagination."""
        await self._check_rate_limit()
        records: List[Dict[str, Any]] = []
        params = self.pagination_strategy.get_initial_params()

        while True:
            response = await self.http.get("/positions", params=params)
            page = response.get("data", response.get("positions", response.get("results", [])))
            if isinstance(page, list):
                records.extend(page)
            else:
                records.append(page)

            await self._consume_rate_limit()
            if not self.pagination_strategy.has_more(response):
                break
            params = self.pagination_strategy.get_next_params(response)

        return records

    async def fetch_contacts(self) -> List[Dict[str, Any]]:
        """Fetch all contacts records with automatic pagination."""
        await self._check_rate_limit()
        records: List[Dict[str, Any]] = []
        params = self.pagination_strategy.get_initial_params()

        while True:
            response = await self.http.get("/contacts", params=params)
            page = response.get("data", response.get("contacts", response.get("results", [])))
            if isinstance(page, list):
                records.extend(page)
            else:
                records.append(page)

            await self._consume_rate_limit()
            if not self.pagination_strategy.has_more(response):
                break
            params = self.pagination_strategy.get_next_params(response)

        return records

    async def fetch_accounts(self) -> List[Dict[str, Any]]:  # type: ignore[override]
        """Required by BaseConnector abstract interface."""
        return await self._fetch_accounts_impl()
