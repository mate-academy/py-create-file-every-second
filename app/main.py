from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> str:
    while True:
        time_now = datetime.now()
        file_name = (f"app-{time_now.hour}"
                     f"_{time_now.minute}"
                     f"_{time_now.second}.log"
                     )
        with open(file_name, "w") as file_hand:
            format_time = time_now.strftime("%Y-%m-%d %H:%M:%S")
            file_hand.write(f"{format_time}")
        time.sleep(1)
        print(f"{format_time} {file_name}")


if __name__ == "__main__":
    main()
