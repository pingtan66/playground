import random


def draw():

    while True:
        x = random.choices([0, 1], k = 2)
        if sum(x) == 1:
            return x[0]

random.seed(123456)
results = [draw() for i in range(100000)]

print(sum(results))

