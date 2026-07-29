from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_dt = datetime.now()
        filename = (f"app-{current_dt.hour}_"
                    f"{current_dt.minute}_{current_dt.second}.log")
        with open(filename, "w") as file:
            file.write(f"{current_dt}")
        print(f"{current_dt} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
