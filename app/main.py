from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        c_time = datetime.now()
        file_name = f"app-{c_time.hour}_{c_time.minute}_{c_time.second}.log"
        print(f"{c_time} {file_name}")
        with open(file_name, "w") as f:
            f.write(f"{c_time.year}-{c_time.month}-{c_time.day}"
                    f" {c_time.hour}:{c_time.minute}:{c_time.second}")
        sleep(1)


if __name__ == "__main__":
    main()
