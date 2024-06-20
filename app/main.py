from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        file_name = f"app-{now.hour}_" \
                    f"{now.minute}_" \
                    f"{now.second}.log"
        with open(file_name, "w") as f:
            f.write(str(now))
        print(now, file_name)
        sleep(1)


if __name__ == "__main__":
    main()
