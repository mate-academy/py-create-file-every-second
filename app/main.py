from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        current_time = datetime.now()
        formatted_time = str(current_time.strftime("%Y-%m-%d %H:%M:%S"))
        hour = str(current_time.hour)
        minute = str(current_time.minute)
        sec = str(current_time.second)
        try:
            with open(f"app-{hour}_{minute}_{sec}.log", "w") as f:
                f.write(f"{formatted_time}")
        finally:
            with open(f"app-{hour}_{minute}_{sec}.log", "r") as f:
                print(f.read(), f"app-{hour}_{minute}_{sec}.log")
        time.sleep(1)


if __name__ == "__main__":
    main()
