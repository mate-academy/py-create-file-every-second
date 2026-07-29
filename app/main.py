from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        get_time = datetime.now()
        hour = get_time.hour
        minute = get_time.minute
        second = get_time.second
        file_name = f"app-{hour}_{minute}_{second}.log"
        with open(file_name, "w") as outfile:
            outfile.write(str(datetime.now()))
            print(f"{datetime.now()} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
