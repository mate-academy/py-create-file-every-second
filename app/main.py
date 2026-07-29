from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now()

        hour = now.hour
        minutes = now.minute
        seconds = now.second

        file_name = f"app-{hour}_{minutes}_{seconds}.log"
        file_content = str(now)

        with open(file_name, "w") as stamped_file:
            stamped_file.write(file_content)

        print(f"{file_content} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
