from __future__ import annotations
from strategies import *

class Context:
  def __init__(self, strategy: Strategy) -> None:
    self._strategy = strategy

  @property
  def strategy(self) -> Strategy:
    return self._strategy

  @strategy.setter
  def strategy(self, strategy: Strategy) -> None:
    self._strategy = strategy

  def do_some_business_logic(self) -> None:
    self._strategy.do_algorithm()
    self._strategy.print_price()




if __name__ == "__main__":
  context = Context(Samovyvoz())
  context.do_some_business_logic()
  print()

  context.strategy = DostavkaVlasnSluzhb()
  context.do_some_business_logic()
  print()

  context.strategy = DostavkaZovnishSluzhb()
  context.do_some_business_logic()
