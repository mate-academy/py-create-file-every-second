from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        data = datetime.now()
        name = f"app-{data.hour}_{data.minute}_{data.second}.log"
        with open(name, "a") as file:
            date = str(data.date())
            hour = str(data.hour)
            minute = str(data.minute)
            second = str(data.second)
            save = date + " " + hour + ":" + minute + ":" + second
            file.write(save)
            print(f"{save} {name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
