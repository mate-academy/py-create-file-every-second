from datetime import datetime
import time


def main() -> None:
    while True:
        data = datetime.now()
        file_name = f"app-{data.hour}_{data.minute}_{data.second}.log"

        with open(file_name, "w") as f:
            f.write(str(data))

        print(f"{str(data)} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
