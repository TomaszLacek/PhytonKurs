program_list = list ( range ( 1 , 11 ) )
program_choice = ''
program_choice_decimal_or_not: bool = False
while not program_choice_decimal_or_not :
    print(  "Witaj w Multitool Python Program by iSA - wersja beta")
    print ( "Wybierz program który cię interesuje: " )
    print ( "    -  1 - Przeliczanie stopni w skali Celcjusza i Fahrenheita" )
    print ( "    -  2 - Podawanie pierwszej i ostatniej cyfry wprowadzonej liczby" )
    print ( "    -  3 - Rysowanie prostokątu o zadanych rozmiarach" )
    print ( "    -  4 - Przeliczanie liczby zapisanej w formacie binarnym na system dziesiętny" )
    print ( "    -  5 - Czy podany rok jest rokiem przestępnym?" )
    print ( "    -  6 - Program do rysowania list " )
    print ( "    -  7 - Rozmienianie pieniędzy" )
    print ( "    -  8 - Rysowanie piramidy o określonej wysokości" )
    print ( "    -  9 - Kalkulator wieku psa" )
    print ( "    - 10 - 24h temperatur" )
    program_choice: str = input ( "Twój wybór: " )
    program_choice_decimal_or_not = program_choice.isdecimal ()
    if (program_choice_decimal_or_not != False and (
            True != program_choice_decimal_or_not and int ( program_choice ) > 10)) :
        print ( 'Wprowadzono błędą wartość: \\'.format ( program_choice ) )
        print ( "By spróbować ponownie wciśnij: T/t" )
        print ( "By zakończyć program wciśnij inny klawisz niż: T/t" )
        if (not input ( "Kontynuować? " ).upper () != "T") : \
                print ( "Wybrałeś kontynuować..." )
        program_choice_decimal_or_not = False
        print ( "Koniec programu." )
        exit ()
    else:
      print("Poprawnie dokonano wyboru. Podałeś: " +user_choice)
      if int ( program_choice ) == 1 :
          program_list = "Przeliczanie stopni w skali Celcjusza i Fahrenheita."
          print ("Konwerter Fahrenheit - Celcjusz")
          temp = input ("Wrowadz temperature w Celcjuszasz lub Fahrenheitach? (np., 45F, 102C itd.) : " )

          result = int ( temp[:-1] )
          i_convention = temp[-1]
          if i_convention.upper() == "C":
            result = int(round((9 * result) / 5 + 32))
            o_convention = "Fahrenheit"
          elif i_convention.upper () == "F":
              result = int(round((result - 32) * 5 / 9))
            o_convention = "Celcjuszach"
            else:
            print("Wprowadz liczbe stopni.")
            quit()
            print("Temperatura w ", o_convention, "wynosi", result, "stopni.")

#
# # #AD4  Napisz program do przeliczania liczby zapisanej w formacie binarnym na system dziesiętny.

    elif int(program_choice) == 2:
  program_title = "Program do przeliczania liczby zapisanej w formacie binarnym na system dziesiętny"
      print ("Konwerter liczb binarnych.")
      user_input = int(input("podaj liczbe binarna:"))
      bits = list(str(user_input))
      decimal = 0
      counter = 0
      for i in reversed (bits)
        decimal += 2**counter * int(i)
        counter+=1
