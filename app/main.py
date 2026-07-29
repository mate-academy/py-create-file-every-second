import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        curr_time = datetime.now()
        filename = (f"app-{curr_time.hour}_{curr_time.minute}"
                    f"_{curr_time.second}.log")
        with open(filename, "w") as f:
            f.write(str(curr_time))
        print(f"{curr_time} {filename}")
        time.sleep(1)


if __name__ == "__main__":
    main()
