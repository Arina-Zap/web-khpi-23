class Database:
  __instance = None

  def __init__(self, db_type):
    if Database.__instance != None:
      raise Exception("This class is a singleton!")
    elif db_type == 'pgsql':
      Database.__instance = PgSQL()
      # do something
      print('This is pgsql database.')
    elif db_type == 'mongodb':
      Database.__instance = MongoDB()
      # do something
      print('This is mongodb database.')

  @staticmethod
  def getInstance(db_type):
    if Database.__instance is None:
      Database.__instance = Database(db_type)
    return Database.__instance._connection


class MongoDB:
  _connection = None
  def __init__(self):
    pass

  def connect(self):
    pass


class PgSQL:
  _connection = None
  def __init__(self):
    pass

  def connect(self):
    pass


if __name__ == "__main__":
  pgsql_db = Database("pgsql")
  mongo_db = Database("mongodb")

