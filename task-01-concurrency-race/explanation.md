# Why LLMs Fail: The Multi-Threaded Ledger

## The Trap
This task looks simple on the surface, which is exactly why LLMs fail it. They usually identify that "locking is needed," but they fail at the **implementation details of distributed locking**.

## Common LLM Failures
1. **The Deadlock Trap:** Most LLMs will write code that locks `from_account` and then `to_account`. If two threads try to send money to each other simultaneously (A->B and B->A), they will each grab one lock and wait forever for the other. 
   - *Fix:* My solution uses **Lock Ordering** (sorting IDs) to ensure all threads acquire locks in the same sequence.

2. **The Atomic Visibility Gap:** LLMs often forget to lock the `get_balance` method. They assume reading a float is "safe." However, in a multi-step transfer, a thread could read a balance *after* the deduction but *before* the addition, leading to "ghost money" in reports.

3. **Global Lock Over-simplification:** If you tell an LLM to be "safe," it might just put a `with self.lock:` around every method. This works but fails the performance constraint, essentially turning a multi-threaded system into a single-threaded one.

## Verifiable Proof
The `test_concurrent_transfers_no_deadlock` test in `test_all.py` specifically triggers the circular dependency that kills buggy LLM code.
