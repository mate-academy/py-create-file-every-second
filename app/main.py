from datetime import datetime
import time


def main():
    while True:
        time.sleep(1)
        t = datetime.now()
        with open(f'app-{t.hour}_{t.minute}_{t.second}.log', 'w') as f:
            f.write(str(t))
            print(f'File {f.name} created at {str(t)}')
