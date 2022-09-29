from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main():
    while True:
        t = datetime.now()
        ti = str(t).split()[1]
        ti = ti.replace(":", "_")

        file_name = "app-" + ti[0:8] + ".log"
        with open(file_name, "w") as f:
            f.write(str(t))
        with open(file_name, "r") as f:
            print(f.read(), file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
