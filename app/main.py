from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        current_time = datetime.now()
        file_name = f"app-{current_time.hour}" \
                    f"_{current_time.minute}" \
                    f"_{current_time.second}.log"
        with open(file_name, "w") as file:
            file.write(str(current_time))

        print(current_time, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
