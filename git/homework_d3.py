#AD1 1. Napisz program do przeliczania stopni Celsjusza na Fahrenheita i odwrotnie (wyświetlając wzór i kolejne obliczenia)

print ("Konwerter Fahrenheit - Celcjusz")
temp = input("Wrowadz temperature w Celcjuszasz lub Fahrenheitach? (np., 45F, 102C itd.) : ")
result = int(temp[:-1])
i_convention = temp[-1]
if i_convention.upper() == "C":
result = int(round((9 * result) / 5 + 32))
o_convention = "Fahrenheit"
elif i_convention.upper() == "F":
result = int(round((result - 32) * 5 / 9))
o_convention = "Celcjuszach"
else:
print("Wprowadz liczbe stopni.")
quit()
print("Temperatura w ", o_convention, "wynosi", result, "stopni.")



#AD4  Napisz program do przeliczania liczby zapisanej w formacie binarnym na system dziesiętny.

print ("Konwerter liczb binarnych.")
user_input = int(input("podaj liczbe binarna:"))

bits = list(str(user_input))

decimal = 0

counter = 0

for i in reversed(bits):
     decimal += 2**counter * int(i)
     counter+=1

print ("Liczba w formacie dziesietnym wynosi:", decimal)

#AD5 Napisz program do sprawdzania czy podany rok jest rokiem przystępnym

print("Sprawdzenie czy podany rok jest przystepny:")
liczba = int(input("Podaj rok: "))
if liczba % 2 == 0:
print("Podany rok jest przystepny")

elif liczba % 2 != 0:
print("Podany rok nie jest przystepny")

 elif liczba <= 0:

   print("Podales niepoprawny rok")
