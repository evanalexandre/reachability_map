import config
import mysql.connector


db = mysql.connector.connect(
    host=config.DB_HOST,
    user=config.DB_USER,
    password=config.DB_PASSWORD,
    database=config.DB_NAME
)


if __name__ == '__main__':
    cursor = db.cursor()
    cursor.execute('SHOW TABLES')
    for i in cursor:
        print(i)