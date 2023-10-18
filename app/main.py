from datetime import datetime
from time import sleep


def main():
    while True:
        create_time = datetime.now()
        file_name = f"app-{create_time.hour}_{create_time.minute}_{create_time.second}.log"
        file_content = (f"{create_time.year}-{create_time.month}-{create_time.day} "
                        f"{create_time.hour}:{create_time.minute}:{create_time.second}")
        with open(file_name, "w") as f:
            f.write(file_content)

        print(f"{file_content} {file_name}")
        sleep(1)


if __name__ == "__main__":
    main()
