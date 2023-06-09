from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        current_time = datetime.now()
        file_name = current_time.strftime("app-%H_%M_%S.log")
        file_content = str(current_time)

        with open(file_name, "w") as file:
            file.write(file_content)

        print(f"{current_time} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
