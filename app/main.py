from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    # write your code here
    while True:
        current_data = datetime.now()
        data = str(current_data)[:19]
        hours = data[-8:-6]
        minutes = data[-5:-3]
        seconds = data[-2:]
        if seconds[0] == "0":
            seconds = data[-1:]

        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        with open(file_name, "w") as file:
            file.write(str(current_data))
            print(f"{str(current_data)} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
