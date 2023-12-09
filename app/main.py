import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        file_cteate()
        time.sleep(1)

def file_cteate() -> None:
    dt = datetime.now()
    hours = dt.hour
    minutes = dt.minute
    seconds = dt.second
    current = f"app-{hours}_{minutes}_{seconds}.log"

    with open(current, "w") as file:
        file.write(str(dt))
        print(f"{dt} {current}")

if __name__ == "__main__":
    main()
