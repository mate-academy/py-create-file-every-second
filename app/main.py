from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        hours, minutes, seconds = (
            datetime.now().hour,
            datetime.now().minute,
            datetime.now().second,
        )
        filename = f"app-{hours}_{minutes}_{seconds}.log"

        with open(filename, "w") as file:
            now = datetime.now()
            file.write(f"{now}")

        print(f"{now} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
