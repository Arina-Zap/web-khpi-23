from components import *

def build_company() -> Company:
  w1d1 = Worker('director', 5000)
  w2d1 = Worker('manager', 3000)
  w3d1 = Worker('dev', 2000)
  w4d1 = Worker('qa', 1500)
  d1 = Department('d1', [w1d1, w2d1, w3d1, w4d1])

  w1d2 = Worker('director', 5500)
  w2d2 = Worker('manager', 3300)
  w3d2 = Worker('dev', 2500)
  w4d2 = Worker('qa', 1500)
  d2 = Department('d1', [w1d2, w2d2, w3d2, w4d2])

  return Company([d1, d2])


if __name__ == "__main__":
  company = build_company()
  d1 = company.get_departments()[0]
  d2 = company.get_departments()[1]
  salary_report_visitor = SalaryReportVisitor()

  components = [company, d1]
  client_code(components, salary_report_visitor)
  print("Company salary:", salary_report_visitor.get_report_company())
  print("Department d1 salary:", salary_report_visitor.get_report_department())


  components = [company, d2]
  client_code(components, salary_report_visitor)
  print("Department d2 salary:", salary_report_visitor.get_report_department())
