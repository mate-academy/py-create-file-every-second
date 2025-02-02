from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        now = datetime.now()
        formatted_time = now.strftime("%H_%M_%S")
        file_name = f"app-{formatted_time}.log"

        with open(file_name, "w") as file:
            file.write(str(now))

        print(now, file_name)

        time.sleep(1)


if __name__ == "__main__":
    main()
