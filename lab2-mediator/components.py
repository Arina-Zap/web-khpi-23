from __future__ import annotations
from mediator import *


class WebComponent:

  def __init__(self, mediator: Mediator = None) -> None:
    self._mediator = mediator

  def set_enabled(self, enabled: bool) -> None:
    self.enabled = enabled

  def is_enabled(self) -> bool:
    return self.enabled

  @property
  def mediator(self) -> Mediator:
    return self._mediator

  @mediator.setter
  def mediator(self, mediator: Mediator) -> None:
    self._mediator = mediator


class Date(WebComponent):

  def select_date(self, date):
    print(date, " is selected.")
    self.mediator.notify(self, "date")


class Time(WebComponent):

  def show_time(self, date):
    print("Available time for", date, "is ...")

  def select_time(self, time):
    print(time, "is selected.")
    self.mediator.notify(self, "time")


class OtherPerson(WebComponent):

  def check_box(self, state):
    print("Checkbox 'Other person' is checked and it's", state)
    self.mediator.notify(self, "other_person")


class NameInput(WebComponent):

  def input_name(self, name):
    print("Name entered: ", name)
    self.mediator.notify(self, "name")


class PhoneInput(WebComponent):

  def input_phone(self, phone):
    print("Phone number entered: ", phone)
    self.mediator.notify(self, "phone")


class PickUpInShop(WebComponent):

  def pick_up(self, state):
    print("Pick up in the shop option is checked and it's", state)
    self.mediator.notify(self, "pickup")
