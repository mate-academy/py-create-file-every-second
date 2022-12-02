from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        data = datetime.now()
        filename = f"app-{data.strftime('%H')}_" \
                   f"{data.strftime('%M')}_" \
                   f"{data.strftime('%S')}.log"
        with open(filename, "w") as f:
            f.write(str(data))
            print(f"{data} {filename}")
            sleep(1)


if __name__ == "__main__":
    main()
