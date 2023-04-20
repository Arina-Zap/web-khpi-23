from abc import ABC, abstractmethod
import json


class RestApi(ABC):
  def __init__(self):
    self.status = None
    self.message = None
    self.data = None
    self.response = None

  def update(self, id, data_to_change) -> None:
    self.data = self.get_data(id)
    if self.validate(data_to_change):
      self.notify()
    self.hook1()
    self.response()

  def save_data(self, response):
    return response

  def get_data(self, id):
    return self.data

  def response(self) -> None:
    self.response = {'status': self.status, 'message': self.message}
    self.save_data(self.response)
    print("AbstractClass says: But I am doing the bulk of the work anyway")

  @abstractmethod
  def validate(self, data_to_change) -> None:
    pass

  @abstractmethod
  def notify(self) -> None:
    pass

  def hook1(self) -> None:
    pass


class Product(RestApi):
  def notify(self) -> None:
    pass


class User(RestApi):
  def validate(self, data_to_change) -> bool:
    if self.data != data_to_change['email']:
      return False


class Order(RestApi):
  def response(self) -> None:
    self.response = {'status': self.status, 'message': self.message, 'json': json.dumps(self.data)}
    self.save_data(self.response)
