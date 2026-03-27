import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        now = datetime.now().replace(microsecond=0)
        hours = now.hour
        minutes = now.minute
        seconds = now.second
        filename = f"app-{hours}_{minutes}_{seconds}.log"
        out_line = f"{now} {filename}"
        with open(filename, "w") as file:
            file.write(f"{now}")
        print(out_line)
        time.sleep(1)


if __name__ == "__main__":
    main()
    # Output:
    # ...
    # 2020-01-01 14:10:07 app-14_10_7.log
    # 2020-01-01 14:10:08 app-14_10_8.log
    # 2020-01-01 14:10:09 app-14_10_9.log
    # ...
