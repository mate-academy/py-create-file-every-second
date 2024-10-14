from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        time_now = datetime.now()
        filename = (f"app-{time_now.hour}_{time_now.minute}"
                    f"_{time_now.second}.log")
        with open(filename, "w") as f:
            f.write(str(time_now))
        print(f"{str(time_now)} {filename}")

        time.sleep(1)


if __name__ == "__main__":
    main()
