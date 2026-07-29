from datetime import datetime
import time


def main() -> None:
    while True:
        now = datetime.now()
        hours = now.hour
        minutes = now.minute
        seconds = now.second
        year = now.year
        month = now.month
        day = now.day
        file_name = f"app-{hours:02d}_{minutes:02d}_{seconds:02d}.log"
        text = (f"{year}-{month:02d}-{day:02d} "
                f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        print(text, file_name)
        with open(file_name, "w") as file:
            file.write(text)
        time.sleep(1)
    print("Process completed")


if __name__ == "__main__":
    main()
