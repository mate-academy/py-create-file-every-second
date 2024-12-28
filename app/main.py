from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        try:
            current_time = datetime.now()
            hours = current_time.hour
            minutes = current_time.minute
            seconds = current_time.second
            file_name = f"app-{hours}_{minutes}_{seconds}.log"
            new_file = open(file_name, "w")
            new_file.write(str(current_time))
            new_file.close()
            print(current_time, file_name)
            sleep(1)
        except KeyboardInterrupt:
            raise SystemExit("Process terminated by user.")


if __name__ == "__main__":
    main()
