import os
import time
from datetime import datetime


def main() -> None:
    while True:
        today = datetime.now()
        today_strf = today.strftime("%Y-%m-%d %H:%M:%S")
        file_name = f"app-{today.hour}_{today.minute}_{today.second}.log"
        file_path = os.path.join(os.getcwd(), file_name)

        with open(file_path, "w") as f:
            f.write(today_strf)

        print(f"{today_strf} {file_name}")

        time.sleep(1)


if __name__ == "__main__":
    main()
