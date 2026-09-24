from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time = datetime.now()
        file_name = f"app-{time.hour}_{time.minute}_{time.second}.log"
        stamp = time.strftime("%Y-%m-%d %H:%M:%S")

        with open(file_name, "w") as timestampe_file:
            timestampe_file.write(stamp)
        print(f"{stamp} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
