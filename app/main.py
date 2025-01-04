import time


def create_file() -> None:
    while True:
        c_time = time.localtime()
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S.%f", c_time)
        file_name = f"app-{c_time.tm_hour}_{c_time.tm_min}_{c_time.tm_sec}.log"
        with open(file_name, "w") as f:
            f.write(timestamp)
        print(f"{timestamp} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    create_file()
