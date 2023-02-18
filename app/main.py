from datetime import datetime
import time


def main() -> None:
    while True:
        file_name = (
            "app-"
            + str(datetime.now().hour)
            + "_"
            + str(datetime.now().minute)
            + "_"
            + str(datetime.now().second)
            + ".log"
        )

        new_file = open(file_name, "w")
        new_file.write(str(datetime.now()))
        new_file.close()

        time.sleep(1)


if __name__ == "__main__":
    main()
