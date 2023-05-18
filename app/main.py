import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        timestamp = datetime.now()
        filename = (f"app-{timestamp.hour}_{timestamp.minute}"
                    f"_{timestamp.second}.log")
        with open(f"{filename}", "w+") as newfile:
            newfile.write(str(timestamp))
            newfile.seek(0)
            print(newfile.read() + f" {filename}")
            time.sleep(1)


if __name__ == "__main__":
    main()
