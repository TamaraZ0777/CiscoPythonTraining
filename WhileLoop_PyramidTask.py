blocksNumber = int(input("How many blocks do you have?"))
blocksLeft = blocksNumber
heightCounter = 0

while blocksLeft > heightCounter:
    heightCounter += 1
    blocksLeft -= heightCounter
    if blocksLeft < heightCounter:
        break

print("Your pyramid height is: ", heightCounter, "Blocks left not used: ", blocksLeft)


