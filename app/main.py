import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main():
    while True:
        dt = datetime.now()
        file_name = "app-" + dt.strftime("%H_%M_%S") + ".log"
        text = dt.strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, 'w') as f:
            f.write(text)
        print(f"{text} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
