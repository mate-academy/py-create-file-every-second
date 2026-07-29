from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        timestamp = datetime.now()
        formatted_time = timestamp.strftime("%H_%M_%S")
        file_name = f"app-{formatted_time}.log"

        with open(file_name, "w") as file:
            file.write(str(timestamp))

        print(f"{timestamp} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
