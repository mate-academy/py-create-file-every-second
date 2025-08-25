from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:

    while True:
        time = datetime.now()
        filename_format = time.strftime("%H_%M_%S")
        infile_format = time.strftime("%H:%M:%S")
        with open(f"app-{filename_format}.log", "w") as logfile:
            logfile.write(f"{time.date()} {infile_format}")
        print(f"{time.date()} {infile_format} "
              f"app-{filename_format}.log")
        sleep(1)


if __name__ == "__main__":
    main()
