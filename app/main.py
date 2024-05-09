import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def create_file() -> None:
    now = datetime.now()
    formatted_time = now.strftime("app-%H_%M_%S.log")

    with open(formatted_time, "w") as f:
        f.write(str(now))

    print(f"{now} {formatted_time}")


def main() -> None:
    while True:
        create_file()
        time.sleep(1)


if __name__ == "__main__":
    main()
