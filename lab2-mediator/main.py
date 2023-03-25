from __future__ import annotations
from components import *


if __name__ == "__main__":
  pick_up = PickUpInShop()
  other_person = OtherPerson()
  name = NameInput()
  phone = PhoneInput()
  date = Date()
  time = Time()

  mediator = ConcreteMediator(pick_up, other_person, name, phone, date, time)

  """
  'Pick up in shop' option ia enabled and other input options are disabled.
  """

  pick_up.pick_up("active")

  print("\n", end="")

  """
  'Other person receiver' option ia enabled and other input options are enabled.
  """

  other_person.check_box("active")
  date.select_date("08.03.2023")

