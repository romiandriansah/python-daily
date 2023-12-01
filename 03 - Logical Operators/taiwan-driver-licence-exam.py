print("Hello, Welcome to registration of "
      "Heavy Motorcycle License Program")

ask1 = input("Do you own Taiwanese scooter license"
             " (regular motorcycle 50 – 250cc) for at least 1 year? Y/N \n")


if ask1 == "y":
    ask2 = input("Do you over 20 years old? Y/N \n")
    if ask2 == "y":
        ask3 = input("If you are foreigner, an ARC that has been issued"
                     " for at least 6 months or longer. Y/N \n")
        if ask3 == "y":
            print("Congratulation! You have met the qualifications")
            print("You can registration this program")
        else:
            print("Sorry! You must met 3 of qualification above")
    else:
        print("Sorry! You must met 3 of qualification above")
else:
    print("You can't yet to take this program")
    print("Your scooter license must at least 1 year")

# i will review program later