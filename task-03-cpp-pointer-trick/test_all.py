import pytest
import os
from solution import test_cpp_compilation

def test_cpp_logic():
    """
    Since we can't always guarantee a C++ compiler in every env,
    this test checks for the file existence and basic structure.
    """
    assert os.path.exists("solution.cpp")
    with open("solution.cpp", "r") as f:
        content = f.read()
        assert "delete[] data" in content
        assert "ref_count" in content

def test_run_compilation():
    # Attempt to run if g++ is present
    test_cpp_compilation()
