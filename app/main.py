from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        filename = f"app-{current_time.hour}_" \
            f"{current_time.minute}_" \
            f"{current_time.second}.log"
        log_file = open(filename, "w")
        file_content = f"{current_time.year}-" \
            f"{current_time.month}-" \
            f"{current_time.day} " \
            f"{current_time.hour}:" \
            f"{current_time.minute}:" \
            f"{current_time.second}"
        log_file.write(file_content)
        log_file.close()
        print(f"{file_content} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
