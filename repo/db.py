from mysql import connector

from models.city import City

SELECT_ALL = 'select * from weather.cities'
SHOW_DATABASES = 'show databases'


def get_db():
    return connector.connect(user='root', password='password',
                             host='localhost')


def get_cursor(conn):
    if conn:
        return conn.cursor()


def close_connection(conn):
    if conn:
        conn.close()


def get_all_records():
    result = {}
    try:
        with get_db() as conn:
            cursor = get_cursor(conn)
            cursor.execute(SELECT_ALL)
            count = 0;

            for i in cursor:
                count += 1
                result[count] = i
    except Exception as e:
        print(f'Exception in get_all_records :{e}')
    finally:
        close_connection(conn)
    return result


def create_weather_table():
    try:
        with get_db() as conn:
            cursor = get_cursor(conn)
            cursor.execute('create table weather.cities (city varchar(100), state varchar(100))')
            print(cursor)
    except Exception as e:
        print(f'Exception in create_weather_table: {e}')
    finally:
        close_connection(conn)


def insert_city(city: City):
    try:
        with get_db() as conn:
            cursor = get_cursor(conn)
            cursor.execute(f'insert into weather.cities (city, state) values (\'{city.name}\', \'{city.state}\')')
            print(cursor)
    except Exception as e:
        print(f'Exception in insert_city: {e}')
    finally:
        close_connection(conn)
