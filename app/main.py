from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        _time = datetime.now()
        file_name = f"app-{_time.hour}_{_time.minute}_{_time.second}.log"
        _output = (f"{_time.year}-{_time.month}-{_time.day} "
                   f"{_time.hour}:{_time.minute}:{_time.second}")

        with (open(file_name, "w") as f):
            f.write(_output)

        print(_output, file_name)

        time.sleep(1)


if __name__ == "__main__":
    main()
