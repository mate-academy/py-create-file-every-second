from datetime import datetime
import time
import keyboard


def main() -> None:
    while True:
        hours = datetime.now().hour
        minutes = datetime.now().minute
        seconds = datetime.now().second
        year = datetime.now().year
        mohth = datetime.now().month
        day = datetime.now().day
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        text = f"{year}-{mohth}-{day} {hours}:{minutes}:{seconds}"
        print(text, file_name)
        time.sleep(1)
        with open(file_name, "w") as file:
            file.write(text)
        if keyboard.is_pressed("esc"):
            print("Process completed")
            break


if __name__ == "__main__":
    main()
