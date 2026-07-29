import time
from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main() -> None:
    while True:
        content = datetime.now()
        name = f"app-{content.hour}_{content.minute}_{content.second}.log"
        with open(name, "w") as file:
            file.write(str(content))
            print(content, name)
            time.sleep(1)
