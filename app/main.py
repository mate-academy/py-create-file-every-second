import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        time_now = datetime.now().time()
        file_name = (
            f"app-{time_now.hour}_"
            f"{time_now.minute}_"
            f"{time_now.second}.log"
        )
        with open(file_name, "w") as file:
            file.write(str(datetime.now()))
        print(f"{datetime.now()} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
