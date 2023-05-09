from __future__ import annotations
from abc import ABC, abstractmethod


class QueryBuilder(ABC):

  @abstractmethod
  def select(self, table, columns) -> QueryBuilder:
    pass

  @abstractmethod
  def where(self, column, operator, value) -> QueryBuilder:
    pass

  @abstractmethod
  def limit(self, limit) -> QueryBuilder:
    pass

  @abstractmethod
  def getSQL(self) -> str:
    pass


class PostgreSQLQueryBuilder(QueryBuilder):
  __query = None

  def select(self, table, columns) -> QueryBuilder:
    self.__query = 'select ' + ', '.join(columns) + ' from ' + table
    return self

  def where(self, column, operator, value) -> QueryBuilder:
    self.__query += ' where ' + column + ' ' + operator + ' ' + value
    return self

  def limit(self, limit) -> QueryBuilder:
    self.__query += ' limit ' + str(limit)
    return self

  def getSQL(self) -> str:
    return self.__query


class MySQLQueryBuilder(QueryBuilder):
  __query = None

  def select(self, table, columns) -> QueryBuilder:
    self.__query = 'select ' + ', '.join(columns) + ' from ' + table
    return self

  def where(self, column, operator, value) -> QueryBuilder:
    self.__query += ' where ' + column + ' ' + operator + ' ' + value
    return self

  def limit(self, limit) -> QueryBuilder:
    self.__query += ' limit ' + str(limit)
    return self

  def getSQL(self) -> str:
    return self.__query


if __name__ == "__main__":
  postgres_query_builder = PostgreSQLQueryBuilder()
  sql = postgres_query_builder \
    .select("users", ['id', 'name', 'email']) \
    .where('name', '=', "John") \
    .limit(10).getSQL()
  print(sql)

  print("\n")

  my_sql_query_builder = PostgreSQLQueryBuilder()
  sql = my_sql_query_builder \
    .select("users", ['id', 'name', 'email']) \
    .where('name', '=', "John") \
    .limit(10).getSQL()
  print(sql)
