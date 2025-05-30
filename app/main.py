from datetime import datetime
import time
import app.main as app_module


date_now = datetime.now()


def main() -> None:
    while True:
        date_str = app_module.datetime.now()
        time_file_name = date_str.strftime("app-%H_%M_%S")
        log_time_file = f"{time_file_name}.log"
        time_point_str = date_str.strftime("%Y-%m-%d %H:%M:%S")

        with open(log_time_file, "w") as f:
            f.write(f"{time_point_str}")

        print(f"{time_point_str} {log_time_file}")
        time.sleep(1)


if __name__ == "__main__":
    main()
