import random

a = 0
b = 100
n = random.randint(a, b)

print("The computer chooses a random number between", a, "and", b)
print("Try and guess it in under 10 chances")


for i in range(10):
    inp = int(input("Your guess :"))
    if (inp == n):
        print()
        print("You are right")
        print("You did it in", i, "chances")
        break
    elif not (inp == n):
        if (i == 10):
            print("You Lost")
            break
        else:
            if (inp > n):
                print("A bit lesser")
            else:
                print("A bit more")
            print("Try Again")
            print()
