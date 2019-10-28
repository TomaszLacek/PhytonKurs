#iek = input("ile masz lat")
#zwierzaki = input("ile masz kotow")


#wiek = 2
#zwierzaki = 5
#zdanie = "ala ma 2 lata i posiada 5 kotow"
#zdanie = "ala ma  " + (str) wiek + "lata i posiada " + str(zwierzaki)
#zdanie = f"ala ma  {wiek} lata i posiada  {zwierzaki} kotow"
#zdanie = "ala ma {} lata i posiada  {} kotow".format(wiek, zwierzaki)
#zdanie = "ala ma {a} lata i posiada  {b} koty".format(b=wiek, a=zwierzaki)

#print(zdanie)

#liczba = 1.234
#print("liczba: %s" % liczba)
#print("liczba: %0.1f" % liczba)
#print("liczba: %d" % liczba)
#
# zdanie = "encyklopedia"
# print(zdanie[4])
# print(zdanie[-3])
# print(zdanie[2:8])
# print(zdanie[:7])
# print(zdanie[8:])
# print(zdanie[1:7:2])
# print(zdanie[:: -1])

# print("start")
# #zmienna = None
#
# if 1 == "1":
#     print("prawda")
# else:
#     print("koniec")

#
#print("sprawdzenie parzystosci liczby")
# print("sprawdzenie podzielnosci liczby")
# liczba = int(input("podaj liczbe:"))
# if liczba % 3 == 0:
#     print("podana liczba jest podzielna przez 3")
#
# elif liczba % 5 == 0:
#     print("podana liczba jest podzielna przez 5")
# elif liczba % 5 == 0 and liczba % 3 == 0:
#     print("podana liczba jest podzielna przez 5 i 3")




# wyrazy = ["raz", "dwa", "trzy"]
# wyrazy[0] = "jeden"
# print(wyrazy)
#

# zakupy = ["kielbasa", "piwko", "chipsy", "wegiel"]
# # # print(zakupy)
# # # zakupy.append("talerzyki")
# # # print(zakupy)
# # # zakupy[0] = "ëlektryczny_grill"
# # # zakupy.remove("piwko")
# # # print(zakupy)


#print 'Program zmienia wprowadzony przez użytkownika ciąg cyfr na formę tekstowa'

# x = raw_input("> Podaj CIAG liczb ")
#
# liczby = ["zero", "jeden", "dwa", "trzy", "cztery", "piec", "szesc", "siedem", "osiem", "dziewiec"]
#
# for i in x:
#     if i.isdigit():
#         y = int(i)
#         print
#         liczby[y],

# lista_ocen = []  # tworzymy pusta liste, aby dodac do niej oceny

# while True:
#     try:
#         oceny = float(raw_input("> Dodaj ocene: "))
#         if oceny in range(1, 7):
#             lista_ocen.append(oceny)
#             print
#             lista_ocen
#         elif oceny not in range(1, 7):
#             print
#             "> Zakres ocen", range(1, 7)
#     except ValueError:
#         break
# #
# # print
# "\n> Srednia ocen", sum(lista_ocen) / len(lista_ocen)


# lista_ocen = []  # tworzymy pusta liste, aby dodac do niej oceny
#
#
# def raw_input(1):
#     pass
#
#
# while True:
#     try:
#         oceny = float(raw_input("> Dodaj ocene: "))
#         if oceny in range(1, 7):
#             lista_ocen.append(oceny)
#             print
#             lista_ocen
#         elif oceny not in range(1, 7):
#             print
#             "> Zakres ocen", range(1, 7)
#     except ValueError:
#         break




temp = input("Wrowadz temperature w Celcjuszasz lub Fahrenheitach? (np., 45F, 102C itd.) : ")
stopnie = int(temp[:-1])
i_convention = temp[-1]

if i_convention.upper() == "C":
  result = int(round((9 * stopni) / 5 + 32))
  o_convention = "Fahrenheit"
elif i_convention.upper() == "F":
  result = int(round((stopnie - 32) * 5 / 9))
  o_convention = "Celcjusza"
else:
  print("Wprowadz liczbe stopni.")
  quit()
print("Temperatura w ", o_convention, "wynosi", result, "stopni.")

