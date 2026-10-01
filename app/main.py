from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> str:

    while True:

        now = datetime.now().replace(microsecond=0)

        hour = now.hour
        minute = now.minute
        second = now.second

        with open(f"app-{hour}_{minute}_{second}.log",
                  "a", encoding="utf-8") as f:
            f.write(f"{now}")
            print(f"{now} {f.name}")
            sleep(1)


if __name__ == "__main__":
    main()
