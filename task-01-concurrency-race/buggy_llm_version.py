import threading
from typing import Dict

class Ledger:
    """
    A common 'buggy' version an LLM might produce.
    It uses fine-grained locking but forgets the sorted order, leading to deadlocks.
    Or it might forget to lock for get_balance.
    """

    def __init__(self) -> None:
        self.accounts: Dict[str, float] = {}
        self.locks: Dict[str, threading.Lock] = {}

    def create_account(self, account_id: str, initial_balance: float) -> None:
        self.accounts[account_id] = initial_balance
        self.locks[account_id] = threading.Lock()

    def get_balance(self, account_id: str) -> float:
        # LLMs often skip locking for simple reads, which is a race condition
        return self.accounts.get(account_id, 0.0)

    def transfer(self, from_id: str, to_id: str, amount: float) -> bool:
        """
        BUGGY: This will deadlock if Thread 1 does A -> B 
        and Thread 2 does B -> A at the same time.
        """
        lock_from = self.locks.get(from_id)
        lock_to = self.locks.get(to_id)

        if not lock_from or not lock_to:
            return False

        # LLM logic: 'Just lock both' - but order matters!
        with lock_from:
            with lock_to:
                if self.accounts[from_id] >= amount:
                    self.accounts[from_id] -= amount
                    self.accounts[to_id] += amount
                    return True
                return False
