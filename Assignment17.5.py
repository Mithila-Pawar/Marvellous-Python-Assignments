import schedule
import time
from datetime import datetime

def write_time_to_file():
    now = datetime.now()
    with open("Marvellous.txt", "a") as f:
        f.write(now.strftime("%Y-%m-%d %H:%M:%S\n"))

schedule.every(5).minutes.do(write_time_to_file)

while True:
    schedule.run_pending()
    time.sleep(1)