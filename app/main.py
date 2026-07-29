import time
from datetime import datetime


def main() -> None:
    while True:
        current_date = datetime.now()
        hh = current_date.hour
        mm = current_date.minute
        ss = current_date.second
        file_name = f"app-{hh}_{mm}_{ss}.log"
        with open(file_name, "w") as new_file:
            new_file.write(str(current_date))
        print(str(current_date), file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
