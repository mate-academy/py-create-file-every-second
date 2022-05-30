import datetime
import time


def main():
    while True:
        now = datetime.datetime.now()
        file_name = "app-"\
                    f"{now.strftime('%H')}_" \
                    f"{now.strftime('%M')}_" \
                    f"{now.strftime('%S')}" + \
                    ".log"
        with open(file_name, "w") as f:
            content = (
                f"{now.strftime('%Y')}-"
                f"{now.strftime('%m')}-"
                f"{now.strftime('%d')} "
                f"{now.strftime('%X')}"
            )

            f.write(content)
            print(content + " " + file_name)
            time.sleep(1)
