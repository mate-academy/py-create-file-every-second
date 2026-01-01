from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        # hours = now.strftime("%H")
        # minutes = now.strftime("%M")
        # seconds = now.strftime("%S")
        # filename = f"app-{hours}_{minutes}_{seconds}.log"
        filename = f"app-{now.strftime('%H_%M_%S')}.log"
        with open(filename, "w") as log:
            log.write(now.strftime("%Y-%m-%d %H:%M:%S"))
        print(now.strftime("%Y-%m-%d %H:%M:%S") + " " + filename)
        sleep(1)


if __name__ == "__main__":
    main()
