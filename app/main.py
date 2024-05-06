import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        time_now = datetime.now()
        new_file = open(f"app-{time_now.hour}"
                        f"_{time_now.minute}"
                        f"_{time_now.second}.log", "w")
        new_file.write(str(time_now))
        print(datetime.now(), new_file)
        time.sleep(1)


if __name__ == "__main__":
    main()
