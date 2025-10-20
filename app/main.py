from datetime import datetime
import time


def main() -> None:
    while True:
        current_time = datetime.now()

        file_name = (f"app-{current_time.hour}_"
                     f"{current_time.minute}_"
                     f"{current_time.second}.log")
        content = current_time.strftime("%Y-%m-%d %H:%M:%S")

        with open(file_name, "w") as file:
            file.write(content)

        print(f"{content} {file_name}")

        time.sleep(1)

if __name__ == "__main__":
    main()
