from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        this_exact_moment = datetime.now()
        new_file_name = (f"app-{this_exact_moment.hour}_"
                         f"{this_exact_moment.minute}_"
                         f"{this_exact_moment.second}.log")
        with open(new_file_name, "a") as f:
            f.write(f"{this_exact_moment}")
        print(this_exact_moment, new_file_name)
        sleep(1)


if __name__ == "__main__":
    main()
