from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        real_time = datetime.now()
        with open(f"app-{real_time.hour}_"
                  f"{real_time.minute}_"
                  f"{real_time.second}.log", "a") as file:
            file.write(str(real_time))
            print(str(real_time), f"app-{real_time.hour}"
                                 f"_{real_time.minute}_"
                                  f"{real_time.second}.log")
            time.sleep(1)


if __name__ == "__main__":
    main()
