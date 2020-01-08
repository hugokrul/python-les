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
    product = int(firstNum) * int(secondNum)
    quotiënt = int(firstNum) / int(secondNum)

    print("The sum is: " + str(som))
    print("The product is: " + str(product))
    print("The quotient is: " + str(quotiënt))

def opdracht3():
    height = input("Enter the height (in cm). ")
    width = input("Enter the width (in cm). ")
    circumference = int(height) + int(width)
    surface = int(height) * int(width)

    print("The circumference is: " + str(circumference) + "cm2")
    print("The surface is: " + str(surface) + "cm2")

def opdracht4():
    height = input("Enter the height of the beam (in cm). ")
    width = input("Enter the width of the beam (in cm). ")
    depth = input("Enter the depth of the beam (in cm). ")
    capacity = int(height) * int(width) * int(depth)
    surface = int(height) * int(width)

    print("The circumference is: " + str(capacity) + "cm3")
    print("The surface is: " + str(surface) + "cm2")

def opdracht5():
    firstNum = int(input("Enter a number less then 100. "))
    while firstNum > 100:
        print(str(firstNum) + " is bigger then 100. \n please enter again.")
        firstNum = input("Enter a number less then 100. ")
    if firstNum <= 100:
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
    lenenBedrag = input("wat is je te lenen bedrag? ")
    rente = input("wat is je rente in percentages? ")
    berdagPM = input("welk pedrag wil je per maand aflossen? ")

def opdracht8():
    print("deze opdracht is nog niet verder uitgewerkt. ")

def opdracht9():
    print("deze opdracht is nog niet verder uitgewerkt. ")

def opdracht10():
    print("deze opdracht is nog niet verder uitgewerkt. ")

def opdracht11():
    print("deze opdracht is nog niet verder uitgewerkt. ")

def opdracht12():
    print("deze opdracht is nog niet verder uitgewerkt. ")

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

main()
