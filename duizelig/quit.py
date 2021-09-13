iteratie = 0
while True:
    antwoord = input("")
    if antwoord.lower() == "quit":
        iteratie = iteratie + 1
        print(str(iteratie)+"e loop")
        break

    iteratie = iteratie + 1
    print(str(iteratie)+"e loop")
