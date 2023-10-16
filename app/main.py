from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        system_time = datetime.now()
        filename = (f"app-{system_time.hour}_{system_time.minute}"
                    f"_{system_time.second}.log")
        with open(filename, "w") as file:
            file.write(str(system_time))
        print(f"{system_time} {filename}")
        sleep(1)


if __name__ == "__main__":
    main()
