import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:

    while True:
        name = f"app-{datetime.now().time().hour}_" \
               f"{datetime.now().time().minute}_" \
               f"{datetime.now().time().second}.log"
        content = f"{datetime.now()}"

        with open(name, "w") as file:
            file.write(content)
            print(f"{content} {name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
