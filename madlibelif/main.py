# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

adj = input("Adjective: ")
name = input("Name: ")
pronoun = input("Pronoun: ")
verb1 = input("Verb:")
noun = input("Noun:")
verb2 = input("Verb: ")

madLibA = f"{name}'s mom is so {adj} when {pronoun} {verb1} the {noun} it {verb2}"
madLibB = f"{name} mom is so {adj} when {pronoun} {verb1} the {noun} it {verb2}"

if name == "your":
   print(madLibB)
else:
   print(madLibA)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
