from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        full_time = datetime.now()
        hour = full_time.hour
        minute, second = full_time.minute, full_time.second
        file_name = f"app-{hour}_{minute}_{second}.log"
        with open(f"{file_name}", "w") as file:
            file.write(str(full_time))
        print(full_time, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
