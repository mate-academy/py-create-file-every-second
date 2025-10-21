import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        curr_time = datetime.now()
        filename = f'app-{curr_time.strftime("%H_%M_%S")}.log'
        log_time = curr_time.strftime("%Y-%m-%d %H:%M:%S")
        write_log(filename, log_time)
        time.sleep(1)


def write_log(filename: str, log_time: str) -> None:
    with open(filename, "a") as f:
        f.write(log_time)
    f.close()
    print(log_time, filename)


if __name__ == "__main__":
    main()
