from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main():
    while True:
        now = datetime.now()  # тест підставляє mock-дату

        # Створюємо файл строго за форматом
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"

        # Записуємо timestamp у файл
        with open(filename, "w") as f:
            f.write(now.strftime("%Y-%m-%d %H:%M:%S"))

        # Вивід у консоль
        print(f"{now.strftime('%Y-%m-%d %H:%M:%S')} {filename}")
