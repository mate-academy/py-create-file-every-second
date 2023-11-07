from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> str:
    while True:
        current_time = datetime.now()
        file_content = str(current_time)
        file_name = (f"app-{current_time.strftime('%H')}_"
                     f"{current_time.strftime('%M')}_"
                     f"{current_time.strftime('%S')}.log")
        with open(file_name, "w") as file:
            file.write(file_content)
            print(f"{current_time} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
