import random

rolle = "YES"

def roll(sds):
    
    num = random.randint(1, sds)
    print("\n" + str(num))

sds = int(input("\nHow many sides?\n"))


while rolle == "YES":
    roll(sds)
    rolle = (input("\nRoll again? (yes, no)\n: ")).upper()
