from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        replaced_date = str(datetime.now()).replace(":", " ")
        second_raplace = replaced_date.replace("-", " ")
        full_replaced = second_raplace.replace(".", " ")
        date = full_replaced.split(" ")
        if date != []:
            file_name = f"app-{date[3]}_{date[4]}_{date[5]}.log"
        with open(file_name, "w") as f:
            f.write(f"{str(datetime.now())}")
        with open(file_name, "r") as file:
            content = file.read().strip()
        print(f"{content} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
