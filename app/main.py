from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    current_time = datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S.%f")
    file_name = (f"app-{current_time.hour}_{current_time.minute}_"
                 f"{current_time.second}.log")
    with open(file_name, "w") as f:
        f.write(formatted_time)

    with open(file_name, "r") as f:
        print(f.read())


while True:
    main()
    time.sleep(1)


if __name__ == "__main__":
    main()
