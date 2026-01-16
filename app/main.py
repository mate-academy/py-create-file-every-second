import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        c_time = datetime.now()
        file_name = f"app-{c_time.hour}_{c_time.minute}_{c_time.second}.log"
        print(f"{c_time} {file_name}")
        with open(file_name, "w") as f:
            f.write(c_time.strftime("%Y-%m-%d %H:%M:%S"))
        time.sleep(1)


if __name__ == "__main__":
    main()
