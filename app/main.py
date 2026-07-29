from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        time_now = datetime.now()
        file_name = f"app-{time_now:%H_%M_%S}.log"
        file_content = str(time_now)
        with open(file_name, "w") as f:
            f.write(file_content)
            print(f"{file_content} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
