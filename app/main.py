from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main():
    while True:
        now = datetime.now()
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(file_name, "x") as file:
            file.write(f"{str(now)}")
        print(f"{now} {file_name}")
        time.sleep(1)  # import time


if __name__ == "__main__":
    main()
