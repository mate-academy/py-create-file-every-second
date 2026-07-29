import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        time_now = str(datetime.now())
        file_name = (f"app-{time_now[11:13]}"
                     f"_{time_now[14:16]}"
                     f"_{time_now[17:19]}.log")
        with open(file_name, "w") as file:
            file.write(time_now)
        print(time_now, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
