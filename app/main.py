from datetime import datetime
from time import sleep


def main() -> None:

    while True:
        hours = datetime.now().strftime("%H")
        minutes = datetime.now().strftime("%M")
        seconds = datetime.now().strftime("%S")
        name = f"app-{hours}_{minutes}_{seconds}.log"
        content = str(datetime.now())
        with open(name, "w") as f:
            f.write(content)
            print(f"{content} {name}")
            sleep(1)


if __name__ == "__main__":
    main()
