from datetime import datetime
from time import sleep


def app_for_creation_file_every_second():

    while True:
        sleep(1)

        now = datetime.now()
        file_name = f"app-{now.hour}_{now.minute}_{now.second}.log"
        with open(file_name, "w") as file:
            file.write(str(now))

        print(f"{now}, {file_name}")


app_for_creation_file_every_second()
