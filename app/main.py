from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now()
        hour = now.hour
        minute = now.minute
        second = now.second
        filename = f"app-{hour}_{minute}_{second}.log"
        with open(filename, "w") as file:
            file.write(str(now.strftime("%Y-%m-%d %H:%M:%S")))
            print(f"{now.strftime('%Y-%m-%d %H:%M:%S')} {filename}")
            time.sleep(1)


if __name__ == "__main__":
    main()
