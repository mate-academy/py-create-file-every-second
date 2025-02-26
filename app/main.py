from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        # Отримуємо поточний час
        now = datetime.now()
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S.%f")
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"

        # Записуємо таймстемп у файл
        with open(filename, "w") as file:
            file.write(timestamp)

        # Виводимо інформацію у консоль
        print(timestamp, filename)

        # Чекаємо 1 секунду перед наступною ітерацією
        sleep(1)
    # write your code here
    pass


if __name__ == "__main__":
    main()
