from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current = datetime.now()
        with open(
                f"app-{current.hour}_{current.minute}_{current.second}.log",
                "w"
        ) as work_file:
            result = current.strftime("%Y-%m-%d %H:%M:%S")
            work_file.write(result)
            print(f"{result} {work_file.name}")
        sleep(1)


if __name__ == "__main__":
    main()
