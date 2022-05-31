from datetime import datetime
from time import sleep


def main():
    while True:
        date_now = datetime.now()
        info = f"app-" \
               f"{date_now.strftime('%H')}_" \
               f"{date_now.strftime('%M')}_" \
               f"{date_now.strftime('%S')}" \
               f".log"

        with open(info, "w") as log_file:
            log_file.write(f"{date_now}")

        print(f"{info}")
        print(f"{date_now}")
        sleep(1)


if __name__ == "__main__":
    main()
