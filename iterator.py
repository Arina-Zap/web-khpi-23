from collections.abc import Iterator
from collection import PlacesCollection


class PlacesOrderIterator(Iterator):
  _position: int = None
  _reverse: bool = False

  def __init__(self, collection: PlacesCollection, position: int = 0, reverse: bool = False) -> None:
    self._collection = collection
    self._position = position if not reverse else -1
    self._reverse = reverse

  def __next__(self):
    try:
      value = self._collection[self._position]
      self._position += -1 if self._reverse else 1
    except IndexError:
      raise StopIteration()

    return value


class NavigatorIterator(PlacesOrderIterator):
  def __init__(self, collection: PlacesCollection, position: int = 0, reverse: bool = False) -> None:
    super().__init__(collection, position, reverse)


class GuideIterator(PlacesOrderIterator):
  def __init__(self, collection: PlacesCollection, position: int = 0, reverse: bool = False) -> None:
    super().__init__(collection, position, reverse)


class TouristIterator(PlacesOrderIterator):
  def __init__(self, collection: PlacesCollection, position: int = 0, reverse: bool = False) -> None:
    super().__init__(collection, position, reverse)
