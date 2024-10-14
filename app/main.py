from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


def main() -> None:
    while True:
        current_date = datetime.now()
        h_m_s_time = current_date.strftime("%H_%M_%S")
        file_name = f"app-{h_m_s_time}.log"
        with open(file_name, "w") as f:
            f.write(str(current_date))
            time.sleep(1)
            print(current_date, file_name)


if __name__ == "__main__":
    main()
