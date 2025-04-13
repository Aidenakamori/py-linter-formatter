import sys


def format_linter_error(error: dict) -> dict:
    """
    Formats a single linter error into a structured dictionary.

    Args:
        error (dict): A dictionary containing the raw error information.

    Returns:
        dict: A dictionary with structured error details.
    """
    return {
        "code": error.get("code"),
        "description": error.get("text"),
        "location": {
            "line": error.get("line_number"),
            "column": error.get("column_number"),
        },
    }


def format_linter_report(linter_report: dict) -> list:
    """
    Formats a linter report dictionary into a structured list.

    Args:
        linter_report (dict): Dictionary with file paths as keys and error lists
                              as values.

    Returns:
        list: A list of formatted dictionaries with path, status, and detailed
              errors.
    """
    formatted_report = []
    for file_path, errors in linter_report.items():
        if errors:
            status = "failed"
        else:
            status = "passed"

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


# Example linter report input
report_file = {
    "./test_source_code_2.py": [],
    "./source_code_2.py": [
        {
            "code": "E501",
            "filename": "./source_code_2.py",
            "line_number": 18,
            "column_number": 80,
            "text": "line too long (99 > 79 characters)",
            "physical_line": '    return f"I like to filter, rounding, doubling, '
            "store and decorate numbers: {', '.join(items)}!\"",
        },
        {
            "code": "W292",
            "filename": "./source_code_2.py",
            "line_number": 18,
            "column_number": 100,
            "text": "no newline at end of file",
            "physical_line": '    return f"I like to filter, rounding, doubling, '
            "store and decorate numbers: {', '.join(items)}!\"",
        },
    ],
}

# Process the linter report
formatted_report = format_linter_report(report_file)

# Check if there are failures and exit with the appropriate code
if any(file["status"] == "failed" for file in formatted_report):
    print("Linting errors found. Exiting with code 1.")
    sys.exit(1)
else:
    print("No linting errors. Exiting with code 0.")
    sys.exit(0)
