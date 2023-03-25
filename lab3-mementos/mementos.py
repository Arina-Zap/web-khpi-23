from __future__ import annotations
from abc import ABC, abstractmethod
from datetime import datetime
from originators import *


class Memento(ABC):

  @abstractmethod
  def get_name(self) -> str:
    pass

  @abstractmethod
  def get_date(self) -> str:
    pass


class NotifySettingsMemento(Memento):
  def __init__(self, news_notifier, letters_notifier, ads_notifier) -> None:
    self._news_notifier = news_notifier
    self._letters_notifier = letters_notifier
    self._ads_notifier = ads_notifier
    self._date = str(datetime.now())[:19]
    self._name = "news: {news_notifier}; letters: {letters_notifier}; ads: {ads_notifier}" \
      .format(news_notifier=self._news_notifier, letters_notifier=self._letters_notifier,
              ads_notifier=self._ads_notifier)

  def get_name(self) -> str:
    return self._name

  def get_date(self) -> str:
    return self._date

  def is_news_notifier(self):
    return self._news_notifier

  def is_letters_notifier(self):
    return self._letters_notifier

  def is_ads_notifier(self):
    return self._ads_notifier


class Caretaker:

  def __init__(self, originator: Originator) -> None:
    self._mementos = []
    self._originator = originator

  def save(self) -> Memento:
    return NotifySettingsMemento

  def backup(self) -> None:
    print("\nCaretaker: Saving Originator's state...")
    self._mementos.append(self._originator.save())

  def undo(self) -> None:
    if not len(self._mementos):
      return

    memento_ = self._mementos.pop()
    memento = self._mementos[len(self._mementos) - 1]
    print(f"Caretaker: Restoring state to: {memento.get_name()}")
    self._originator.restore(memento)

  def show_history(self) -> None:
    print("Caretaker: Here's the list of mementos:")
    for memento in self._mementos:
      print(memento.get_name())
