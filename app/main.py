from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        current_date = datetime.now()
        formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
        hours = current_date.hour
        minutes = current_date.minute
        seconds = current_date.second
        file_name = f"app-{hours}_{minutes}_{seconds}.log"

        print(formatted_date + " " + file_name)

        with open(file_name, "w") as text_file:
            text_file.write(str(formatted_date))

        time.sleep(1)


if __name__ == "__main__":
    main()
