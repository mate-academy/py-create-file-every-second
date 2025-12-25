from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        t_naw = datetime.now()
        name_file = f"app-{t_naw.hour}_{t_naw.minute}_{t_naw.second}.log"
        date_time = datetime.now()
        with open(name_file, "w") as fil:
            fil.write(str(date_time))
        print(f"{date_time} {name_file}")
        time.sleep(1)


if __name__ == "__main__":
    main()
