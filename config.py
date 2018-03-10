#encoding:utf-8
import os

DEBUG = True

SECRET_KEY = os.urandom(24)

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'blog_demo'
USERNAME = 'root'
PASSWORD = 'root'
DB_URL = 'mysql+mysqldb://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,
                                                              PORT,DATABASE)

SQLALCHEMY_DATABASE_URL = DB_URL