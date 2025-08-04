from datetime import datetime  # DO NOT CHANGE THIS IMPORT


def main():
    while True:
        time = datetime.now().split(":")
        file_name = f"app-{time[0][-2,-1]}_{time[1]}_{time[2]}.log"
        with open(f"file_name", "w") as f:
            f.write(datetime.now())
            print(datetime.now(), file_name)



if __name__ == "__main__":
    main()
