from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:

        this_moment = datetime.now()
        file_name = (f"app-{this_moment.hour}_"
                     f"{this_moment.minute}_"
                     f"{this_moment.second}.log")
        with open(file_name, "w") as current_file:
            current_file.write(str(this_moment))
        print(this_moment, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
