from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    # write your code here
    while True:
        current_datatime = datetime.now()

        file_name = "app-" + \
                    f"{current_datatime.hour}_" \
                    f"{current_datatime.minute}_" \
                    f"{current_datatime.second}" + \
                    ".log"

        try:
            file_obj = open(file_name, "w")
            file_obj.write(str(current_datatime))
        finally:
            if not file_obj.closed:
                file_obj.close()

        print(f"{current_datatime} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
