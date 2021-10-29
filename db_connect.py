import config
import mysql.connector


db = mysql.connector.connect(
    host=config.DB_HOST,
    user=config.DB_USER,
    password=config.DB_PASSWORD
)

if __name__ == '__main__':
    print(db)