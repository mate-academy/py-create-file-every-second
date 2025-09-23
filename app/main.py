from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        # Отримуємо поточний час
        now = datetime.now()

        # Формуємо ім'я файлу без папки і без мікросекунд
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"

        # Записуємо timestamp у файл
        with open(filename, "w") as f:
            f.write(now.strftime("%Y-%m-%d %H:%M:%S"))

        # Вивід у консоль
        print(f"{now.strftime('%Y-%m-%d %H:%M:%S')} {filename}")

        # Чекаємо 1 секунду
        sleep(1)


if __name__ == "__main__":
    main()
