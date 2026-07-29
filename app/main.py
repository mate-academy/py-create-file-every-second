import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        filename = datetime.now().strftime("%Y-%m-%d %H:%M:%S "
                                           "app-%H_%M_%S.log")
        short_name = filename.split()[-1]
        parts = filename.split()
        first_two = parts[0:2]
        write_info = " ".join(first_two)
        with open(short_name, "w") as f:
            f.write(f"{write_info}")

        print(filename)

        time.sleep(1)


if __name__ == "__main__":
    main()
