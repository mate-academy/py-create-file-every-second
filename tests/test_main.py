import os
import time
import datetime
from contextlib import redirect_stdout
from io import StringIO

import pytest
from pytest import MonkeyPatch

from app.main import main


class CleanUpFiles:
    def __init__(self, filenames: list):
        self.filenames = filenames

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        for filename in self.filenames:
            if os.path.exists(filename):
                os.remove(filename)


@pytest.mark.parametrize(
    "number_of_files,timestamps,filenames,content_of_the_files,outputs",
    [
        (
            1,
            [
                datetime.datetime(
                    year=2022, month=12, day=31, hour=23, minute=59, second=1
                ),
            ],
            [
                "app-23_59_01.log",
            ],
            [
                "2022-12-31 23:59:01",
            ],
            [
                "2022-12-31 23:59:01 app-23_59_01.log",
            ],
        ),
        (
            3,
            [
                datetime.datetime(
                    year=2022, month=12, day=31, hour=23, minute=59, second=1
                ),
                datetime.datetime(
                    year=2022, month=12, day=31, hour=23, minute=59, second=2
                ),
                datetime.datetime(
                    year=2022, month=12, day=31, hour=23, minute=59, second=3
                ),
            ],
            [
                "app-23_59_01.log",
                "app-23_59_02.log",
                "app-23_59_03.log",
            ],
            [
                "2022-12-31 23:59:01",
                "2022-12-31 23:59:02",
                "2022-12-31 23:59:03",
            ],
            [
                "2022-12-31 23:59:01 app-23_59_01.log",
                "2022-12-31 23:59:02 app-23_59_02.log",
                "2022-12-31 23:59:03 app-23_59_03.log",
            ],
        ),
    ],
)
def test_main(
    number_of_files: int,
    timestamps: list,
    filenames: list,
    content_of_the_files: list,
    outputs: list,
    monkeypatch: MonkeyPatch,
):
    start_time = time.time()

    class MockDatetime:
        @staticmethod
        def now():
            if time.time() - start_time > number_of_files - 0.5:
                raise KeyboardInterrupt
            return timestamps[int(time.time() - start_time)]

    monkeypatch.setattr(datetime, "datetime", MockDatetime)
    with CleanUpFiles(filenames):
        with pytest.raises(KeyboardInterrupt):
            f = StringIO()
            with redirect_stdout(f):
                main()
        assert f.getvalue().splitlines() == outputs
        for i in range(number_of_files):
            assert os.path.exists(filenames[i])
            with open(filenames[i], "r") as f:
                assert f.read() == content_of_the_files[i]