import datetime
import time


def create_file_every_second():
    while True:
        file_name = 'app-' + datetime.datetime.now().strftime("%-H_%-M_%-S") + '.log'
        with open(file_name, 'w') as f:
            content = datetime.datetime.now().strftime("%Y-%m-%d %X.%f")
            f.write(content)
        time.sleep(1)
        print(file_name + " " + content)


def main():
    create_file_every_second()


if __name__ == "__main__":
    main()
