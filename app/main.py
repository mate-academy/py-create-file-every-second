from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        try:
            op_time_stamp = datetime.now()
            op_hour = format(op_time_stamp.hour)
            op_min = format(op_time_stamp.minute)
            op_sec = format(op_time_stamp.second)
            time_stamp_str = f"{op_hour}_{op_min}_{op_sec}.log"
            file_name = "app-" + time_stamp_str
            file_instance = open(file_name, "w")
            file_instance.write(str(op_time_stamp))
            file_instance.close()
            print(f"{op_time_stamp} {file_name}")
            sleep(1)
        except KeyboardInterrupt:
            raise KeyboardInterrupt


if __name__ == "__main__":
    main()
