from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main():
    while True:
        now = datetime.now()
        app_name = f"app-{now.hour}_{now.minute}"\
                   f"_{now.second}.log"
        with open(app_name, "w") as app:
            app.write(f"{now}")
        sleep(1)
        print(now, app_name)


if __name__ == "__main__":
    main()
