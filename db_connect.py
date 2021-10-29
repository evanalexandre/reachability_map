import config
import mysql.connector


db = mysql.connector.connect(
    host=config.DB_HOST,
    user=config.DB_USER,
    password=config.DB_PASSWORD,
    database=config.DB_NAME
)

def build_schema():
    with open('schema.sql', 'r') as f:
        commands = f.read().split(';')
        print(commands)
        cursor = db.cursor()
        for command in commands:
            cursor.execute(command)


def read_scans():
    cursor = db.cursor()
    select = 'SELECT * FROM scans'
    cursor.execute(select)
    result = cursor.fetchall()
    for i in result:
        print(i)


if __name__ == '__main__':
    read_scans()
