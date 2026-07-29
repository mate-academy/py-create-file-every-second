import time
from datetime import datetime


def main() -> None:
    while True:
        with open(
            f"{datetime.now().strftime('app-%H_%M_%-S.log')}", "a"
        ) as log_file:
            log_file.write(f"{datetime.now()}")
            print(
                f"{datetime.now()} "
                f"{datetime.now().strftime('app-%H_%M_%-S.log')}"
            )

            time.sleep(1)


if __name__ == "__main__":
    main()
