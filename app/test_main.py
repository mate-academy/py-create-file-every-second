import pytest
from unittest.mock import patch
from app.main import create_file
import os

@pytest.fixture
def clean_up_files():
    yield
    for file in os.listdir():
        if file.startswith("app-") and file.endswith(".log"):
            os.remove(file)

def test_create_file(clean_up_files):
    with patch("time.sleep", return_value=None):
        create_file()

        for file in os.listdir():
            if file.startswith("app-") and file.endswith(".log"):
                with open(file, "r") as f:
                    timestamp = f.read()
                assert len(timestamp) > 0
                break
