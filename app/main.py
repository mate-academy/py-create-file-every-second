from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        f_name = (f"app-"
                  f"{datetime.now().hour}_"
                  f"{datetime.now().minute}_"
                  f"{datetime.now().second}.log")
        t_file = open(f"{f_name}", "w")
        c_time = datetime.now()
        formatted_time = c_time.strftime("%Y-%m-%d %H:%M:%S")
        t_file.write(formatted_time)
        print(f"{formatted_time} {f_name}")
        t_file.close()
        sleep(1)


if __name__ == "__main__":
    main()
