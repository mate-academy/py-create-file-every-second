from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main(number_of_files: int | None = None) -> None:
    files_created = 0
    while True:
        now = datetime.now()
        hours = now.strftime("%H")
        minutes = now.strftime("%M")
        seconds = now.strftime("%S")
        # file name
        file_name = f"app-{hours}_{minutes}_{seconds}.log"
        time_stamp = now.strftime("%Y-%m-%d %H:%M:%S")

        try:
            with open(file_name, "w") as file:
                file.write(time_stamp)
            print(f"{time_stamp} {file_name}")
            files_created += 1
        except Exception as e:
            print(f"Помилка при відкритті файлу: {e}")

        time.sleep(1)

        if number_of_files is not None and files_created >= number_of_files:
            break


if __name__ == "__main__":
    main()
