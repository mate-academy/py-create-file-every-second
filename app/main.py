from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    current_date = datetime.now()
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S.%f")
    file_name = "app-" + str(current_date.strftime("%H_%M_%S")) + ".log"
    with open(file_name, "a") as f:
        f.write(formatted_datetime)


if __name__ == "__main__":
    main()
