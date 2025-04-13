import sys

def format_linter_report(linter_report: dict) -> list:
    # Your existing formatting logic
    formatted_report = [
        {
            "path": file_path,
            "status": "failed" if errors else "passed",
            "errors": [
                {
                    "line": error.get("line_number"),
                    "column": error.get("column_number"),
                    "message": error.get("text"),
                    "name": error.get("code"),
                    "source": "flake8",
                }
                for error in errors
            ],
        }
        for file_path, errors in linter_report.items()
    ]
    return formatted_report

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
    ],
}
formatted_report = format_linter_report(report_file)

# Check if there are any failures and exit appropriately
if any(file["status"] == "failed" for file in formatted_report):
    print("Linting errors found.")
    sys.exit(1)
else:
    print("No linting errors.")
    sys.exit(0)


def format_single_linter_file(file_path: str, errors: list) -> dict:
    """
    Formats linter errors for a specific file into a structured dictionary.

    Args:
        file_path (str): The path to the file where errors were found.
        errors (list): A list of error dictionaries.

    Returns:
        dict: Formatted dictionary with file path, status, and error details.
    """
    return {
        "errors": [
            {
                "line": error.get("line_number"),
                "column": error.get("column_number"),
                "message": error.get("text"),
                "name": error.get("code"),
                "source": "flake8",  # Presuming the linter source is flake8
            }
            for error in errors
        ],
        "path": file_path,
        "status": "failed" if errors else "passed",  # Status logic
    }


def format_linter_report(linter_report: dict) -> list:
    """
    Formats a linter report dictionary into a structured list.

    Args:
        linter_report (dict): Dictionary with file paths as keys and error lists as values.

    Returns:
        list: A list of formatted dictionaries with path, status, and detailed errors.
    """
    return [
        {
            "path": file_path,
            "status": "failed" if errors else "passed",
            "errors": [
                {
                    "line": error.get("line_number"),
                    "column": error.get("column_number"),
                    "message": error.get("text"),
                    "name": error.get("code"),
                    "source": "flake8",
                }
                for error in errors
            ],
        }
        for file_path, errors in linter_report.items()
    ]
