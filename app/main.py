from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        format_hms = current_time.strftime("%H_%M_%S")
        file_name = f"app-{format_hms}.log"
        with open(file_name, "w") as w:
            w.write(current_time.strftime("%Y-%m-%d %H:%M:%S"))
        with open(file_name, "r") as r:
            print(r.readline(), file_name)
        sleep(1)


if __name__ == "__main__":
    main()
