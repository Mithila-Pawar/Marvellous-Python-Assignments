import schedule
import time

def print_jay_ganesh():
    print("Jay Ganesh...")

schedule.every(2).seconds.do(print_jay_ganesh)

while True:
    schedule.run_pending()
    time.sleep(1)