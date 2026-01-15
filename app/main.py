from datetime import datetime
import time


def main() -> None:
    while True:
        current_time = datetime.now()
        file_name = (f"app-{current_time.hour}_"
                     f"{current_time.minute}_"
                     f"{current_time.second}.log")
        file_content = str(current_time)

        with open(file_name, "w") as f:
            f.write(file_content)

        print(f"{current_time} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
