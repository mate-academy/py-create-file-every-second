from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S").split("_")
        time_stamp = (f"{current_time[0]}-{current_time[1]}-{current_time[2]} "
                      f"{current_time[3]}:{current_time[4]}:{current_time[5]}")
        file_name = (
            f"app-{current_time[3]}_{current_time[4]}_{current_time[5]}.log"
        )
        with open(file_name, "w") as file:
            file.write(time_stamp)
            print(time_stamp, file_name)

        sleep(1)


if __name__ == "__main__":
    main()
