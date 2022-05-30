from datetime import datetime
import time


def main():
    while True:
        t = datetime.now().time()
        text = datetime.now()
        file_name = f"app-{t.hour}_{t.minute}_{t.second}.log"
        with open(file_name, "w") as file:
            file.write(str(text))
        time.sleep(1)


if __name__ == "__main__":
    main()
