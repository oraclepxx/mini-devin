import subprocess
import sys

def run_tests():

    result = subprocess.run(
        [sys.executable, "-m", "pytest"],
        cwd="workspace",
        capture_output=True,
        text=True
    )

    return {
        "success": result.returncode == 0,
        "output": result.stdout + result.stderr
    }