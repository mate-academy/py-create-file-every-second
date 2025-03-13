from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        now = datetime.now()
        hours = now.hour
        minutes = now.minute
        seconds = now.second
        filena = f"app-{hours}_{minutes}_{seconds}.log"
        file = open(filena, "w+")
        content = str(now)
        content = content.rsplit(".")[0]
        file.write(content)
        file.close()
        print(content + " " + filena)
        sleep(1)


if __name__ == "__main__":
    main()
