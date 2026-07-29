from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now()
        hours, minutes, seconds = now.hour, now.minute, now.second
        file_name = f"app-{hours:02d}_{minutes:02d}_{seconds:02d}.log"
        file_content = now.strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "w") as new_file:
            new_file.write(file_content)
        print(f"{file_content} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
