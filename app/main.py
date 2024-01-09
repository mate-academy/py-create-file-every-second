from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        current_datetime = datetime.now()
        current_time = (str(current_datetime).split(" ")[1]).split(".")[0]
        file_name = "app-" + current_time.replace(":", "_") + ".log"
        with open(file_name, "w") as new_file:
            new_file.write(str(current_datetime))
            print(str(current_datetime), file_name)
            sleep(1)


if __name__ == "__main__":
    main()
