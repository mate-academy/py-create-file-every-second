from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now()
        hours, minutes, seconds = now.hour, now.minute, now.second

        content = f"{now.strftime('%Y-%m-%d %H:%M:%S')}"
        file_name = f"app-{hours}_{minutes}_{seconds}.log"

        with open(file_name, "w") as f:
            f.write(f"{content}")

        print(f"{content} {file_name}")

        time.sleep(1)


if __name__ == "__main__":
    main()
