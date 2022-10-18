from datetime import datetime
import time


def main() -> None:
    while True:
        hours = str(datetime.now().time())[0:2]
        minutes = str(datetime.now().time())[3:5]
        seconds = str(datetime.now().time())[6:8]
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        with open(f"{file_name}", "w") as file:
            file.write(f"{datetime.now()}")
            print(f"{datetime.now()} {file_name}")

        time.sleep(1)


if __name__ == "__main__":
    main()
