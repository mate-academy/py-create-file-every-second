from datetime import datetime
import time


def main() -> None:
    file_count = 0

    while True:
        file_count += 1
        current_time = datetime.now()
        file_name = current_time.strftime("app-%H_%M_%S.log")
        file_content = current_time.isoformat(sep=" ")

        with open(file_name, "w") as file:
            file.write(file_content)
        print(file_content, file_name)

        time.sleep(1)


if __name__ == "__main__":
    main()
