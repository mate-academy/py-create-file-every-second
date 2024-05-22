from datetime import datetime
import time


def main() -> None:
    while True:
        # Отримуємо поточний час
        now = datetime.now()

        # Форматуємо ім'я файлу
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"

        # Записуємо час у файл
        with open(file_name, "w") as file:
            file.write(now.strftime("%Y-%m-%d %H:%M:%S.%f"))

        # Виводимо інформацію про створення файлу
        print(f"{now.strftime("%Y-%m-%d %H:%M:%S.%f")} {file_name}")

        # Затримка на 1 секунду
        time.sleep(1)


main()
