import time


def do_something():
    print('процесс идет')
    time.sleep(2)

fl = True

try:
    while fl:
        do_something()
except KeyboardInterrupt:
    print('Вы нажали Ctrl+C, процесс завершен.')
    fl = False