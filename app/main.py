from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date = datetime.now()
        hours = date.hour
        minutes = date.minute
        seconds = date.second

        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        content = f"{date}"

        with open(file_name, "w") as file:
            file.write(content)

        print(f"{content} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
