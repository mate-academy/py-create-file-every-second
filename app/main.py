from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        file_name = datetime.now().strftime("%H:%M:%S").replace(":", "_")
        current_time = datetime.now()
        sleep(1)
        with open(f"app-{file_name}.log", "w") as file:
            file.write(str(current_time))
        print(current_time, f"app-{file_name}.log")


if __name__ == "__main__":
    main()
