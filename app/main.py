from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:

    while True:
        years = datetime.now().year
        months = datetime.now().month
        dates = datetime.now().day
        hours = datetime.now().hour
        minutes = datetime.now().minute
        times = datetime.now().time()
        seconds = datetime.now().second

        file_name = f"app-{hours}_{minutes}_{seconds}"

        with open(file_name + ".log", "w") as file:

            text = f"{years}-{months}-{dates} {times}"
            file.write(text)
            print(f"{text} {file.name}")
            time.sleep(1)


if __name__ == "__main__":
    main()
