from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        curr_time = datetime.now().strftime("%H:%M:%S").split(":")
        file_time = f"app-{curr_time[0]}_{curr_time[1]}_{curr_time[2]}.log"
        with open(file_time, "w") as f:
            current = datetime.now()
            time = current.strftime("%Y-%m-%d %H:%M:%S")
            f.write(str(time))
            print(time + " " + file_time)
        sleep(1)


if __name__ == "__main__":
    main()
