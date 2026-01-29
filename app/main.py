import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        today = datetime.now()
        file_name = f"app-{today.hour}_{today.minute}_{today.second}.log"
        with open(file_name, "w") as file:
            file.write(str(today))
            print(f"{today} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
