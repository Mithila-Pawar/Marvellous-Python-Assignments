import schedule
import time

def check_email():
    print("Checking mail...")

schedule.every(10).seconds.do(check_email)

while True:
    schedule.run_pending()
    time.sleep(1)