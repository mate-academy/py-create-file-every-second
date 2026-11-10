from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    try:
        while True:
            curr_time = datetime.now()
            file_name = (f"app-{curr_time.hour}_{curr_time.minute}_"
                         f"{curr_time.second}.log")

            with open(file_name, "w") as f:
                f.write(str(curr_time))
                print(str(curr_time) + " " + file_name)

            time.sleep(1)

    except KeyboardInterrupt:
        raise


if __name__ == "__main__":
    main()
