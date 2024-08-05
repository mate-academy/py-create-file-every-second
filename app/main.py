import time
from datetime import datetime


def main() -> None:
    while True:
        # Отримання поточного часу
        current_time = datetime.now()

        # Формування імені файлу
        file_name = current_time.strftime("app-%H_%M_%S.log")

        # Створення файлу і запис у нього часу
        with open(file_name, "w") as file:
            timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
            file.write(timestamp)

        # Виведення на екран часу імені файлу
        print(f"{timestamp} {file_name}")

        # Використання затримки між ітераціями циклу
        time.sleep(1)


# Виклик функції main
if __name__ == "__main__":
    main()
