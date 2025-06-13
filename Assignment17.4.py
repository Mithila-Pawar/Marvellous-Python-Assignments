import schedule
import time

def print_namskar():
    print("Namskar...")

schedule.every().day.at("09:00").do(print_namskar)

while True:
    schedule.run_pending()
    time.sleep(1)