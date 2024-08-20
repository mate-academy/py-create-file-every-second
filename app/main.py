from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        timing = str(datetime.now()).split()
        exact_time = timing[1]
        dot_index = exact_time.find(".")
        exact_time_sliced = exact_time if dot_index == - 1 \
            else exact_time[:dot_index]
        exact_time_split = exact_time_sliced.split(":")
        hours = exact_time_split[0]
        minutes = exact_time_split[1]
        seconds = exact_time_split[2]
        final_time = f"{hours}_{minutes}_{seconds}"
        file_name = f"app-{final_time}.log"
        with open(file_name, "w") as file:
            file.write(str(datetime.now()))
        print(datetime.now(), file_name)
        sleep(1)


if __name__ == "__main__":
    main()
