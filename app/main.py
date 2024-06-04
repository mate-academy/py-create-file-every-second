from datetime import datetime
from time import sleep


def main():
    while True:
        current_time = datetime.now()
        hours = current_time.hour
        minutes = current_time.minute
        seconds = current_time.second
        filename = f"app-{hours}_{minutes}_{seconds}.log"
        time = current_time.strftime("%Y-%m-%d %H:%M:%S")

        with open(filename, "a") as file:
            file.write(time)

        print(f"{current_time} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
