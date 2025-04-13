def format_linter_error(error: dict) -> dict:
    """
    Formats a linter error into a dictionary with specific keys.

    Args:
        error (dict): Dictionary containing error details.

    Returns:
        dict: Formatted dictionary with keys `code`, `description`, and `location`.
    """
    return {
        "code": error.get("code"),
        "description": error.get("text"),
        "location": {
            "line": error.get("line_number"),
            "column": error.get("column_number"),
        },
    }


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
