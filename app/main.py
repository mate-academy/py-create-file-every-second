from datetime import datetime
import time


def main():
    while True:
        date_info = datetime.now()
        file_name = f"app-{date_info.hour}_{date_info.minute}" \
                    f"_{date_info.second:02d}.log"
        with open(file_name, "w") as file:
            file.write(str(date_info))
        print(f"{date_info} {file_name}")
        time.sleep(1)


if __name__ == "__main__":
    main()
