import sys
import subprocess
import json


def format_linter_error(error: dict) -> dict:
    """Formats a single linter error into a structured dictionary."""
    return {
        "code": error.get("code"),
        "description": error.get("text"),
        "location": {
            "line": error.get("line_number"),
            "column": error.get("column_number"),
        },
    }


def format_linter_report(linter_report: dict) -> list:
    """Formats a linter report dictionary into a structured list.

    Args:
        linter_report (dict): Dictionary with file paths as keys and error
            lists as values.

    Returns:
        list: A list of formatted dictionaries with path, status, and
            detailed errors.
    """
    formatted_report = []
    for file_path, errors in linter_report.items():
        status = "failed" if errors else "passed"

        formatted_errors = []
        for error in errors:
            formatted_error = {
                "line": error.get("line_number"),
                "column": error.get("column_number"),
                "message": error.get("text"),
                "name": error.get("code"),
                "source": "flake8",
            }
            formatted_errors.append(formatted_error)

        formatted_report.append(
            {
                "path": file_path,
                "status": status,
                "errors": formatted_errors,
            }
        )
    return formatted_report


def run_flake8(path):
    """Runs flake8 and returns a report.

    Returns an empty dictionary if flake8 fails (but logs the error).
    """
    try:
        result = subprocess.run(
            ["flake8", "--format=json", path],
            capture_output=True,
            text=True,
            check=False,  # Changed to False
        )
        if result.returncode != 0:
            print(f"Flake8 found errors in {path}:")
            print(result.stderr)  # Print flake8's output
        if result.stdout:
            try:
                report = json.loads(result.stdout)
            except json.JSONDecodeError:
                print(f"JSONDecodeError: {result.stdout}")
                return {}
        else:
            report = {}
        return report
    except FileNotFoundError:
        print(f"Error: flake8 not found. Is it installed?")
        return {}


if __name__ == "__main__":
    # 1. Run Flake8
    flake8_report = {}
    flake8_report["./app/main.py"] = run_flake8("./app/main.py")
    flake8_report["./linter_script.py"] = run_flake8("./linter_script.py")

    # 2. Format Flake8 Report
    formatted_report = format_linter_report(flake8_report)

    # 3. Check for Linting Failures
    linting_failed = any(file["status"] == "failed" for file in formatted_report)

    # 4. Run Pytest
    pytest_result = subprocess.run(["pytest"], capture_output=True, text=True)
    pytest_failed = pytest_result.returncode != 0

    # 5. Determine Final Exit Code
    if linting_failed or pytest_failed:
        print("Linting and/or tests failed. Exiting with code 1.")
        if linting_failed:
            print("Linting Errors")
        if pytest_failed:
            print("Pytest Errors")
        sys.exit(1)
    else:
        print("Linting and tests passed. Exiting with code 0.")
        sys.exit(0)
