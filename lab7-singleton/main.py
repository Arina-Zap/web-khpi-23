class Database:
  __instance = None

  def __init__(self, db_type):
    if db_type == 'pgsql':
      #do something
      print('This is pgsql database.')
    elif db_type == 'mongodb':
      #do something
      print('This is mongodb database.')

  @staticmethod
  def getInstance(db_type):
    if Database.__instance == None:
      Database.__instance = Database(db_type)
    return Database.__instance

