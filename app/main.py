from datetime import datetime, time  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        content_file = now.strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "w") as file:
            file.write(content_file)
        print(f"{content_file} {file_name}")
        sleep(1)

if __name__ == "__main__":
    main()
