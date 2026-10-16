from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        times_str = now.strftime("%Y-%m-%d %H:%M:%S")
        file_names = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(file_names, "w") as f:
            f.write(times_str)
        print(times_str, file_names)
        sleep(1)


if __name__ == "__main__":
    main()
