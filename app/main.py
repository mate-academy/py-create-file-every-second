from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        momentum = f"{datetime.now()}"
        file_name_start, file_name_end = "app-", ".log"
        file_name_mid = list()
        for elem in momentum.split()[1].split(".")[0].split(":"):
            file_name_mid.append(elem)
        file_name = (
            file_name_start + "_".join(file_name_mid) + file_name_end
        )

        with open(file_name, "w") as f:
            f.write(momentum)
            print(momentum, file_name)
            sleep(1)


if __name__ == "__main__":
    main()
