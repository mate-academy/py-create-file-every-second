from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        date_time = datetime.now()
        file_name = date_time.strftime("%X")
        original = file_name.split(":")
        with open(f"app-{original[0]}_{original[1]}_{original[2]}.log", "a") \
                as file:
            file.write(f"{date_time}")
        time.sleep(1)
        print(f"{date_time} app-{original[0]}_{original[1]}_{original[2]}.log")


if __name__ == "__main__":
    main()
