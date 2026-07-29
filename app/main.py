from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        n_time = datetime.now()
        with open(f"app-{n_time.hour}_"
                  f"{n_time.minute}_"
                  f"{n_time.second}.log", "w") as file:
            file.write(str(n_time))
            print(n_time, file.name)
            sleep(1)


if __name__ == "__main__":
    main()
