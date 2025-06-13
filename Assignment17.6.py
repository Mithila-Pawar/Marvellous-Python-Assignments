import schedule
import time

def print_lunch_time():
    print("Lunch Time!")

def print_wrap_up_work():
    print("Wrap up work")

schedule.every().day.at("13:00").do(print_lunch_time)
schedule.every().day.at("18:00").do(print_wrap_up_work)

while True:
    schedule.run_pending()
    time.sleep(1)