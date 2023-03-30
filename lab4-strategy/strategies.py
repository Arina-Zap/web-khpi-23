from abc import ABC, abstractmethod


class Strategy(ABC):
  price = None

  @abstractmethod
  def do_algorithm(self):
    pass

  def print_price(self):
    print("Your price for delivery is", self.price, "grn.")


class Samovyvoz(Strategy):
  def __init__(self):
    self.price = 0.0
  def do_algorithm(self) -> None:
    print("Self-delivery was chosen.")


class DostavkaZovnishSluzhb(Strategy):
  def __init__(self):
    self.price = 70.0
  def do_algorithm(self) -> None:
    print("External delivery was chosen.")


class DostavkaVlasnSluzhb(Strategy):
  def __init__(self):
    self.price = 50.0
  def do_algorithm(self) -> None:
    print("Internal delivery was chosen.")
