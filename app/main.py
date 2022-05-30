from datetime import datetime
from time import sleep


def main():
    while True:
        sleep(1)
        t = datetime.now()
        with open(f'app-{t.hour}_{t.minute}_{t.second}.log', 'w') as f:
            f.write(str(t))
            print(f.name, str(t))

main()
