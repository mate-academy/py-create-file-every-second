from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while (True):
        now = datetime.now()
        hours = now.hour
        minutes = now.minute
        seconds = now.second

        try:
            file_name = f"app-{hours}_{minutes}_{seconds}.log"

            # Формат YYYY-MM-DD HH:MM:SS
            formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(formatted_datetime)
            print(formatted_datetime + " " + file_name)
        except IOError as e:
            print(f"Виникла помилка при роботі з файлом: {e}")
        time.sleep(1)


if __name__ == "__main__":
    main()
