from datetime import datetime  # DO NOT CHANGE THIS IMPORT
from time import sleep

def main():
    while True:
        
        current_time = datetime.now()
        file_name = f"app-{current_time.hour}_{current_time.minute}_{current_time.second}.log"
        timestamp = current_time.strftime("%Y-%m-%d %H:%M:%S")
        with open(file_name, "w") as f:
            f.write(timestamp)
            
        sleep(1)    
        print(f"{timestamp} {file_name}")
        
        
if __name__ == "__main__":
    main()
