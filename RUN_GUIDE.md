# Run Guide: Insight Code Tasks

These tasks are designed to verify algorithmic and concurrency logic.

## Setup
Ensure `pytest` is installed:
```bash
pip install pytest
```

## How to Run

### Task 1: Concurrency (Ledger)
```bash
cd task-01-concurrency-race
pytest test_all.py
```

### Task 2: Dynamic Programming (Vault)
```bash
cd task-02-dp-hidden-edge
pytest test_all.py
```

### Task 3: C++ Pointer Trick
Requires `g++` for the full compilation test.
```bash
cd task-03-cpp-pointer-trick
# This script handles compilation and basic execution
python solution.py
# This runs the logic structure tests
pytest test_all.py
```
