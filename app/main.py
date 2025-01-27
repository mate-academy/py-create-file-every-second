from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        hours = datetime.now().hour
        minutes = datetime.now().minute
        seconds = datetime.now().second
        date = datetime.now().date()
        time = datetime.now().time()
        name_of_file = f"app-{hours}_{minutes}_{seconds}.log"
        file_content = f"{date} {time}"
        with open(name_of_file, "a") as f:
            f.write(file_content)
        sleep(1)
        print(f"{file_content} {name_of_file}")


if __name__ == "__main__":
    main()
