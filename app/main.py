from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while 1:
        hours = datetime.now().hour
        minutes = datetime.now().minute
        seconds = datetime.now().second

        filename = f"app-{hours}_{minutes}_{seconds}.log"
        file_content = f"{datetime.now()}"
        print_content = f"{file_content} {filename}"

        with open(filename, 'a') as f:
            f.write(file_content)
            print(print_content)
            time.sleep(1)


if __name__ == "__main__":
    main()
