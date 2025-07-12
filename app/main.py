from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:

    while True:

        all_timing = datetime.now()
        filename = (f"app-{all_timing.hour}_"
                    f"{all_timing.minute}_{all_timing.second}.log")
        correct_time = all_timing.strftime("%Y-%m-%d %H:%M:%S")

        with open(filename, "x") as f:
            f.write(correct_time)
            print(correct_time + " " + filename)
        time.sleep(1)


if __name__ == "__main__":
    main()
