from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:

    while True:
        with open(
                f"app-{datetime.now().strftime('%H')}_"
                f"{datetime.now().strftime('%M')}_"
                f"{datetime.now().strftime('%S')}.log", "w"
        ) as file:
            file.write(f"{datetime.now()}")

        print(datetime.now(), file.name)

        sleep(1)


if __name__ == "__main__":
    main()
