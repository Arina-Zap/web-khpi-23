from typing import Any, List


class PlacesCollection:

  def __init__(self):
    self.collection = []

  def add_item(self, item: Any):
    self.collection.append(item)
