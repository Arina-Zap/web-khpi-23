from mementos import *


class Originator:
  _name = None
  _news_notifier = None
  _letters_notifier = None
  _ads_notifier = None

  def save(self) -> Memento:
    return NotifySettingsMemento(self._news_notifier, self._letters_notifier, self._ads_notifier)

  def restore(self, memento: Memento) -> None:
    self._name = memento.get_name()


class NotifySettings(Originator):
  def __init__(self, news_notifier, letters_notifier, ads_notifier) -> None:
    self._news_notifier = news_notifier
    self._letters_notifier = letters_notifier
    self._ads_notifier = ads_notifier
    self._name = "news: {news_notifier}; letters: {letters_notifier}; ads: {ads_notifier}" \
      .format(news_notifier=self._news_notifier, letters_notifier=self._letters_notifier,
              ads_notifier=self._ads_notifier)

  def restore(self, memento: Memento) -> None:
    self._name = memento.get_name()
    print(f"Originator: My state has changed to: {self._name}")

  def get_name(self) -> str:
    return self._name

  def set_news_notifier_state(self, news_notifier):
    self._news_notifier = news_notifier

  def is_news_notifier(self):
    return self._news_notifier

  def set_letters_notifier_state(self, letters_notifier):
    self._letters_notifier = letters_notifier

  def is_letters_notifier(self):
    return self._letters_notifier

  def set_ads_notifier_state(self, ads_notifier):
    self._ads_notifier = ads_notifier

  def is_ads_notifier(self):
    return self._ads_notifier
