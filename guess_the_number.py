import random
inputU = int(input())
min = 3
max = 6
rando = random.randint(min,max)
print (inputU)
print (rando)
while (rando!=inputU or rando == inputU):
    if (inputU<3):
        print("Your guess is very low....!\n")
    elif (inputU>6):
        print("Your guess is very high....!\n")
    else:
        print("Your guess is correct.....!\n")
    break
