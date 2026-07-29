from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        time_file = datetime.now()
        hours = time_file.hour
        minutes = time_file.minute
        seconds = time_file.second
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        with open(file_name, "w") as f:
            f.write(str(time_file))

        with open(file_name) as f_2:
            print(f_2.read() + " " + file_name)

        time.sleep(1)


if __name__ == "__main__":
    main()
