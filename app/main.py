from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    try:
        while True:
            timestamp = datetime.now()
            file_name = (f"app-{datetime.now().hour}"
                         f"_{datetime.now().minute}"
                         f"_{datetime.now().second}.log")

            with open(file_name, "w") as file:
                file.write(str(timestamp))

            print(f"{timestamp} {file_name}")

            sleep(1)
    except KeyboardInterrupt as e:
        raise e


if __name__ == "__main__":
    main()
