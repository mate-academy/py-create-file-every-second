from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main(sleep_enabled=True):
    while True:
        try:
            now = datetime.now()
            file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

            with open(file_name, "w", encoding="utf-8") as f:
                f.write(timestamp)

            print(f"{timestamp} {file_name}")

            if sleep_enabled:
                time.sleep(1)

        except KeyboardInterrupt:
            # Не приглушуємо — передаємо далі
            raise
