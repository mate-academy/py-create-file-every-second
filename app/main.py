from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        date_and_time = datetime.now()
        filename = date_and_time.strftime("app-%-H_%-M_%-S.log")
        with open(filename, "w") as file:
            file.write(str(date_and_time))
            print(date_and_time, filename)
        time.sleep(1)


if __name__ == "__main__":
    main()
