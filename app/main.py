from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        hours = now.hour
        minutes = now.minute
        seconds = now.second
        timefilena = f"app-{hours}_{minutes}_{seconds}.log"
        timefile = open(timefilena, "w+")
        content = str(now)
        content = content.rsplit(".")[0]
        timefile.write(content)
        timefile.close()
        print(content + " " + timefilena)
        sleep(1)


if __name__ == "__main__":
    main()
