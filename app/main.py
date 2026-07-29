from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        timestamp = datetime.now()
        formatted_time = timestamp.strftime("%H_%M_%S")
        filename = f"app-{formatted_time}.log"

        with open(filename, "w") as f:
            f.write(str(timestamp))

        print(f"{timestamp} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
