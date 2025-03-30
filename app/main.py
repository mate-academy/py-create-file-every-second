# import os
from time import sleep
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    # dirname = os.path.dirname(os.path.abspath(__file__))
    while True:
        time_now = datetime.now()
        file_name = ("app-{}_{}_{}.log".format(
            time_now.hour,
            time_now.minute,
            time_now.second
        ))
        #  with open(f"{dirname}/{file_name}", "w") as f:
        with open(file_name, "w") as f:
            f.write(str(time_now))
        print(str(time_now) + " " + file_name)
        sleep(1)


if __name__ == "__main__":
    main()
