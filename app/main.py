from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        t = str(datetime.now())
        name_for_task = "app-" + t[11:13] + "_" \
                        + t[14:16] + "_" + t[17:19] + ".log"
        with open(name_for_task, 'w') as f:
            f.write(t)
            print(t + " " + name_for_task)
            sleep(1)


if __name__ == "__main__":
    main()
