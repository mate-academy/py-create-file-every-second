from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep
import os

def main():
    # Створюємо папку logs, якщо її немає
    os.makedirs("logs", exist_ok=True)

    try:
        while True:
            now = datetime.now()

            # Формуємо унікальне ім'я файлу за година_хвилина_секунда
            filename = f"logs/app-{now.hour}_{now.minute}_{now.second}.log"

            # Записуємо timestamp у файл
            with open(filename, "w") as f:
                f.write(now.strftime("%Y-%m-%d %H:%M:%S"))

            # Вивід у консоль
            print(f"{now.strftime('%Y-%m-%d %H:%M:%S')} {filename}")

            # Чекаємо 1 секунду перед створенням наступного файлу
            sleep(1)

    except KeyboardInterrupt:
        print("\nProgram stopped by user.")

if __name__ == "__main__":
    main()

