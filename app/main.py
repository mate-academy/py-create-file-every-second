from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    # write your code here
    try:
        while True:
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

            file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"

            with open(file_name, "w") as file:
                file.write(timestamp)

            print(f"{timestamp} {file_name}")

            time.sleep(1)
    except KeyboardInterrupt:
        raise KeyboardInterrupt


if __name__ == "__main__":
    main()
