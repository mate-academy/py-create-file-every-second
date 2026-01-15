from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:

    while True:
        current_time = datetime.now()
        file_name = current_time.strftime("app-%H_%M_%S.log")
        sleep(1)
        with open(file_name, "a") as f:
            f.write(f"{current_time}")

        print(f"{current_time} {file_name}")


if __name__ == "__main__":
    main()
