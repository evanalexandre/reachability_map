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
        

def show_tables():
    cursor = db.cursor()
    cursor.execute('SHOW TABLES')
    for i in cursor:
        print(i)


if __name__ == '__main__':
    build_schema()
    show_tables()