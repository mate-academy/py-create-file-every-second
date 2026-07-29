from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        dt_now = datetime.now()
        file_name = f"app-{dt_now.hour}_{dt_now.minute}_{dt_now.second}.log"
        with open(file_name, "w") as file:
            file.write(str(dt_now))
            print(dt_now, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
