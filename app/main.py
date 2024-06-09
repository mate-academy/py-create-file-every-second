from datetime import datetime
import time


def main() -> None:
    while True:
        temp_time = str(datetime.now())
        temp_file = (f"app-{temp_time[11:19].split(":")[0]}"
                     f"_{temp_time[11:19].split(":")[1]}"
                     f"_{temp_time[11:19].split(":")[2]}.log")
        with open(f"{temp_file}", "w") as file:
            file.write(str(temp_time))
        print(temp_time, temp_file)
        time.sleep(1)


if __name__ == "__main__":
    main()
