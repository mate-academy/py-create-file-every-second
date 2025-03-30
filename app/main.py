from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        timer = datetime.now()
        hours = timer.strftime("%H")
        minutes = timer.strftime("%M")
        seconds = timer.strftime("%S")
        name_to_open = f"app-{hours}_{minutes}_{seconds}.log"
        with open(name_to_open, "w") as f:
            time_str = str(timer)
            f.write(time_str)
            print(f"{time_str} {name_to_open}")
            sleep(1)

if __name__ == "__main__":
    main()
