from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        time_of = datetime.now()
        with open(f"app-{time_of.hour}"
                  f"_{time_of.minute}_"
                  f"{time_of.second}" + ".log", "w") as f:
            f.write(str(time_of))
            print(time_of, f"app-{time_of.hour}_"
                           f"{time_of.minute}_"
                           f"{time_of.second}" + ".log")
            time.sleep(1)


if __name__ == "__main__":
    main()
