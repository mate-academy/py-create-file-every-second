from datetime import datetime
from time import sleep


def main():
    while True:
        now = datetime.now()
        now_file_name = f"app-{datetime.now().strftime('%H_%M_%S')}.log"

        with open(now_file_name, "w") as f:
            f.write(str(now))
        with open(now_file_name, "r") as f:
            print(f"{f.read()} {now_file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
