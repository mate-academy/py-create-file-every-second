from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        content = datetime.now()
        file_name = f"app-{content.hour}_{content.minute}_{content.second}.log"

        with open(file_name, "w") as file:
            file.write(str(content))

        print(content, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
