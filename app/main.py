import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        t_n = datetime.now()
        with open(f"app-{t_n.hour}_{t_n.minute}_{t_n.second}.log", "w") as f:
            f.write(str(t_n))
        print(t_n, f"app-{t_n.hour}_{t_n.minute}_{t_n.second}.log")
        time.sleep(1)


if __name__ == "__main__":
    main()
