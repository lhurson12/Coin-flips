import sys
import random

#initialising all values
heads = 0
tails = 0
count = 0

print("Heads or Tails?")
#loop to count results of the coin flip
while count <= 99:
    count += 1
    flip = random.randint(1,2)
    if flip == 1:
        heads += 1
    else:
        tails += 1
#stating the results of the flip
if heads<tails:
    print("Tails had",tails, "flips! Tails won by", tails-heads, "flips!")
else:
    print("Heads had", heads, "flips! Heads won by", heads-tails, "flips!")
