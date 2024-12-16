from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def generate_filename() -> str:
    now = datetime.now()
    filename = now.strftime("app-%H_%M_%S.log")
    return filename


def generate_log_file() -> None:
    filename = generate_filename()
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    with open(filename, "w") as f:
        f.write(timestamp)

    print(f"{timestamp} {filename}")


def main() -> None:
    while True:
        generate_log_file()
        sleep(1)


if __name__ == "__main__":
    main()
