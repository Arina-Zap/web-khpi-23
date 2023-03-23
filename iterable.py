from typing import List
from collections.abc import Iterable
from iterator import *
from collection import *


class PlacesCollectionIterable(Iterable, PlacesCollection):

  def __init__(self, collection: PlacesCollection):
    super().__init__()
    self._collection = collection.collection

  def __iter__(self) -> PlacesOrderIterator:
    return PlacesOrderIterator(self._collection)

  def get_guide_place(self) -> GuideIterator:
    print("All places:")
    return GuideIterator(self._collection)

  def get_navigator_place(self) -> NavigatorIterator:
    print("Two last places of the list:")
    return NavigatorIterator(self._collection, 1)

  def get_tourist_place(self) -> TouristIterator:
    print("Reverse order of the places:")
    return TouristIterator(self._collection, reverse=True)
