import schedule
import time
from datetime import datetime

def display_datetime():
    now = datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

schedule.every(1).minutes.do(display_datetime)

while True:
    schedule.run_pending()
    time.sleep(1)