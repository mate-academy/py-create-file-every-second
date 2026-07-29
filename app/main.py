from datetime import datetime
from time import sleep


def main():
    while True:
        date_now = datetime.now()
        info = f"app-" \
               f"{date_now.strftime('%H')}_" \
               f"{date_now.strftime('%M')}_" \
               f"{date_now.strftime('%S')}" \
               f".log"

        with open(info, "w") as f:
            content = (
                f"{date_now.strftime('%Y')}-"
                f"{date_now.strftime('%m')}-"
                f"{date_now.strftime('%d')} "
                f"{date_now.strftime('%X')}"
            )

            f.write(content)
            print(content + " " + info)
            sleep(1)


if __name__ == "__main__":
    main()
