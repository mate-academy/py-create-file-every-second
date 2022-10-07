from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        time_now = datetime.now()
        hours = time_now.strftime("%H")
        minutes = time_now.strftime("%M")
        seconds = time_now.strftime("%S")
        name = f"app-{hours}_{minutes}_{seconds}.log"
        time.sleep(1)
        now_print = time_now.strftime("%Y-%m-%d %H:%M:%S")
        with open(name, "w") as f:
            f.write(now_print)
            print(f"{time_now} {name}")


if __name__ == "__main__":
    main()
