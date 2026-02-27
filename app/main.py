import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        present = datetime.now()
        file_name = (f"app-{present.hour}"
                     f"_{present.minute}"
                     f"_{present.second}"
                     + ".log")

        with open(file_name, "w") as file:
            file.write(str(present))
            print(str(present), file_name)

        time.sleep(1)


if __name__ == "__main__":
    main()
