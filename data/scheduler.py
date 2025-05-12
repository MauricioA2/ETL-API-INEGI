import schedule
import time
from main_etl import run_etl  

schedule.every().monday.at("08:00").do(run_etl)

while True:
    schedule.run_pending()
    time.sleep(60)
