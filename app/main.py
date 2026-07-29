import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:

        file_name = (f"app-{datetime.now().hour}_"
                     f"{datetime.now().minute}_"
                     f"{datetime.now().second}.log")
        new_file = open(file_name, "w")
        content = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        new_file.write(content)
        print(content + " " + file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
