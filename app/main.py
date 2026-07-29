from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        today = datetime.now()
        app_name = f"app-{today.hour}_{today.minute}_{today.second}.log"
        with open(app_name, "w") as f:
            f.write(f"{today}")
            print(f"{today} {app_name}")
            sleep(1)


if __name__ == "__main__":
    main()
