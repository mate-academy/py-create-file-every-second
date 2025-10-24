from datetime import datetime
import time


def main() -> None:
    while True:
        day_to_name = datetime.now().strftime("%H_%M_%S")
        name = f"app-{day_to_name}.log"
        to_file_time = f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        with open(name, "w", encoding="utf-8") as f:
            f.write(f"{to_file_time}")

        print(f"{to_file_time} {name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
