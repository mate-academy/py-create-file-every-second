import time
from datetime import datetime


def main() -> None:
    while True:
        # Отримуємо поточний час
        now = datetime.now()
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"

        # Форматуємо вміст файлу (timestamp)
        timestamp_content = now.strftime("%Y-%m-%d %H:%M:%S")

        # Створюємо та записуємо файл
        with open(file_name, "w", encoding="utf-8") as f:
            f.write(timestamp_content)

        # Виводимо інформацію в консоль
        print(f"{timestamp_content} {file_name}")

        # Чекаємо 1 секунду перед наступною ітерацією
        time.sleep(1)


if __name__ == "__main__":
    main()
