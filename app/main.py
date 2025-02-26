from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")  # Видалено .%f
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"

        try:
            with open(filename, "w") as file:
                file.write(timestamp)

            print(timestamp, filename)
        except Exception as e:
            print(f"Error creating file {filename}: {e}")

        sleep(1)


if __name__ == "__main__":
    main()
