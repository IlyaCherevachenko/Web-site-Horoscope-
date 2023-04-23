from scripts.db_for_news import create_db
import schedule
from time import sleep
from pytz import timezone


con, data = create_db.data_db()
tz = timezone('Europe/Moscow')

schedule.every().day.at('00:00', tz).do(create_db.filling_db, data, con)
schedule.every().day.at('00:00', tz).do(create_db.delete_record, con)


while True:
    delay = 1

    try:
        schedule.run_pending()
        sleep(delay)

    except KeyboardInterrupt:
        break
