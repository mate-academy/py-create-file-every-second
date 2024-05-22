from datetime import datetime
import time


def main() -> None:
    while True:
        now = datetime.now()
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"

        with open(file_name, "w") as file:
            file.write(now.strftime("%Y-%m-%d %H:%M:%S.%f"))
        print(f'{now.strftime("%Y-%m-%d %H:%M:%S.%f")} {file_name}')
        time.sleep(1)


main()
