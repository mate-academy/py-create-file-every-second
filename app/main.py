from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep
import os

def main():
    # Створюємо папку logs, якщо її немає
    try:
        os.makedirs("logs", exist_ok=True)
    except Exception as e:
        print(f"Cannot create logs folder: {e}")
        return

    try:
        while True:
            now = datetime.now()

            # Формуємо унікальне ім'я файлу з мілісекундами
            filename = f"logs/app-{now.strftime('%H_%M_%S_%f')}.log"

            # Записуємо timestamp у файл з обробкою помилок
            try:
                with open(filename, "w") as f:
                    f.write(now.strftime("%Y-%m-%d %H:%M:%S"))
            except Exception as e:
                print(f"Cannot write to file {filename}: {e}")
                continue

            # Вивід у консоль
            print(f"{now.strftime('%Y-%m-%d %H:%M:%S')} {filename}")

            # Чекаємо 1 секунду перед наступним файлом
            sleep(1)

    except KeyboardInterrupt:
        print("\nProgram stopped by user.")

if __name__ == "__main__":
    main()

