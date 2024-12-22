import pytest
from unittest.mock import patch
from app.main import create_file
import os


# Fixture to clean up files after the test
@pytest.fixture
def clean_up_files() -> None:
    """
    Fixture to clean up created files after the test.
    """
    yield
    for log_file in os.listdir():
        if log_file.startswith("app-") and log_file.endswith(".log"):
            os.remove(log_file)


def test_create_file(clean_up_files: None) -> None:
    """
    Tests file creation with a timestamp.
    """
    # Mock sleep to avoid waiting 1 second
    with patch("time.sleep", return_value=None):
        # Run the function
        create_file()

        # Check if the file with the correct name was created
        # Since the time changes, we'll search for the file by pattern
        for log_file in os.listdir():
            if log_file.startswith("app-") and log_file.endswith(".log"):
                with open(log_file, "r") as f:
                    timestamp = f.read()
                assert len(timestamp) > 0
                break
