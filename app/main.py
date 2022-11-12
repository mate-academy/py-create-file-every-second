from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        dt = datetime.now()
        sleep(1)
        file_name = f"app-{dt.hour}_{dt.minute}_{dt.second}.log"
        with open(file_name, "w") as f:
            f.write(f"{dt}")
        print(f"{dt} {file_name}")


if __name__ == "__main__":
    main()
