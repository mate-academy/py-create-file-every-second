from datetime import datetime
import time


def main():
    while True:
        file_name = f"app-{datetime.now().hour}_" \
                    f"{datetime.now().minute}_{datetime.now().second}.log"
        line = str(datetime.now())
        with open(file_name, 'w') as f:
            f.write(line)
            print(line, end=" ")
            print(file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
