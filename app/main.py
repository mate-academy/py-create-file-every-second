from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        current_date = datetime.now()
        current_second = str(current_date.second)
        if current_second[0] == "0":
            current_second = current_second[1]

        file_name = ("app-"
                     + str(current_date.hour)
                     + "_" + str(current_date.minute)
                     + "_" + current_second
                     + ".log")

        with open(file_name, "w") as f:
            f.write(str(current_date))
            print(f"{current_date} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
