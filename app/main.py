import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        now = datetime.now()
        ft = now.strftime("%Y-%m-%d %H:%M:%S")
        file_name = f"app-{now.strftime("%H_%M_%S")}.log"
        with open(file_name, "w") as file:
            file.write(f"{now}")
            print(f"{ft} {file_name}")
            time.sleep(1)


if __name__ == "__main__":
    main()
