import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        time_now = datetime.now()
        app = "_".join(time_now.strftime("%X").split(":"))
        file_name = f"app-{app}.log"
        with open(file_name, "w") as f:
            f.write(str(time_now))
        print(time_now, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
