from datetime import datetime  
from time import sleep


def main() -> None:
    while True:
        timestamp = datetime.now()
        formatted_time = timestamp.strftime("%Y-%m-%d %H:%M:%S")
        filename = f"app-{timestamp.hour}_{timestamp.minute}_{timestamp.second}.log"

        with open(filename, "w") as f:
            f.write(formatted_time)

        print(f"{formatted_time} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
