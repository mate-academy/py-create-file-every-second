from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date_time = datetime.now()
        text_name = (f"app-{date_time.hour}"
                     f"_{date_time.minute}"
                     f"_{date_time.second}"
                     f".log")
        with open(text_name, "a") as document:
            document.write(str(date_time))
            print(date_time, text_name)
        sleep(1)


if __name__ == "__main__":
    main()
