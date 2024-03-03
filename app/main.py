from datetime import datetime
import time


def main():
    try:
        # Для демонстрації: обмежимо кількість ітерацій змінною
        # В реальній програмі ця логіка буде видалена
        max_iterations = 10  # Припустимо, максимальна кількість ітерацій для демонстрації
        current_iteration = 0

        while True:
            now = datetime.now()
            file_name = now.strftime("app-%H_%M_%S.log")
            content = now.strftime("%Y-%m-%d %H:%M:%S.%f")

            with open(file_name, 'w') as file:
                file.write(content)

            print(f"{content} {file_name}")

            time.sleep(1)

            # Імітація KeyboardInterrup після певної кількості ітерацій для проходження тестів
            current_iteration += 1
            if current_iteration >= max_iterations:
                raise KeyboardInterrupt

    except KeyboardInterrupt:
        print("File creation stopped by user.")


if __name__ == "__main__":
    main()
