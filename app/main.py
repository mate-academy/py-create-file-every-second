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

            with open(file_name, "w") as new_file:
                new_file.write(str(current_time))

            print(current_time, file_name)
            sleep(1)
        except KeyboardInterrupt:
            print("Process terminated by user.")
            return


if __name__ == "__main__":
    main()
