import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        now = datetime.now()
        text = now.strftime("%Y-%m-%d %H:%M:%S")
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        print(f"{text} {file_name}", flush=True)
        with open(file_name, "w") as file:
            file.write(text)   #
        time.sleep(1)


if __name__ == "__main__":
    main()
