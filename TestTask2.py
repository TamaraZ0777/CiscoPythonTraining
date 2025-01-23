# number = int(input("Enter a integer number that is not zero or negative: "))
for number in range(1, 10000000):
    step_counter = 0
    initial_number = number

    while number > 1:
        if number % 2 == 0:
            number /= 2
            step_counter +=1
            #print(number)
            if step_counter > 1000:
                print("Oh, more than " + str(step_counter) + "!")
                break
        else:
            number = 3 * number + 1
            step_counter +=1
            #print(number)
    else:
        #print(number)
        if number < 1:
            print("Here it is!")
    #print (str(initial_number) + ":" + str(step_counter))

