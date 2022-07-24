# Wrzuć najważniejsze rzeczy
import string, secrets, os
pokazGeneracjeAndroida42 = lambda: os.system('clear')

# Ustaw potem potrzebne zmienne
a = string.ascii_letters
b = string.digits

# Poproś o informacje i wygeneruj to co potrzeba
c = input("Co chcesz otrzymać? [H(asło)/P(in)/N(ick)]: ")

if c == "H" or c == "h": # Wybór: Hasło
  d = input("Jakiej długości hasło potrzebujesz? [nieskończony zakres]: ")
  e = ''.join(secrets.choice (a) for i in range(int(d)))
  pokazGeneracjeAndroida42()
  print("Twoje hasło to:")
  print(e)

if c == "P" or c == "p": # Wybór: PIN
  d = input("Jakiej długości PIN potrzebujesz? [nieskończony zakres]: ")
  f = ''.join(secrets.choice (b) for i in range(int(d)))
  pokazGeneracjeAndroida42()
  print("Twój PIN to:")
  print(f)

if c == "N" or c == "n": # Wybór: Nick???
  print("Wkrótce 👀")
