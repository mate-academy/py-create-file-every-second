from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(filename, "w") as f:
            f.write(formatted_now)
        print(f"{formatted_now} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
