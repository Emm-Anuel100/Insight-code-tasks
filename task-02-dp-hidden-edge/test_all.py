import pytest
from solution import solve_vault

def test_basic_vault():
    items = [(10, 5), (15, 10), (20, 15)]
    # Case where penalty makes taking more items worse
    assert solve_vault(items, 30, 20, 10) == 25 # (10+15) is better than (45 - 30)

def test_penalty_worth_it():
    items = [(10, 5), (15, 10), (100, 15)]
    # 100 is so big that even with penalty it's worth it
    # (10+15+100) - 3*5 = 125 - 15 = 110
    assert solve_vault(items, 30, 20, 5) == 110

def test_empty_items():
    assert solve_vault([], 100, 50, 10) == 0

def test_zero_capacity():
    assert solve_vault([(10, 5)], 0, 20, 5) == 0

def test_threshold_at_max():
    items = [(10, 5), (20, 5)]
    # Threshold is 10, max is 10. If we take both, weight is 10. 
    # Penalty only applies if weight > threshold.
    assert solve_vault(items, 10, 10, 100) == 30
