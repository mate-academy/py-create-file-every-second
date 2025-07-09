from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        now = now.replace(microsecond=0)
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(file_name, "w+") as f:
            f.write(f"{now}")
            f.seek(0)
            print(f.read(), file_name)
            sleep(1)


if __name__ == "__main__":
    main()
