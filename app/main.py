from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        content = now.__str__()
        print(content, file_name)
        with open(file_name, "w") as writer:
            writer.write(content)
        sleep(1)


if __name__ == "__main__":
    main()
