from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main():
    while True:
        t = str(datetime.now())
        ti = t.split()[1].replace(':', '_')[:8]
        file_name = f'app-{ti}.log'

        with open(file_name, 'w') as f:
            f.write(t)

        with open(file_name, 'r') as f:
            print(f.read(), file_name)

        time.sleep(1)


if __name__ == "__main__":
    main()
