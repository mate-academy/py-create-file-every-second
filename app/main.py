import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    # write your code here
    while True:
        name_time = datetime.now().strftime("%H_%M_%S")
        with open(f"app-{name_time}.log", "w") as f:
            f.write(str(datetime.now()))
            print(str(datetime.now()) + f" app-{name_time}.log")
            time.sleep(1)


if __name__ == "__main__":
    main()
