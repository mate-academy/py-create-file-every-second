from datetime import datetime
import time


def main() -> None:
    while True:
        file_name = f"app-{datetime.now().strftime('%H_%M_%S')}.log"
        with open(file_name, "w") as file:
            file_content = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            file.write(file_content)
            print(f"{file_content} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
