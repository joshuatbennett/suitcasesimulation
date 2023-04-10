import random


def get_random_number(lower_bound, upper_bound):
    return random.randint(lower_bound, upper_bound)


isInSuitcase = 0
isNotInSuitcase = 0

for i in range(1, 1000000):
    suitcase = [0, 0, 0, 0]
    if get_random_number(0, 100) <= 80:
        compartment = get_random_number(0, 3)
        suitcase[compartment] = 1

    if suitcase[0] == 0 and suitcase[1] == 0 and suitcase[2] == 0:
        if suitcase[3] == 1:
            isInSuitcase += 1
        else:
            isNotInSuitcase += 1
# 199934
print(isInSuitcase)
# 197673
print(isNotInSuitcase)