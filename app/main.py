from datetime import datetime
from time import sleep


def main() -> None:
    while 1:
        tu = datetime.now()
        formated_t = tu.strftime("%Y-%m-%d %H:%M:%S")
        app_name = f"app-{tu.hour}_{tu.minute}_{tu.second}.log"

        with open(f"{app_name}", "w") as f:
            f.write(formated_t)

        print(formated_t, app_name)
        sleep(1)


if __name__ == "__main__":
    main()
