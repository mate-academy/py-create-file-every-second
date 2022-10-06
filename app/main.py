import time
from datetime import datetime


def main():
    while True:
        time_now = datetime.now()
        name_file = f"app-{time_now.strftime('%H_%M_%S')}.log"

        with open(name_file, "w") as f:
            f.write(f"{time_now}")

        print(time_now, name_file)
        time.sleep(1)


if __name__ == "__main__":
    main()
