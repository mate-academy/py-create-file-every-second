from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main():
    while True:
        t = datetime.now()
        file_name = f"app-{t.hour}_{t.minute}_{t.second}.log"
        with open(file_name, "a") as f:
            f.write(str(t))
        print(f"{t} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
