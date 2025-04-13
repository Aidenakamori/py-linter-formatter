# app/main.py
def process_data(data: list[int | float]) -> str:
    """Processes some data.

    Returns a success message or raises ValueError if there's an error.
    """
    if not isinstance(data, list):
        raise ValueError("Data must be a list")

    if not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("Data must contain only numbers")

    if not data:
        raise ValueError("Data list cannot be empty")

    total = sum(data)
    average = total / len(data)

    return f"Processed data: Total={total}, Average={average}"


def greet(name: str) -> str:
    """Greets the person passed in as a parameter"""
    return f"Hello, {name}"


def log_message(message: str) -> None:
    """Logs a message."""
    print(f"Logging: {message}")  # Fixed: Added two spaces before comment


def file_process(path: str) -> None:
    """Processes the file under the given path"""
    print("Processing path")  # Fixed: Added two spaces before comment


if __name__ == "__main__":
    import sys

    try:
        # Simulate reading data from command line arguments
        if len(sys.argv) > 1:
            data_strings = sys.argv[1:]
            data = [float(x) for x in data_strings]
        else:
            # Provide default data
            data = [1.0, 2.0, 3.0]  # Default data if no arguments are provided

        result = process_data(data)
        print(result)
        sys.exit(0)  # Success
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)  # Failure
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)
