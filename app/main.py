from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        data_inside = datetime.now().time()
        name_file = (datetime.now())
        sleep(1 - data_inside.microsecond / 1_000_000)
        data_inside = str(data_inside).replace(":", "_")
        print(f"{name_file} app-{data_inside}.log")

        with open(f"app-{data_inside}.log", "w") as f:
            f.write(f"{name_file}")


if __name__ == "__main__":
    main()
