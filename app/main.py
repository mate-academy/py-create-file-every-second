from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        name = f"app-{now.hour:02}_{now.minute:02}_{now.second:02}.log"
        content = now.strftime("%Y-%m-%d %H:%M:%S")
        with open(name, "w") as file:
            file.write(content)

        print(f"{content} {name}")
        sleep(1)


if __name__ == "__main__":
    main()
