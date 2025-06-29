from datetime import datetime
import time


def main() -> None:
    try:
        while True:
            now = datetime.now()
            hours = now.hour
            minutes = now.minute
            seconds = now.second
            year = now.year
            month = now.month
            day = now.day
            file_name = f"app-{hours}_{minutes}_{seconds}.log"
            text = (f"{year}-{month}-{day} "
                    f"{hours}:{minutes}:{seconds}")
            print(text, file_name)
            with open(file_name, "w") as file:
                file.write(text)
                time.sleep(1)
    except KeyboardInterrupt:
        print("Process completed")


if __name__ == "__main__":
    main()
