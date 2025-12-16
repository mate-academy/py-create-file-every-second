from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        now = datetime.now()
        name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        file_content = f"{now.date()} {now.time()}"
        with open(name, "w") as f:
            f.write(file_content)

        print(file_content, name)
        sleep(1)


if __name__ == "__main__":
    main()
