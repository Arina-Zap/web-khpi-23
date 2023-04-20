from __future__ import annotations
from components import *


class Visitor(ABC):
  @abstractmethod
  def report_company(self, element: Company):
    pass

  @abstractmethod
  def get_report_company(self) -> int:
    pass

  @abstractmethod
  def report_department(self, element: Department):
    pass

  @abstractmethod
  def get_report_department(self) -> int:
    pass


class SalaryReportVisitor(Visitor):
  def __init__(self):
    self.report_company_ = None
    self.report_department_ = None

  def report_company(self, element, salary=0):
    departments = element.get_departments()
    for department in departments:
      workers = department.get_workers()
      for worker in workers:
        salary += worker.get_salary()

    self.report_company_ = salary

  def get_report_company(self) -> int:
    return self.report_company_

  def report_department(self, element, salary=0):
    workers = element.get_workers()
    for worker in workers:
      salary += worker.get_salary()

    self.report_department_ = salary

  def get_report_department(self) -> int:
    return self.report_department_


def client_code(components: List[Component], visitor: Visitor) -> None:
  for component in components:
    component.accept(visitor)
