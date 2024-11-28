import time
from datetime import datetime


def main() -> None:
    dat_name = datetime.now()
    while True:
        time.sleep(1)
        with open(f"app-{dat_name.strftime('%H')}"
                  f"_{dat_name.strftime('%M')}"
                  f"_{dat_name.strftime('%S')}.log", "a") as f:
            f.write(f"{dat_name.strftime('%Y')}-"
                    f"{dat_name.strftime('%m')}-"
                    f"{dat_name.strftime('%d')} "
                    f"{dat_name.strftime('%H')}:"
                    f"{dat_name.strftime('%M')}:"
                    f"{dat_name.strftime('%S')}."
                    f"{dat_name.strftime('%f')}")


if __name__ == "__main__":
    main()
