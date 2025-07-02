from datetime import datetime
from time import sleep

def main():
    while True:
        now = datetime.now()

        filename = f"app-{now.strftime('%H_%M_%S')}.log"

        # Запис у файл без переносу рядка
        with open(filename, "w") as file:
            file.write(f"{now.strftime('%Y-%m-%d %H:%M:%S')}")

        # Вивід у консоль без \n
        print(f"{now.strftime('%Y-%m-%d %H:%M:%S')} {filename}", end="")

        sleep(1)
        print()  # Ручний перехід на новий рядок для зручності

if __name__ == "__main__":
    main()
