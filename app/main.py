from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:

        now = datetime.now()
        formatted_now = now.strftime("%Y-%m-%d %H:%M:%S")
        file_name = (f"app-{now.hour}_"
                     f"{now.minute}_"
                     f"{now.second}.log")

        with open(file_name, "w") as file:

            file.write(formatted_now)
            print(formatted_now, file_name)

        sleep(1)


if __name__ == "__main__":
    main()
