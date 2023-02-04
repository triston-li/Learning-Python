def fart():
    print("I hope you didn't fart.")
    answer = input("Did you fart?? Y/N > ")
    if answer == "Y":
        print("Ugh you smell!")
    elif answer == "N":
        print("Good job at keeping that fart in!")
    else:
        print("Type Y or N, I don't know what you're saying to me right now.")

print("I'm going to see if you farted, okay?")
fart()