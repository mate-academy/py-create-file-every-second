from datetime import datetime  # DO NOT CHANGE THIS IMPORT
import time


# def main():
#     output = []
#     while True:
#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         filename = f"app-{datetime.now().strftime('%H_%M_%S')}.log"
#         output.append(f"{timestamp} {filename}")
#         print(*output)
#         with open(filename, "w") as f:
#             f.write(timestamp)
#         time.sleep(1)

def main() -> None:
    output = []
    while True:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        filename = f"app-{datetime.now().strftime("%H_%M_%S")}.log"
        output.append(f"{timestamp} {filename}")
        print(output[-1])  # Виводимо тільки останній рядок, доданий до списку
        with open(filename, "w") as f:
            f.write(timestamp)
        time.sleep(1)


if __name__ == "__main__":
    main()
