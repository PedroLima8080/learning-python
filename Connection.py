import sqlalchemy as db

class Connection:
    _connection = None;

    def __init__(self):
        connection_str = f'mysql+pymysql://root:root@localhost:3306/learning-py';
        engine = db.create_engine(connection_str);
        connection = engine.connect();
        self._connection = connection;

    def getConnection(self):
        return self._connection;