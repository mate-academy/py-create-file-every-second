from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        try:
            now = datetime.now()

            file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
            content = str(now.strftime("%Y-%m-%d %H:%M:%S"))

            with open(file_name, "w") as document:
                document.write(content)

            print(f"{content} {file_name}")

            sleep(1)

        except KeyboardInterrupt:
            raise


if __name__ == "__main__":
    main()
