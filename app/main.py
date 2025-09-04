from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now_time = datetime.now()
        file_name = f"app-{now_time.strftime("%H_%M_%S")}.log"
        file_content = now_time.strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "w") as file:
            file.write(file_content)
        print(file_content, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
