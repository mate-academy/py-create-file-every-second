from datetime import datetime  # DO NOT CHANGE THIS IMPOR
import time
import os
import sys


def main():
    os.chdir(os.path.dirname(sys.argv[0]))
    while True:
        d = datetime.now()
        h, m, s = d.hour, d.minute, d.second
        name = f"app-{h}_{m}_{s}.log"
        new_file = open(name, "w")
        new_file.write(str(d))
        new_file.close()
        print(f"{d} {name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
