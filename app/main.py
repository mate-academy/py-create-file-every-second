from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        sleep(1)
        now = datetime.now()
        content = now.strftime("%Y-%m-%d %H:%M:%S")
        filename = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(filename, "w") as file:
            file.write(f"{content}")
        print(f"{content} {filename}")


if __name__ == "__main__":
    main()
