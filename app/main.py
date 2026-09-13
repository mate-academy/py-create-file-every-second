from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        with open(f"app-{datetime.now().hour}"
                  f"_{datetime.now().minute}"
                  f"_{datetime.now().second}.log", "w") as f:
            line = datetime.now().replace(microsecond=0)
            f.write(str(line))
            print(f"{line} app-{datetime.now().hour}"
                  f"_{datetime.now().minute}"
                  f"_{datetime.now().second}.log")

        time.sleep(1)


if __name__ == "__main__":
    main()
