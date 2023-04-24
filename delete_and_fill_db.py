import create_db
import schedule
from time import sleep
from pytz import timezone


con, data = create_db.data_db()

time_delete = '00:00'
time_filling = "00:00"
tz = timezone('Europe/Moscow')

schedule.every().day.at(time_filling, tz).do(create_db.filling_db, data, con)
schedule.every().day.at(time_delete, tz).do(create_db.delete_record, con)


while True:
    delay = 1

    try:
        schedule.run_pending()
        sleep(delay)

    except KeyboardInterrupt:
        break
