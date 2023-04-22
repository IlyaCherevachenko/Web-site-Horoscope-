import sqlite3 as sl
from Goroskop.parcer.parcing_news_main import get_news_main
from json import dumps, loads
import schedule


def create_db(con):
    with con:
        con.execute("""
            CREATE TABLE news (
               id_news INTEGER PRIMARY KEY AUTOINCREMENT,
               name_news TEXT ,
               first_text TEXT,
               image_link TEXT,
               text TEXT
            );
        """)


def check_db(con):
    with con:
        data = con.execute("select count(*) from sqlite_master where type='table' and name='news'")

        for row in data:
            for item in row:
                if item == 0:
                    create_db(con)
                    return True

        cursor = con.cursor()
        cursor.execute("""SELECT * FROM news""")
        records = cursor.fetchall()

        if len(records) == 0:
            return True

        return False


def delete_record(con):
    numbers_delete = 3

    with con:
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM news""")
        records = cursor.fetchall()

        for k in range(1, numbers_delete + 1):
            for i in range(len(records)):
                if i < numbers_delete:
                    id_news = records[i][0]

                    delete_data = f"""DELETE FROM news WHERE id_news = {id_news}"""
                    cursor.execute(delete_data)
                    con.commit()


def create_data_for_db():
    result = get_news_main()
    limits = 3
    data = []

    for i in range(limits):
        name, first_text, link_img, text = result[i]
        text = dumps(text)
        data.append((name, first_text, link_img, text))

    return data


def filling_db(data, con):
    sql = 'INSERT INTO news (name_news, first_text, image_link, text) values(?, ?, ?, ?)'
    with con:
        con.executemany(sql, data)


def print_db(con):
    result = []

    with con:
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM news""")
        records = cursor.fetchall()

        print("Всего строк:  ", len(records))
        print("Вывод каждой строки")

        for row in records:
            id_news, name_news, first_text, link, text = row
            text = loads(text)
            result.append([name_news, first_text, link, text])

    return result


def main_db():
    con = sl.connect('scripts/db_for_news/news.db')

    if check_db(con):
        data = create_data_for_db()
        filling_db(data, con)

    result = print_db(con)

    return result


def done_script():
    con = sl.connect('scripts/db_for_news/news.db')
    data = create_data_for_db()
    schedule.every(20).seconds.do(delete_record, con)
    schedule.every(10).seconds.do(filling_db, data, con)
