from originators import *

if __name__ == "__main__":
  notify_settings = NotifySettings(True, True, True)
  caretaker = Caretaker(notify_settings)
  caretaker.backup()
  caretaker.show_history()
  # news: true; letters: true; adv: true

  print("\n", end="")

  notify_settings.set_news_notifier_state(False)
  caretaker.backup()
  caretaker.show_history()
  # news: true; letters: true; adv: true
  # news: false; letters: true; adv: true

  print("\n", end="")

  notify_settings.set_ads_notifier_state(False)
  caretaker.backup()
  caretaker.show_history()
  # news: true; letters: true; adv: true
  # news: false; letters: true; adv: true
  # news: false; letters: true; adv: false

  print("\n", end="")

  caretaker.undo()
  print("\n", end="")

  caretaker.undo()
  print("\n", end="")

  caretaker.show_history()
  # news: true; letters: true; adv: true
