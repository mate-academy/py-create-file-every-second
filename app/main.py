from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        with open(f"app-{datetime.now().hour}"
                  f"_{datetime.now().minute}"
                  f"_{datetime.now().second}.log", "a+") as f:
            now = datetime.now().replace(microsecond=0)
            f.write(f"{now}")
            f.seek(0)
            print(f"{now} {f.name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
