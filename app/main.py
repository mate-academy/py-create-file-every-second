from time import sleep
from datetime import datetime


def main() -> None:

    while True:

        file_contents = datetime.now()
        file_name = (
            f"app-{datetime.now().hour}_{datetime.now().minute}"
            f"_{datetime.now().second}.log"
        )

        with open(file_name, "w") as f:
            f.write(f"{file_contents}")
            print(f"{file_contents} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
