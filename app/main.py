import time
from datetime import datetime


def main() -> None:
    try:
        while True:
            now = datetime.now()
            file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
            cur_time = now.strftime("%H:%M:%S")
            with open(file_name, "w") as f:
                f.write(f'{now.strftime("%Y-%m-%d")} {cur_time}')
                print(f'{now.strftime("%Y-%m-%d")} {cur_time} {file_name}')
            time.sleep(1)
    except KeyboardInterrupt:
        raise


if __name__ == "__main__":
    main()
