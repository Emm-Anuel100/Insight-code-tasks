# Problem: The Multi-Threaded Ledger

## Context
You are building a high-frequency ledger system. Multiple threads will be transferring funds between various accounts simultaneously.

## Task
Implement a `Ledger` class that supports:
1. `create_account(account_id: str, initial_balance: float)`
2. `transfer(from_id: str, to_id: str, amount: float) -> bool`
3. `get_balance(account_id: str) -> float`

## Constraints
- Transfers must be **atomic**. If a transfer starts, it must either complete fully or not change any balances if it fails.
- The system must be **thread-safe**. Multiple threads will call `transfer` and `get_balance` at the same time.
- **Performance:** Do not use a single global lock for the entire ledger. This will bottleneck the system. Use fine-grained locking.
- **Deadlock Prevention:** Ensure that concurrent transfers between the same two accounts (e.g., A -> B and B -> A) do not cause a deadlock.
- `amount` must be positive.
- `transfer` should return `False` if the source account has insufficient funds.

## Input/Output Example
```python
ledger = Ledger()
ledger.create_account("A", 100)
ledger.create_account("B", 50)
ledger.transfer("A", "B", 30) # Returns True
ledger.get_balance("A") # Returns 70
```
