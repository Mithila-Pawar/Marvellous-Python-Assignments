import schedule
import time

def print_do_coding():
    print("Do Coding..!")

schedule.every(30).minutes.do(print_do_coding)

while True:
    schedule.run_pending()
    time.sleep(1)