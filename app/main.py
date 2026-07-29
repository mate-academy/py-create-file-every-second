from datetime import datetime   # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        file_content = f"{now.__str__()}"
        with open(file_name, "w") as output_file:
            output_file.write(file_content)
        print(f"{file_content} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
