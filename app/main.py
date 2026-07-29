from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep  # DO NOT CHANGE THIS IMPORT


def get_current_timestamp() -> str:
    """Повертає поточний timestamp у форматі YYYY-MM-DD HH:MM:SS."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def create_log_file() -> None:
    """Створює файл з ім'ям у форматі app-{hours}_{minutes}_{seconds}.log."""
    current_time: datetime = datetime.now()
    file_name: str = (
        f"app-{current_time.hour}_{current_time.minute}_"
        f"{current_time.second}.log"
    )
    timestamp: str = get_current_timestamp()

    with open(file_name, mode="w", encoding="utf-8") as file:
        file.write(timestamp)

    print(f"{timestamp} {file_name}")


def main() -> None:
    """Головна функція, яка створює файл кожну секунду."""
    while True:
        create_log_file()
        sleep(1)


if __name__ == "__main__":
    main()
