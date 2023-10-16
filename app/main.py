from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:

    while True:
        curr_time = datetime.now().strftime("%H:%M:%S").split(":")
        file_name = f"app-{curr_time[0]}_{curr_time[1]}_{curr_time[2]}.log"

        with open(file_name, "w") as f:
            current_time = datetime.now()
            formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
            f.write(str(formatted_time))
            print(formatted_time + " " + file_name)
            sleep(1)


if __name__ == "__main__":
    main()
