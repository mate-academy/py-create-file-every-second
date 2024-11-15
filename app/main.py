from datetime import datetime
from time import sleep


def main() -> None:
    while True:

        now = datetime.now()
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        file_content = now.strftime("%Y-%m-%d %H:%M:%S")

        with open(file_name, "w") as file:
            file.write(file_content)

        print(f"{file_content} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
