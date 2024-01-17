from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    filettt = "app-{hours}_{minutes}_{seconds}.log"

    while True:
        now = datetime.now()
        formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
        file_name = filettt.format(hours=now.hour,
                                   minutes=now.minute,
                                   seconds=now.second)

        with open(file_name, "w") as f:
            f.write(formatted_time)
        print(f"{formatted_time} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
