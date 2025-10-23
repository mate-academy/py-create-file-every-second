from datetime import datetime  # Імпортуємо, як вимагає завдання
import time                   # Імпортуємо модуль time для time.sleep()


def main() -> None:
    """
    Runs an infinite loop that creates a new log file every second.
    
    The file name is based on the current time (app-H_M_S.log),
    and the file content is the full timestamp.
    """
    
    # 5. Запускаємо нескінченний цикл
    while True:
        try:
            # Отримуємо поточний час
            now = datetime.now()
            
            # 1. Готуємо назву файлу (app-години_хвилини_секунди.log)
            file_name = (
                f"app-{now.hour}_{now.minute}_{now.second}.log"
            )
            
            # 2. Готуємо вміст файлу (повна мітка часу)
            # Приклад: 2020-01-01 14:10:07
            timestamp_content = now.strftime("%Y-%m-%d %H:%M:%S")
            
            # 3. Створюємо файл і записуємо в нього вміст
            with open(file_name, "w") as f:
                f.write(timestamp_content)
                
            # 4. Виводимо в консоль мітку часу і назву файлу
            print(f"{timestamp_content} {file_name}")

        except IOError as e:
            # Обробка, якщо раптом не вийде створити файл
            print(f"Error writing file: {e}")
        except KeyboardInterrupt:
            # Дозволяє зупинити програму натисканням Ctrl+C
            print("\nApp terminated by user.")
            break
            
        # 6. Чекаємо 1 секунду перед наступною ітерацією
        time.sleep(1)


if __name__ == "__main__":
    main()
