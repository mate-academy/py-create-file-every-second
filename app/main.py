from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        currnet_time = datetime.now()

        with open(f"app-{currnet_time.hour}_"
                  f"{currnet_time.minute}_"
                  f"{currnet_time.second}.log", "a") as f:
            f.write(str(currnet_time))
            print(str(currnet_time), f"app-"
                                     f"{currnet_time.hour}"
                                     f"_{currnet_time.minute}"
                                     f"_{currnet_time.second}.log")

        time.sleep(1)


if __name__ == "__main__":
    main()
