import sqlite3 as sl
from json import dumps, loads
from parcer.parcing_news_main import get_news_main


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
    nothing = 0

    with con:
        data = con.execute("select count(*) from sqlite_master where type='table' and name='news'")

        for row in data:
            for item in row:
                if item == nothing:
                    create_db(con)
                    return True

        cursor = con.cursor()
        cursor.execute("""SELECT * FROM news""")
        records = cursor.fetchall()

        if len(records) == nothing:
            return True

        return False


def delete_record(con):
    numbers_delete = 3
    first_item = 0

    with con:
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM news""")
        records = cursor.fetchall()

        for k in range(1, numbers_delete + 1):
            for i in range(len(records)):
                if i < numbers_delete:
                    id_news = records[i][first_item]

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
    limit = 3

    with con:
        cursor = con.cursor()
        cursor.execute("""SELECT * FROM news""")
        records = cursor.fetchall()

        for i in range(len(records)):
            if i < limit:
                id_news, name_news, first_text, link, text = records[i]
                print(id_news, name_news, first_text)
                text = loads(text)
                result.append([name_news, first_text, link, text])
            else:
                break

    return result


def main_db():
    con = sl.connect('news.db')

    if check_db(con):
        data = create_data_for_db()
        filling_db(data, con)

    result = print_db(con)

    return result


def data_db():
    con = sl.connect('news.db')
    data = create_data_for_db()
    result = [con, data]

    return result
