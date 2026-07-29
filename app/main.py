from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        formatted_time = current_time.strftime("%H_%M_%S")
        file_name = f"app-{formatted_time}.log"
        with open(file_name, "w") as f:
            f.write(f"{current_time}")
        print(f"{current_time} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
