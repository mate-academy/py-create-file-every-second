from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:

        try:
            current_time = datetime.now()
            file_name = (
                f'app-{current_time.strftime("%H_%M_")}'
                f"{current_time.second}.log"
            )

            with open(file_name, "w") as my_file:
                my_file.write(str(current_time.replace(microsecond=0)))

            with open(file_name, "r") as my_file:
                print(my_file.read(), file_name)

            sleep(1)
        except KeyboardInterrupt:
            raise KeyboardInterrupt("Process finished by the user.")
            break


if __name__ == "__main__":
    main()
