import os
import time
from datetime import datetime

# Ensure the folder for files exists
output_folder = "generated_files"
os.makedirs(output_folder, exist_ok=True)

try:
    while True:
        # Generate a unique filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
        filename = f"file_{timestamp}.txt"
        filepath = os.path.join(output_folder, filename)

        # Create the file and write the current timestamp into it
        with open(filepath, "w") as file:
            file.write(f"File created at: {datetime.now()}\n")

        print(f"Created file: {filename}")
        time.sleep(1)  # 1-second delay
except KeyboardInterrupt:
    print("Program stopped.")
