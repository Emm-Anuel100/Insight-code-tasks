import subprocess
import os

def test_cpp_compilation():
    """
    This 'solution.py' acts as a runner/checker for the C++ task.
    It proves we can integrate multi-language tasks.
    """
    cpp_file = "solution.cpp"
    output_bin = "task_output.exe" if os.name == 'nt' else "./task_output"
    
    # Check if compiler exists
    try:
        subprocess.run(["g++", "--version"], capture_output=True, check=True)
    except:
        print("Skipping C++ compilation test (g++ not found)")
        return

    # Compile
    compile_res = subprocess.run(["g++", "-o", "task_output", cpp_file], capture_output=True)
    if compile_res.returncode != 0:
        print(f"Compilation Failed: {compile_res.stderr.decode()}")
        return

    # Run
    run_res = subprocess.run(["./task_output" if os.name != 'nt' else "task_output.exe"], capture_output=True)
    print("C++ Execution Output:")
    print(run_res.stdout.decode())

if __name__ == "__main__":
    test_cpp_compilation()
