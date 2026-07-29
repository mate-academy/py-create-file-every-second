import time
from datetime import datetime


def main() -> None:
    try:
        while True:
            dat_name = datetime.now()
            time.sleep(1)
            with open(f"app-{dat_name.strftime('%H')}"
                      f"_{dat_name.strftime('%M')}"
                      f"_{dat_name.strftime('%S')}.log", "w") as f:
                f.write(f"{dat_name.strftime('%Y')}-"
                        f"{dat_name.strftime('%m')}-"
                        f"{dat_name.strftime('%d')} "
                        f"{dat_name.strftime('%H')}:"
                        f"{dat_name.strftime('%M')}:"
                        f"{dat_name.strftime('%S')}")
            with open(f"app-{dat_name.strftime('%H')}"
                      f"_{dat_name.strftime('%M')}"
                      f"_{dat_name.strftime('%S')}.log", "r") as f:
                cont = f.readline()
                print(f"{cont} {f.name}")
    except KeyboardInterrupt:
        raise KeyboardInterrupt


if __name__ == "__main__":
    main()
