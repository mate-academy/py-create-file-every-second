from datetime import datetime
from time import sleep


def main() -> None:
    while True:
        current_time = datetime.now()
        file_and_content = (f"app-{int(current_time.hour)}_"
                            f"{int(current_time.minute)}_"
                            f"{int(current_time.second)}"
                            )
        times_date = current_time.strftime("%Y-%m-%d %H:%M:%S")
        with open(f"{file_and_content}.log", "w") as f:
            f.write(times_date)
        print(f"{times_date} {file_and_content}")
        sleep(1)


if __name__ == "__main__":
    main()
