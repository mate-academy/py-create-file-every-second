from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S")
        # é um metodo que transforma esse objeto
        # datetime em uma string formatada.
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"

        with open(file_name, "w") as f:
            f.write(timestamp_str)

        print(f"{timestamp_str} {file_name}")

        sleep(1)


if __name__ == "__main__":
    main()
