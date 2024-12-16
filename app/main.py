from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        date = datetime.now()
        file_name = date.strftime("app-%H_%M_%S.log")

        with open(file_name, "w") as file:
            file.write(str(date))

        print(f"{date} {file_name}")

        time.sleep(1)


if __name__ == "__main__":
    main()
