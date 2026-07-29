from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date = datetime.now()
        filename = f"app-{date.strftime('%H_%M_%S')}.log"

        with open(filename, "w") as file:
            file.write(str(date))
        print(f"{date} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
