import threading
from typing import Dict

class Ledger:
    """
    A thread-safe ledger with fine-grained locking to prevent deadlocks.
    We use a dictionary of locks, one for each account, and always acquire
    them in a consistent global order (sorted by account ID).
    """

    def __init__(self) -> None:
        self.accounts: Dict[str, float] = {}
        self.locks: Dict[str, threading.Lock] = {}
        self.master_lock = threading.Lock()

    def create_account(self, account_id: str, initial_balance: float) -> None:
        """Initializes an account with a balance and its own lock."""
        with self.master_lock:
            if account_id not in self.accounts:
                self.accounts[account_id] = initial_balance
                self.locks[account_id] = threading.Lock()

    def get_balance(self, account_id: str) -> float:
        """Returns the current balance of an account."""
        # We need the lock even for reading to ensure we don't read 
        # a balance in the middle of a transfer.
        lock = self.locks.get(account_id)
        if not lock:
            raise ValueError("Account does not exist")
        
        with lock:
            return self.accounts[account_id]

    def transfer(self, from_id: str, to_id: str, amount: float) -> bool:
        """
        Transfers money between two accounts atomically.
        Uses sorted lock acquisition to prevent deadlocks.
        """
        if amount <= 0:
            return False
        
        if from_id == to_id:
            return True

        # Sort IDs to ensure consistent locking order across all threads
        first_id, second_id = sorted([from_id, to_id])
        
        lock1 = self.locks.get(first_id)
        lock2 = self.locks.get(second_id)

        if not lock1 or not lock2:
            return False

        with lock1:
            with lock2:
                if self.accounts[from_id] < amount:
                    return False
                
                self.accounts[from_id] -= amount
                self.accounts[to_id] += amount
                return True
