from typing import Protocol


class TransactionManagerSync(Protocol):
    def commit(self) -> None: ...


class TransactionManagerAsync(Protocol):
    async def commit(self) -> None: ...
