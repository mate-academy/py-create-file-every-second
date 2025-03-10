from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        today = datetime.now()
        file_name = f"app-{today.hour}_{today.minute}_{today.second}.log"
        file_contain = (f"{today.year}-{today.month}-{today.day} "
                        f"{today.hour}:{today.minute}:{today.second}")

        with open(file_name, "w") as f:
            f.write(file_contain)
            print(f"{file_contain} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
