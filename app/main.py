from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    file_count = 0
    while True:
        now = datetime.now()
        timestamp = now.strftime("%H_%M_%S")
        filename = f"app-{timestamp}.log"
        with open(filename, "w") as file:
            file.write(str(now))
        print(f"{now} {filename}")
        file_count += 1
        time.sleep(1)
        if file_count >= 3:
            raise KeyboardInterrupt


if __name__ == "__main__":
    main()
