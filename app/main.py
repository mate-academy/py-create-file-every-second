from datetime import datetime
import time
import os


def create_file() -> str:
    """Создаёт один файл с текущим временем и возвращает имя файла."""
    now = datetime.now()
    filename = f"app-{now.hour}_{now.minute}_{now.second}.log"
    with open(filename, "w") as f:
        f.write(now.strftime("%Y-%m-%d %H:%M:%S"))
    print(f"{now.strftime('%Y-%m-%d %H:%M:%S')} {filename}")
    return filename


def main() -> None:
    """Бесконечный цикл создания файлов каждую секунду."""
    while True:
        create_file()
        time.sleep(1)


if __name__ == "__main__":
    main()
