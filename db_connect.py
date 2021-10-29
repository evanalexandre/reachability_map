import config
import mysql.connector


db = mysql.connector.connect(
    host=config.DB_HOST,
    user=config.DB_USER,
    password=config.DB_PASSWORD,
    database=config.DB_NAME
)


def execute_sql(script):
    with open(script, 'r') as f:
        commands = f.read().split(';')
        print(commands)
        cursor = db.cursor()
        for command in commands:
            cursor.execute(command)


def build_schema():
    execute_sql('schema.sql')


def drop_tables():
    execute_sql('drop_tables.sql')


def rebuild_schema():
    drop_tables()
    build_schema()


def read_scans():
    cursor = db.cursor()
    select = 'SELECT * FROM scans'
    cursor.execute(select)
    result = cursor.fetchall()
    for i in result:
        print(i)


if __name__ == '__main__':
    rebuild_schema()
    read_scans()
