from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        n_time = datetime.now()
        file_name = f"app-{n_time.hour}_{n_time.minute}_{n_time.second}.log"
        with open(file_name, "w") as file:
            file.write(str(n_time))
        print(f"{n_time} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
