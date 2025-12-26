from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        content = now.strftime("%Y-%m-%d %H:%M:%S")
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(filename, "w") as file:
            file.write(content)
        print(f"{content} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
