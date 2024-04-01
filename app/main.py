from datetime import datetime
from time import sleep


def main() -> None:
    try:
        while True:
            now = datetime.now()
            file_test = f"app-{now.hour}_{now.minute}_{now.second}.log"
            with open(file_test, "w") as f:
                f.write(str(now))
            print(f"{now} {file_test}")
            sleep(1)
    except KeyboardInterrupt:
        raise


if __name__ == "__main__":
    main()
