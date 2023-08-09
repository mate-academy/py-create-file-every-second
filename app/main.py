from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        timestamp = datetime.now()

        hours = timestamp.strftime("%H")
        minutes = timestamp.strftime("%M")
        seconds = timestamp.strftime("%S")

        filename = f"app-{hours}_{minutes}_{seconds}.log"

        with open(filename, "w") as file:
            file.write(f"{timestamp}")

        time.sleep(1)

        if file.closed:
            with open(filename, "r") as file2:
                print(f"{file2.read()} {filename}")


if __name__ == "__main__":
    main()
