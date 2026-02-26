from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        file_name = f"app-{current_time.strftime('%H_%M_%S')}.log"
        file_content = current_time.strftime("%Y-%m-%d %H:%M:%S")

        with open(file_name, "w") as f:
            f.write(file_content)
        print(file_content, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
