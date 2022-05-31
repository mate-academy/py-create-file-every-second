from datetime import datetime
from time import sleep


def main():
    while True:
        date_now = datetime.now()
        time_info = f"{datetime.now().hour}_" \
                    f"{datetime.now().minute}_" \
                    f"{datetime.now().second}"
        with open(f"app-{time_info}.log", "w") as log_file:
            log_file.write(f"{date_now}")
            print(f"file with name app-{time_info}.log "
                  f"was created {date_now}")
            sleep(1)


if __name__ == "__main__":
    main()
