from time import sleep
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    try:
        while True:
            now = str(datetime.now())[:19]
            hours = int(now[11:13])
            minutes = int(now[14:16])
            seconds = int(now[17:19])

            with open(f"app-{hours}_{minutes}_{seconds}.log", "w") as file:
                file.write(f"{now}")
                print(f"{now} app-{hours}_{minutes}_{seconds}.log")
            sleep(1)
    except KeyboardInterrupt:
        raise KeyboardInterrupt


if __name__ == "__main__":
    main()
