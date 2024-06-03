from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        dt_now = datetime.now()
        file_name = f"app-{dt_now.hour}_{dt_now.minute}_{dt_now.second}.log"
        file_write = f"{dt_now.strftime("%Y-%m-%d %H:%M:%S")}"
        with open(file_name, "w") as f:
            f.write(file_write)
        print(file_write, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
