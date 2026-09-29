from datetime import datetime
import time


def main() -> None:
    while True:
        # 1. Отримуємо поточний час та дату
        now = datetime.now()

        # 2. Форматуємо вміст файлу (YYYY-MM-DD HH:MM:SS)
        content_timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

        # 3. Форматуємо ім'я файлу відповідно до шаблону без провідних нулів
        file_name = (
            f"app-{int(now.strftime('%H'))}_"
            f"{int(now.strftime('%M'))}_"
            f"{int(now.strftime('%S'))}.log"
        )

        # 4. Створюємо файл та записуємо в нього таймстемп
        with open(file_name, "w") as file:
            file.write(content_timestamp)

        # 5. Виводимо інформацію в консоль
        print(f"{content_timestamp} {file_name}")

        # 6. Засинаємо на 1 секунду перед наступною ітерацією
        time.sleep(1)


if __name__ == "__main__":
    main()
