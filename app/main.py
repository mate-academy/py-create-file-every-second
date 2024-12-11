from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        filename = f"app-{datetime.now().strftime("%H_%M_%S")}.log"
        with open(filename, "w") as file:
            file.write(current_time)

        print(f"{current_time} {filename}")
        time.sleep(1)


if __name__ == "__main__":
    main()
