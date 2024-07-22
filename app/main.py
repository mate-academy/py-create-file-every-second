from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        file_name = (f"app-{datetime.now().hour}"
                     f"_{datetime.now().minute}"
                     f"_{datetime.now().second}.log")
        file_content = str(datetime.now())

        print(file_content, file_name)

        with open(file_name, "w") as f:
            f.write(file_content)

        sleep(1)


if __name__ == "__main__":
    main()
