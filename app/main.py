import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        data_time = datetime.now()
        file_name = (f"app-{data_time.hour}"
                     f"_{data_time.minute}_{data_time.second}.log")
        with open(file_name, "w") as f:
            context = data_time.strftime("%Y-%m-%d %H:%M:%S")
            f.write(context)
        print(f"{context} {file_name}")

        time.sleep(1)


if __name__ == "__main__":
    main()
