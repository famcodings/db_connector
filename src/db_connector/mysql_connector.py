import MySQLdb


class MySqlDBConnector:

    def __init__(self, user, password, host, database):
        self.db_credentials = {
            'user': user,
            'passwd': password,
            'host': host,
            'db': database,
        }
        self.connect()
    

    def connect(self):
        self.connection = MySQLdb.connect(**self.db_credentials)
        self.db_cursor = self.connection.cursor(MySQLdb.cursors.DictCursor)
    

    def fetch_all(self, query, params):
        if not self.connection.open:
            self.connect()
        self.db_cursor.execute(query, params)
        result = self.db_cursor.fetchall()
        return result
    

    def fetch_one(self, query, params):
        if not self.connection.open:
            self.connect()
        self.db_cursor.execute(query, params)
        result = self.db_cursor.fetchone()
        return result
    

    def close(self):
        self.connection.close()
    

    def __del__(self):
        self.close()