from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        # Получение текущего времени
        current_time = datetime.now()

        # Форматирование имени файла
        file_name = (
            f"app-{current_time.hour}_{current_time.minute}_"
            f"{current_time.second}.log"
        )

        # Запись временной метки в файл
        with open(file_name, "w") as file:
            file.write(str(current_time))

        # Вывод информации в консоль
        print(f"{current_time} {file_name}")

        # Задержка на 1 секунду
        sleep(1)


if __name__ == "__main__":
    main()
