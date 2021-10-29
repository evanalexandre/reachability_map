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
        commands = f.read()
        print(commands)
        

if __name__ == '__main__':
    build_schema()