from datetime import datetime
from time import sleep


def create_file() -> None:
    current_time = datetime.now()
    file_name = (f"app-{current_time.hour:02d}_"  # noqa
                 f"{current_time.minute:02d}_"  # noqa
                 f"{current_time.second:02d}.log")  # noqa
    file_content = current_time.strftime(
        "%Y-%m-%d %H:%M:%S.%f"
    )[:-7].rstrip("0")

    with open(file_name, "a") as f:
        f.write(file_content)

    print(f"{current_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-7]} {file_name}")


def main() -> None:
    try:
        while True:
            create_file()
            sleep(1)
    except KeyboardInterrupt:
        raise


if __name__ == "__main__":
    main()
