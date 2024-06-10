from datetime import datetime
import time


def main() -> None:
    while True:
        temp_time = str(datetime.now())
        only_time = temp_time[11:19].split(":")
        temp_file = f"app-{only_time[0]}_{only_time[1]}_{only_time[2]}.log"
        with open(f"{temp_file}", "w") as file:
            file.write(str(temp_time))
        print(temp_time, temp_file)
        time.sleep(1)


if __name__ == "__main__":
    main()
