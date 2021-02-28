baliky = {
    "B541X": True,
    "B547X": False,
    "B251X": False,
    "B501X": True,
    "B947X": False,
}
cisloBaliku = input("Zadej číslo balíku: ")
if baliky[cisloBaliku]:
   print("Balík byl předán kurýrovi.")
else:
       print("Balík zatím nebyl předán kurýrovi.")
 