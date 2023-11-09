from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        file_name = (
            f"app-{datetime.now().hour}"
            f"_{datetime.now().minute}_{datetime.now().second}.log"
        )
        with open(file_name, "w") as f:
            now = datetime.now()
            print(now, file_name)
            f.write(str(now))
            time.sleep(1)


if __name__ == "__main__":
    main()
