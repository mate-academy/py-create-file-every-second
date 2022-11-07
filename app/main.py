import time
from datetime import datetime


def main() -> str:
    while True:
        file_name = datetime.now()
        with open(f"app-{file_name.hour}_"
                  f"{file_name.minute}_"
                  f"{file_name.second}.log", "w") as new_file:
            new_file.write(str(file_name))
            print(f"{file_name} app-{file_name.hour}_"
                  f"{file_name.minute}_"
                  f"{file_name.second}.log")
        time.sleep(1)


if __name__ == "__main__":
    main()
