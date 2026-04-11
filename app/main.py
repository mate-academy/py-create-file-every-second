from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        hour = now.hour
        minute = now.minute
        second = now.second
        file_name = f"app-{hour}_{minute}_{second}.log"
        content = now.strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "w") as f:
            f.write(content)
        print(f"{content} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
