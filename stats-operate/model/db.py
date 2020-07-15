import mysql.connector as connector


class Database:
    @staticmethod
    def connection():
        config = {
            "user": "namnt",
            "password": "123456",
            "host": "localhost",
            "port": 3306,
            "database": "bg_dsp"
        }
        try:
            c = connector.connect(**config)
            return c
        except Exception as e:
            print("connection error :" + str(e))
            exit(1)
