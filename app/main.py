from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        file_content = f"{now} {file_name}\n"
        with open(file_name, "w") as file:
            file.write(str(now))
        print(file_content, end="")
        sleep(1)


if __name__ == "__main__":
    main()
