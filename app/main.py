from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep


def main() -> None:
    while True:
        doom = datetime.now()
        scorpion = doom.strftime("%Y-%m-%d %H:%M:%S")
        name = f"app-{doom.hour}_{doom.minute}_{doom.second}.log"
        with open(name, "w") as x:
            x.write(f"{scorpion}")
            print(f"{scorpion} {name}")
        sleep(1)


if __name__ == "__main__":
    main()
