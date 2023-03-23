from __future__ import annotations
from iterable import *


if __name__ == "__main__":

  collection = PlacesCollection()
  collection.add_item("Tower Bridge")
  collection.add_item("Big Ben")
  collection.add_item("Stonehenge")

  iterable = PlacesCollectionIterable(collection)

  print("-- Guide place --")
  print("\n".join(iterable.get_guide_place()))
  print("")

  print("-- Tourist place --")
  print("\n".join(iterable.get_tourist_place()))
  print("")

  print("-- Navigator place --")
  print("\n".join(iterable.get_navigator_place()), end="")
