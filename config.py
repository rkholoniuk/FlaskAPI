import os
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = {
    'drivername': 'sqlite',
    'database': os.path.join(basedir, 'test.db')
}

# DATABASE_SQL = {
#     'drivername': 'mysql',
#     'host': 'localhost',
#     'port': '3306',
#     'username': 'root',
#     'password': '',
#     'database': 'test_db'
# }