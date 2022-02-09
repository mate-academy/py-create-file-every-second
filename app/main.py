import datetime
import time


def create_file_every_second():
    while True:
        time_now = datetime.datetime.now()
        file_name = f"app-{time_now.strftime('%-H_%-M_%-S')}.log"
        with open(file_name, 'w') as moment_file:
            content = time_now.strftime("%Y-%m-%d %X.%f")
            moment_file.write(content)
        time.sleep(1)
        print(file_name, content)


def main():
    create_file_every_second()


if __name__ == "__main__":
    main()
