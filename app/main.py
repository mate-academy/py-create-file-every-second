from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        text = datetime.now()
        current_time = text.strftime("%H_%M_%S")
        name = "app-" + current_time + ".log"

        with open(name, "w") as f:
            f.write(str(text))
        print(f"{text} {name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
