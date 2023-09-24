from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        filename = (f"app-{datetime.now().hour}_"
                    f"{datetime.now().minute}_"
                    f"{datetime.now().second}.log")
        file_content = str(datetime.now())
        with open(filename, "w") as file:
            file.write(file_content)
            sleep(1)
            print(f"{file_content} {filename}")


if __name__ == "__main__":
    main()
