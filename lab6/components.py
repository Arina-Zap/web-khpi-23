from abc import ABC, abstractmethod
from typing import List
from visitors import *


class Component(ABC):
  @abstractmethod
  def accept(self, visitor: Visitor):
    pass


class Worker:
  def __init__(self, title: str, salary: int):
    self.title = title
    self.salary = salary

  def get_title(self) -> str:
    return self.title

  def get_salary(self) -> int:
    return self.salary


class Department(Component):
  def __init__(self, name: str, workers: List[Worker]):
    self.workers = workers
    self.name = name

  def accept(self, visitor: Visitor):
    visitor.report_department(self)

  def get_name(self) -> str:
    return self.name

  def get_workers(self) -> List[Worker]:
    return self.workers


class Company(Component):
  def __init__(self, departments: List[Department]):
    self.departments = departments

  def accept(self, visitor: Visitor):
    visitor.report_company(self)

  def get_departments(self) -> List[Department]:
    return self.departments

