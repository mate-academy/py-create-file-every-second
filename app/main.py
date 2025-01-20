import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while 1:
        file_name = (f"app-{datetime.now().hour}_{datetime.now().minute}"
                     f"_{datetime.now().second}.log")
        content = datetime.now()
        with open(file_name, "w") as file_to_write:
            file_to_write.write(str(content))
            print(content, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
