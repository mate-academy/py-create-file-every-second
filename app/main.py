from datetime import datetime
import time


def main() -> None:
    """Tworzy pliki w każdej sekundzie"""

    while True:
        now = datetime.now()
        format_time = now.strftime("%Y-%m-%d %H:%M:%S")

        hours = now.hour
        minutes = now.minute
        seconds = now.second
        name_file = f"app-{hours}_{minutes}_{seconds}.log"

        with open(name_file, "w", encoding="utf-8") as file:
            file.write(f"{format_time}")

        print(f"{format_time} {name_file}")

        time.sleep(1)


if __name__ == "__main__":
    main()
