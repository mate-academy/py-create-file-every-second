from datetime import datetime
import time


def main() -> None:
    while True:
        current_datetime = datetime.now()
        formatted_name = current_datetime.strftime("%H_%M_%S")
        name = formatted_name.split("_")
        name_file = f"app-{name[0]}_{name[1]}_{name[2]}.log"
        file_content = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        with open(name_file, "w") as names:
            names.write(file_content)
        print(current_datetime, name_file)
        time.sleep(1)


if __name__ == "__main__":
    main()
