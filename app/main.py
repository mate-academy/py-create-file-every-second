from datetime import datetime
from time import sleep


def main():
    while True:
        info_date = str(datetime.now())
        with open(f"app-{info_date[11:13]}_"
                  f"{info_date[14:16]}_{info_date[17:19]}.log", "w") as f:
            f.write(info_date)
        print(info_date, end=" ")
        print(f"app-{info_date[11:13]}_{info_date[14:16]}"
              f"_{info_date[17:19]}.log")
        sleep(1)


if __name__ == "__main__":
    main()
