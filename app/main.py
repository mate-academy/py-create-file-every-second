from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    # write your code here
    while True:
        now = datetime.now()
        hours = now.hour
        minutes = now.minute
        seconds = now.second
        formatted_now_file = now.strftime("%Y-%m-%d")
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        with open(file_name, "w") as file:
            file.write(f"{formatted_now_file} {hours}:{minutes}:{seconds}")
        sleep(1)
        formatted_now_print = now.strftime("%Y-%m-%d %H:%M:%S")
        print(f"{formatted_now_print} {file_name}")


if __name__ == "__main__":
    main()
