from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        try:
            now = datetime.now()
            formatted_time = now.strftime("%H_%M_%S")
            with open(f"app-{formatted_time}.log", "w") as time_stamp:
                time_stamp.write(str(now))
        except Exception as e:
            print(e)
        else:
            print(f"{str(now)} app-{formatted_time}.log")
            sleep(1)


if __name__ == "__main__":
    main()
