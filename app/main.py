from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    try:
        while True:
            maintenant = datetime.now()
            d_format = maintenant.strftime("%Y-%m-%d %H:%M:%S")
            name = "app-" + maintenant.strftime("%H_%M_%S") + ".log"

            with open(name, "w", encoding="utf8") as file:
                file.write(d_format)

            print(d_format, end=" ")
            print(name)
            time.sleep(1)

    except KeyboardInterrupt:
        raise


if __name__ == "__main__":
    main()
