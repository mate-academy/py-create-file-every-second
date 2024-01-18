from datetime import datetime  # DO NOT CHANGE THIS IMPOR
from time import sleep
import os
import sys


def main() -> None:
    os.chdir(os.path.dirname(sys.argv[0]))
    while True:
        date = datetime.now()
        hr, mn, sd = date.hour, date.minute, date.second
        name = f"app-{hr}_{mn}_{sd}.log"
        new_file = open(name, "w")
        new_file.write(str(date))
        new_file.close()
        print(f"{date} {name}")
        sleep(1)


if __name__ == "__main__":
    main()
