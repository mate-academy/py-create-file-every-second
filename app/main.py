from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        currnet_time = datetime.now()

        file_name = \
            (f"app-{currnet_time.hour}"
             f"_{currnet_time.minute}_"
             f"{currnet_time.second}.log")

        with open(file_name, "w") as f:
            timestamp = currnet_time.strftime("%Y-%m-%d %H:%M:%S.%f")
            f.write(timestamp)

        print(f"{timestamp} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
