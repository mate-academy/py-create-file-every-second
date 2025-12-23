from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:

    while True:
        current_time = datetime.now()
        name = current_time.strftime("app-%H_%M_%S.log")
        with open(name, "w") as f:
            formatted_timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
            f.write(formatted_timestamp)
            print(formatted_timestamp + " " + name)
            sleep(1)


if __name__ == "__main__":
    main()
