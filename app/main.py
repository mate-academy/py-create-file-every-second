import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        now = datetime.now()
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"
        file_time = now.strftime("%Y-%m-%d %H:%M:%S")
        with open(f"{filename}", "w") as f:
            f.write(file_time)
        print(f"{file_time} {filename}")
        time.sleep(1)


if __name__ == "__main__":
    main()
