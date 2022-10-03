from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main():
    while True:
        full_time_now = datetime.now()
        file_name = f"app-{full_time_now.hour}_{full_time_now.minute}" \
                    f"_{full_time_now.second}.log"
        with open(file_name, "w") as f:
            f.write(str(file_name))
        print(full_time_now, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
