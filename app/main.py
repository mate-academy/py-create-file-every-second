from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        name = datetime.now().strftime("%H:%M:%S").split(":")
        name_f = f"app-{name[0]}_{name[1]}_{name[2]}.log"

        with open(name_f, "w") as f:
            f.write(str(datetime.now()))
            print(datetime.now(), name_f)

        time.sleep(1)


if __name__ == "__main__":
    main()
