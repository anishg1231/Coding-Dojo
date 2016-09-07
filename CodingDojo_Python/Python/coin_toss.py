import random

def coinToss():
    total_heads = 0
    total_tails = 0
    count = 0
    random_num = 0
    while count <= 5000:
        random_num = random.randint(1,2)
        if (random_num == 1):
            print("Attempt #",count, ":Throwing a coin...it's head! ...",total_heads,"head(s) so far and",total_tails,"tail(s) so far")
            total_heads += 1
            count += 1
        elif (random_num == 2):
            print("Attempt #",count, ":Throwing a coin...it's tail! ...",total_tails,"tail(s) so far and",total_heads,"heads(s) so far")
            total_tails += 1
            count += 1

coinToss()
