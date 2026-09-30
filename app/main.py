from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:

        now = datetime.now()
        hours = now.strftime("%H")
        minutes = now.strftime("%M")
        seconds = now.strftime("%S")

        file_name = f"app-{hours}_{minutes}_{seconds}.log"

        text = f"{now.date()} {now.strftime('%H:%M:%S')}"
        with open(file_name, "w") as f:
            f.write(text)
        print(text, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
