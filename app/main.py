from time import sleep
from datetime import datetime

def main():
  while True:
      sleep(1)
      date = datetime.now()
      time_info = f"{datetime.now().hour}_" \
                  f"{datetime.now().minute}_" \
                  f"{datetime.now().second}"
      with open(f"{time_info}.log", "w") as log_file:
          log_file.write(f"{date}")
          print(f"file with name {time_info}.log "
                f"was created {date}")

        
if __name__ == "__main__":
  main()   
