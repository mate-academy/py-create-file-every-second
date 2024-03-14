from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        filename = (
            f"app-{datetime.now().hour}"
            f"_{datetime.now().minute}"
            f"_{datetime.now().second}.log"
        )
        content = datetime.now()

        with open(filename, "w") as timestamp_file:
            timestamp_file.write(str(content))

        print(content, filename)
        sleep(1)


if __name__ == "__main__":
    main()
