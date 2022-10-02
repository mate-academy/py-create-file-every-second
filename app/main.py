from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        get_time = datetime.now()
        file_name = f"app-{get_time.hour}_" \
                    f"{get_time.minute}_" \
                    f"{get_time.second}.log"
        with open(file_name, "w") as file:
            file.write(str(get_time))
        print(get_time, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
