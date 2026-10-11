import time
from datetime import datetime


def main() -> str:
    while True:
        now = datetime.now()
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"
        print_time = now.strftime("%Y-%m-%d %H:%M:%S")
        with open(f"{filename}", "w") as file:
            file.write(f"{now}")
        print(f"{print_time} {filename}")
        time.sleep(1)


if __name__ == "__main__":
    main()
