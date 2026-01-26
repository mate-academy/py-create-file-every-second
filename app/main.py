from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        timestamp = datetime.now().strftime("%H_%M_%S")
        content = str(datetime.now().replace(microsecond=0))
        filename = f"app-{timestamp}.log"

        with open(filename, "w") as file:
            file.write(content)

        print(content, filename)
        sleep(1)


if __name__ == "__main__":
    main()
