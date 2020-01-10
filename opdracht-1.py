import random
import math

def opdracht1():
    firstFour = input("Enter your four numbers. ")
    print(firstFour[3])
    print(firstFour[2])
    print(firstFour[1])
    print(firstFour[0])

def opdracht2():
    firstNum = input("Enter first number. ")
    secondNum = input("Enter second number. ")
    som = int(firstNum) + int(secondNum)
    verschil = int(firstNum) - int(secondNum)
    product = int(firstNum) * int(secondNum)
    quotiënt = int(firstNum) / int(secondNum)

    print("The sum is: " + str(som))
    print("The differnce is: " + str(verschil))
    print("The product is: " + str(product))
    print("The quotient is: " + str(quotiënt))

def opdracht3():
    height = input("Enter the height (in cm). ")
    width = input("Enter the width (in cm). ")
    circumference = (int(height) + int(width)) * 2
    surface = int(height) * int(width)

    print("The circumference is: " + str(circumference) + "cm2")
    print("The surface is: " + str(surface) + "cm2")

def opdracht4():
    height = input("Enter the height of the beam (in cm). ")
    width = input("Enter the width of the beam (in cm). ")
    depth = input("Enter the depth of the beam (in cm). ")
    capacity = int(height) * int(width) * int(depth)
    # surface goedmaken
    eenEnDrie = (int(width) * int(height)) * 2
    tweeEnVier = (int(width) * int(depth)) * 2
    vijfEnZes = (int(height) * int(depth)) * 2


    surface = eenEnDrie + tweeEnVier + vijfEnZes

    print("The circumference is: " + str(capacity) + "cm3")
    print("The surface is: " + str(surface) + "cm2")

def opdracht5():
    firstNum = int(input("Enter a number less then 100. "))
    while firstNum > 100:
        print(str(firstNum) + " is bigger then 100. \n please enter again.")
        firstNum = input("Enter a number less then 100. ")
    i = 1
    addNum = firstNum
    while i <= firstNum:
        addNum = addNum + i
        i = i + 2
    print("Your final number is: " + str(addNum))

def opdracht6():
    first = int(input("Enter the first number. "))
    second = int(input("Enter the second number. "))
    third = int(input("Enter the third number. "))

    if first > second and first > third:
        print("The first number is the biggest number. ")
    elif second > first and second > third:
        print("The second number is the biggest number. ")
    elif third > first and third > first:
        print("The third number is the biggest")

def opdracht7():
    lenenBedrag = int(input("wat is je te lenen bedrag in euro's? "))
    rente = int(input("wat is je rente in percentages? ")) / 100
    berdagPM = int(input("welk pedrag wil je per maand aflossen in euro's? "))

    print(((lenenBedrag + (lenenBedrag *  rente)) - berdagPM) / 12 + " jaar")

def opdracht8():
    def fibonacci2(n):
        a = 0
        b = 1
        for i in range(0, n):
            # alleen om waarschuwing weg te halen XD
            i=i
            print(a)
            temp = a
            a = b
            b = temp + b
        return a

    # Directly display the numbers.
    fibonacci2(20)

def opdracht9():
    som = 0
    numA = int(input("Enter a number that is smaller then 10. "))
    while numA > 10:
        numA = int(input("The number is bigger then 10. \nPlease enter a number smaller then 10. "))

    numB = int(input("Enter a number that is bigger the first and less then 50. "))

    while numB < numA or numB >= 50:
        numB = int(input("This is invalid \nPlease enter a number. "))

    print("getal " + " derde macht " + " vierde macht")
    numA9 = numA
    while numA < numA9 + 10:
        print(str(numA) + "       " + str(numA ** 3) + "           " + str(numA ** 4))
        numA = numA + 1

    if (numA9 % 2) == 1:
        start = numA9 + 1 

    else:
        start = numA9 + 2
    
    
    while start < numB:
        som = som + (start ** 2)
        start = start + 2

    print(som)

def opdracht10():
    prijs = 0
    goOn = True
    uur = input("Hoeveel uur sta je? ")
    minuten = input("Hoeveel minuten sta je")


    while goOn:
        if uur < 1 or minuten < 60 and uur == 0:
            prijs = 1
    

def opdracht11():
    lijst = []
    aantal = 0

    for i in range(100):
        i = random.randint(0, 100)
        lijst.append(i)

    for i in lijst:
        if (i % 2) == 0:
            aantal = aantal + 1
    
    print("Even: " + str(aantal))
    print("Oneven: " + str(100 - aantal))


def opdracht12():
    i = -4
    sin = 
    print()

def opdracht13():
    print("deze opdracht is nog niet verder uitgewerkt. ")

def opdracht14():
    print("deze opdracht is nog niet verder uitgewerkt. ")

def opdracht15():
    print("deze opdracht is nog niet verder uitgewerkt. ")

def main():
    answer = input("Welke opdracht wil je doen? ")
    if answer == "opdracht 15":
        opdracht15()
    if answer == "opdracht 14":
        opdracht14()
    if answer == "opdracht 13":
        opdracht13()
    if answer == "opdracht 12":
        opdracht12()
    if answer == "opdracht 11":
        opdracht11()
    if answer == "opdracht 10":
        opdracht10()
    if answer == "opdracht 9":
        opdracht9()
    if answer == "opdracht 8":
        opdracht8()
    if answer == "opdracht 7":
        opdracht7()
    if answer == "opdracht 6":
        opdracht6()
    if answer == "opdracht 5":
        opdracht5()
    if answer == "opdracht 4":
        opdracht4()
    if answer == "opdracht 3":
        opdracht3()
    if answer == "opdracht 2":
        opdracht2()
    if answer == "opdracht 1":
        opdracht1()    

opdracht11()