import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT

def main():
    while True:
        # 1. Берем текущее время
        now = datetime.now()
        
        # 2. Формируем имя файла строго по условию
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        
        # 3. Формируем контент (без микросекунд, как в примере)
        timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
        
        # 4. Создаем файл и записываем контент
        with open(file_name, "w") as f: # "w", так как файл новый каждую секунду
            f.write(timestamp)
            
        # 5. Печатаем в консоль результат успешного создания
        print(f"{timestamp} {file_name}")
        
        # 6. Ждем 1 секунду до следующего файла
        time.sleep(1)

if __name__ == "__main__":
    main()
