from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        log_content = get_log_content()

        write_log_file(log_content)
        print(f"{log_content[1]} {log_content[0]}")
        time.sleep(1)


def get_log_content() -> tuple:
    time_point = datetime.now()

    return (
        f"app-{time_point.hour}_{time_point.minute}_{time_point.second}.log",
        time_point.isoformat(" ")
    )


def write_log_file(log_content: tuple) -> None:
    with open(log_content[0], "w") as timelog:
        timelog.write(log_content[1])


if __name__ == "__main__":
    main()
