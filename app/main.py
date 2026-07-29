from datetime import datetime
import time


def main() -> None:
    while True:
        moment = datetime.now()

        with open(
                f"app-{moment.hour}_{moment.minute}_{moment.second}.log", "w"
        ) as file:

            file.write(f"{moment}")
            print(f"{moment} {file.name}")
            time.sleep(1)


if __name__ == "__main__":
    main()
