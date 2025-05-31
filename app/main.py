from datetime import datetime
from time import sleep

def main() -> None:
    while True:
        now = datetime.now()
        hours = now.strftime("%H")
        minutes = now.strftime("%M")
        seconds = now.strftime("%S")

        filename = f"app-{hours}_{minutes}_{seconds}.log"
        with open(filename, "w") as f:
            f.write(now.strftime("%Y-%m-%d %H:%M:%S"))

        print(now.strftime("%Y-%m-%d %H:%M:%S"), filename)
        sleep(1)

if __name__ == "__main__":
    main()
