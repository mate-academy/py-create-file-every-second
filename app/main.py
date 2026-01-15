import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:

    time_now = datetime.now()

    while True:
        file_name = (
            f"app-{time_now.hour}_{time_now.minute}_{time_now.second}.log"
        )

        with open(file_name, "w") as time_file:
            time_now_formatted_to_str = time_now.strftime("%Y-%m-%d %H:%M:%S")
            time_file.write(time_now_formatted_to_str)
            print(time_now_formatted_to_str + " " + file_name)
            time.sleep(1)
            time_now = datetime.now()


if __name__ == "__main__":
    main()
