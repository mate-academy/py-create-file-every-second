from datetime import datetime
from time import sleep


while True:
    # Текущее время
    now = datetime.now()

    # Формируем имя файла
    file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"

    # Создаём файл и пишем в него timestamp
    with open(file_name, "w") as f:
        f.write(now.strftime("%Y-%m-%d %H:%M:%S"))

    # Печатаем в консоль
    print(f"{now.strftime('%Y-%m-%d %H:%M:%S')} {file_name}")

    # Ждём 1 секунду
    sleep(1)
