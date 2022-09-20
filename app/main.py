from datetime import datetime
from time import sleep


def main():

    while True:
        current_time = datetime.now()
        file_name = f"app-{current_time.hour}_"\
                    f"{current_time.minute}_{current_time.second}.log"
        with open(file_name, "w") as f:
            f.write(str(current_time))
            print(current_time, f.name)
        sleep(1)


if __name__ == "__main__":
    main()
