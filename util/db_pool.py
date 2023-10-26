from dbutils.pooled_db import PooledDB
import pymysql


class Database:
    def __init__(self):
        self.pool = None

    def connect(self):
        if not self.pool:
            self.pool = PooledDB(
                creator=pymysql,
                maxconnections=10,  # 设置最大连接数
                host='111.231.16.72',
                port=3306,
                user='root',
                password='123456',
                database='temp_exp',
                charset='utf8mb4'
            )

    def get_connection(self):
        return self.pool.connection()