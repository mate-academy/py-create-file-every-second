from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        time = str(datetime.now())
        file_name = f"app-{time[11:13]}_{time[14:16]}_{time[17:19]}.log"
        with open(file_name, "x") as f:
            f.write(f"{time}")
        print(time, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
