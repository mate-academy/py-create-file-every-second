from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep

def main() -> None:
    while True:
        date_now = datetime.now()
        current_time = str(date_now.time()).split(":")
        file_name = f"app-{current_time[0]}_{current_time[1]}_{current_time[2][:2]}.log"
        with open(file_name, "w") as new_file:
            new_file.write(f"{date_now}")
        with open(file_name, "r") as file:
            print(file.read(), file_name)
        sleep(1)


if __name__ == "__main__":
    main()
