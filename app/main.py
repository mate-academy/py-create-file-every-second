from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        date = datetime.now()
        year = date.year
        month = date.month
        day = date.day

        hour = date.hour
        minute = date.minute
        second = date.second
        file_name = f"app-{hour}_{minute}_{second}.log"
        content = (f"{year}-{month}-{day} "
                   f"{hour}:{minute}:{second}")
        with open(file_name, "w") as file:
            print(content + " " + file_name)
            file.write(content)

        sleep(1)


if __name__ == "__main__":
    main()
