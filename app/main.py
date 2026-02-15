from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        time_now = (f""
                    f"app-{str(
                        datetime.now().time()
                    )[:8].replace(':', '_')}.log"
                    f"")
        with open(time_now, "w") as file:
            file.write(f"{str(datetime.now())}")
            print(f"{str(datetime.now())} {time_now}")

        sleep(1)


if __name__ == "__main__":
    main()
