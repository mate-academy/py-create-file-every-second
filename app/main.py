from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from pathlib import Path
import time

BASE_DIR = Path(__file__).resolve().parent


def main() -> None:
    try:
        while True:
            c_date = datetime.now()
            file_route = f" app-{c_date.hour}-{c_date.minute}-"
            file_route += f"{c_date.second}.log"
            print(c_date.strftime("%Y-%m-%d %H:%M:%S") + file_route)
            write_file = open(BASE_DIR / file_route, "w")
            write_file.write(c_date.strftime("%Y-%m-%d %H:%M:%S"))
            write_file.close()
            time.sleep(1)
    except KeyboardInterrupt:
        print("Programa finalizado")


if __name__ == "__main__":
    main()
