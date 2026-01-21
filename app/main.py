from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:

    def log_time(new_time: str) -> str:
        return f"app-{new_time.split()[1].replace(':', '_')}.log"

    while True:
        date_time = datetime.now().isoformat(" ", timespec="seconds")
        name_file = log_time(date_time)
        with open(name_file, "w") as file:
            file.write(date_time)
        print(f"{date_time} {name_file}")
        sleep(1)


if __name__ == "__main__":
    main()
