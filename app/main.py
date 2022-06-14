from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main():
    while True:
        current_time = datetime.datetime.now()

        file_name = current_time.strftime("app-%H_%M_%S.log")
        with open(file_name, "w") as log_file:
            log_file.write(str(current_time))

        print(current_time, file_name)
        time.sleep(1)


if __name__ == "__main__":
    main()
