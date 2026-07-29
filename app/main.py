from datetime import datetime
import time


def main() -> None:
    while True:
        now = datetime.now()
        str_now = now.strftime("%Y-%m-%d %H:%M:%S")
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(file_name, "w") as f:
            f.write(str_now)
        print(str_now, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
