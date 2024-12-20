import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        timing = datetime.now()
        cleared_time = str(timing).split(" ")
        timex = (cleared_time[1].split("."))
        ready_string = f'app-{timex[0].replace(":", "_")}.log'
        with open(ready_string, "w") as file:
            file.write(str(timing))
        print(f"{timing} {ready_string}")
        time.sleep(1)


if __name__ == "__main__":
    main()
