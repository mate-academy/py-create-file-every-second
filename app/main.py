from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        name = (f"app-{datetime.now().hour}"
                f"_{datetime.now().minute}"
                f"_{datetime.now().second}.log")
        context = str(datetime.now())
        with open(name, "w") as f:
            f.write(context)
        print(context, name)
        sleep(1)


if __name__ == "__main__":
    main()
