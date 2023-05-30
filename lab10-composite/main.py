from __future__ import annotations
from abc import ABC, abstractmethod


class Component(ABC):
  def __init__(self, id):
    self.id = id

  @abstractmethod
  def get_html_element(self):
    pass


class FieldSet(Component):
  def __init__(self, id):
    super().__init__(id)
    self.items = []

  def add_item(self, item):
    self.items.append(item)
    return self

  def del_item(self, item):
    self.items.remove(item)

  def get_items(self):
    return self.items

  def get_item(self, item):
    return item.get_html_element()

  def get_html_element(self):
    items = map(self.get_item, self.items)
    items = list(items)
    content = ""
    for item in items:
      content += str(item)
    return "<fieldset>\n" + content + "</fieldset>\n\n"


class Input(Component):
  def __init__(self, id):
    super().__init__(id)
    self.id = id

  def get_html_element(self):
    return "<input id=" + self.id + "/>\n"


class Select(Component):
  def __init__(self, id):
    super().__init__(id)
    self.id = id

  def get_html_element(self):
    return "<select id=" + self.id + "</select>\n"


if __name__ == "__main__":
  fieldset = FieldSet('fs1')

  input1 = Input('in1')
  select1 = Select("s1")

  fieldset = fieldset.add_item(input1).add_item(select1)
  print(fieldset.get_html_element())

  input2 = Input('in2')
  print(input2.get_html_element())

  select2 = Select('s2')
  print(select2.get_html_element())
