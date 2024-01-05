import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        date = datetime.now()
        filename = f"app-{date.hour}_{date.minute}_{date.second}.log"
        if date.microsecond == 0:
            microsec = ""
        else:
            microsec = "." + str(date.microsecond)
        content = ("" + str(date.year) + "-"
                   + str(date.month) + "-"
                   + str(date.day) + " "
                   + str(date.hour) + ":"
                   + str(date.minute) + ":"
                   + str(date.second)
                   + microsec)
        with open(filename, "w") as f:
            f.write(content)
        print(f"{content} {filename}")
        time.sleep(1)


if __name__ == "__main__":
    main()
