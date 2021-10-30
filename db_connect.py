import config
import logging
import mysql.connector


logging.basicConfig(
    filename=config.LOG_FILE,
    level=logging.DEBUG,
    format=config.LOG_FORMAT
)

db = mysql.connector.connect(
    host=config.DB_HOST,
    user=config.DB_USER,
    password=config.DB_PASSWORD,
    database=config.DB_NAME
)


def execute_sql(script):
    with open(script, 'r') as f:
        commands = f.read().split(';')[:-1]
        cursor = db.cursor()
        for command in commands:
            logging.info(command)
            cursor.execute(command)


def build_schema():
    execute_sql('schema.sql')


def drop_tables():
    execute_sql('drop_tables.sql')


def rebuild_schema():
    drop_tables()
    build_schema()


def select_all(table):
    cursor = db.cursor()
    select = 'SELECT * FROM {}'.format(table)
    logging.info(select)
    cursor.execute(select)
    result = cursor.fetchall()
    for i in result:
        print(i)


if __name__ == '__main__':
    select_all('hosts')
    select_all('scans')
    select_all('traces')
    select_all('hops')
    select_all('ipv4_addresses')
