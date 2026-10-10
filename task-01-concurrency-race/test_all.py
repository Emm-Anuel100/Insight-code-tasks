import pytest
import threading
from concurrent.futures import ThreadPoolExecutor
from solution import Ledger

def test_basic_transfer():
    ledger = Ledger()
    ledger.create_account("A", 100)
    ledger.create_account("B", 50)
    assert ledger.transfer("A", "B", 30) is True
    assert ledger.get_balance("A") == 70
    assert ledger.get_balance("B") == 80

def test_insufficient_funds():
    ledger = Ledger()
    ledger.create_account("A", 10)
    ledger.create_account("B", 50)
    assert ledger.transfer("A", "B", 20) is False
    assert ledger.get_balance("A") == 10

def test_concurrent_transfers_no_deadlock():
    """
    Stress test for deadlocks. 
    Many threads transferring back and forth between A and B.
    """
    ledger = Ledger()
    ledger.create_account("A", 1000)
    ledger.create_account("B", 1000)

    def task_a_to_b():
        for _ in range(100):
            ledger.transfer("A", "B", 1)

    def task_b_to_a():
        for _ in range(100):
            ledger.transfer("B", "A", 1)

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = []
        for _ in range(10):
            futures.append(executor.submit(task_a_to_b))
            futures.append(executor.submit(task_b_to_a))
        
        for f in futures:
            f.result()

    # Total balance should remain 2000
    assert ledger.get_balance("A") + ledger.get_balance("B") == 2000

def test_invalid_account():
    ledger = Ledger()
    ledger.create_account("A", 100)
    assert ledger.transfer("A", "C", 10) is False

def test_negative_amount():
    ledger = Ledger()
    ledger.create_account("A", 100)
    ledger.create_account("B", 100)
    assert ledger.transfer("A", "B", -50) is False
