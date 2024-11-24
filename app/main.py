from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        actual_time = str(datetime.now())
        with open(f"app-{actual_time[11:13]}_"
                  f"{actual_time[14:16]}_"
                  f"{actual_time[17:19]}.log", "w") as f:
            f.write(f"{actual_time}")
        print(f"{actual_time} {f.name}")
        sleep(1)


if __name__ == "__main__":
    main()
