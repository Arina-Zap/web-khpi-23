from __future__ import annotations
from abc import ABC
from components import *


class Mediator(ABC):

  def notify(self, sender: object, event: str) -> None:
    pass


class ConcreteMediator(Mediator):
  def __init__(self, pickup_in_shop: PickUpInShop, other_person: OtherPerson,
               name: NameInput, phone: PhoneInput, date: Date, time: Time) -> None:
    self._pickup_in_shop = pickup_in_shop
    self._pickup_in_shop.mediator = self

    self._other_person = other_person
    self._other_person.mediator = self

    self._name = name
    self._name.mediator = self

    self._phone = phone
    self._phone.mediator = self

    self._date = date
    self._date.mediator = self

    self._time = time
    self._time.mediator = self

  def notify(self, sender: object, event: str) -> None:
    if event == "pickup":
      self._pickup_in_shop.set_enabled(True)
      self._other_person.set_enabled(False)
      self._date.set_enabled(False)
      self._time.set_enabled(False)
      self._name.set_enabled(False)
      self._phone.set_enabled(False)
    elif event == "other_person":
      self._pickup_in_shop.set_enabled(False)
      self._date.set_enabled(True)
      self._time.set_enabled(True)
      self._name.set_enabled(True)
      self._phone.set_enabled(True)
      self._name.input_name("Arina Zaporozhets")
      self._phone.input_phone("+380984756050")
    if event == "date":
      self._time.show_time(date="25.03.2023")
      self._time.select_time(time="10am")
