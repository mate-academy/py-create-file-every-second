from datetime import datetime
from time import sleep


def main():
    while True:
        content = str(datetime.now())
        q = content.split(" ")
        x = q[1].split(".")
        hms = x[0].split(":")
        file_name = f"app-{hms[0]}_{hms[1]}_{hms[2]}.log"
        with open(file_name, "w") as f:
            f.write(content)
        with open(file_name, "r") as f:
            print(f"{f.readline()} {f.name}")
        sleep(1)


if __name__ == "__main__":
    main()
