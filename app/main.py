from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        hours = now.strftime("%H")
        minutes = now.strftime("%M")
        seconds = now.strftime("%S")
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        try:
            with open(file_name, "w") as file:
                file.write(timestamp)
                print(f"{timestamp} {file_name}")
        except Exception as e:
            print(f"Error creating file {file_name}: {e}")
            continue
        sleep(1)


if __name__ == "__main__":
    main()
