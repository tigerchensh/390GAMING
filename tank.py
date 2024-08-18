import scipy.stats
import random
import numpy as np

POSSBILITY_COPPER = 1
POSSBILITY_SILVER = 0.45
POSSBILITY_GOLD = 0.05
POSSBILITY_CAR = 0.013
POSSBILITY_TREASURE = 0.2
WANTED_COPPER = 10
WANTED_SILVER = 5
WANTED_GOLD = 4

def main():
    buy = 0
    car_copper = 0
    car_silver = 0
    car_gold = 0
    treaure_copper = 0
    treasure_silver = 0
    treaure_gold = 0
    while(True):
        buy += 1
        if random.uniform(0, 1) < POSSBILITY_CAR or treaure_copper == 40:
            if treaure_copper == 40:
                treaure_copper = 0
            if car_copper > WANTED_COPPER :
                buy, treaure_gold, car_gold, treasure_silver, car_silver = treasure_mystery(buy, treaure_gold, car_gold, treasure_silver, car_silver, True)
            else:
                car_copper += 1
        else:
            treaure_copper += 1
            if random.uniform(0, 1) < POSSBILITY_TREASURE:
                buy, treaure_gold, car_gold, treasure_silver, car_silver = treasure_mystery(buy, treaure_gold, car_gold, treasure_silver, car_silver)
        if car_gold > WANTED_GOLD :
            return buy

def treasure_mystery(buy, treaure_gold, car_gold, treasure_silver, car_silver, if_gold = False):
    i = 1
    while i > 0:
        i -= 1
        rand = random.uniform(0, 1)
        if rand < POSSBILITY_GOLD :
            if if_gold or random.uniform(0, 1) < POSSBILITY_CAR or treaure_gold == 20:
                if_gold = False
                if treaure_gold == 20:
                    treaure_gold = 0
                car_gold += 1
            else:
                treaure_gold += 1
                if random.uniform(0, 1) < POSSBILITY_TREASURE:
                    i += 1
        elif rand > POSSBILITY_GOLD and rand < POSSBILITY_SILVER :
            if random.uniform(0, 1) < POSSBILITY_CAR or treasure_silver == 40:
                if treasure_silver == 40:
                    treasure_silver = 0
                if car_silver > WANTED_SILVER:
                    i += 1
                    if_gold = True
                else:
                    car_silver += 1
            else:
                treasure_silver += 1
                if random.uniform(0, 1) < POSSBILITY_TREASURE:
                    i += 1
        else:
            buy -= 1
    return buy, treaure_gold, car_gold, treasure_silver, car_silver

def mean_confidence_interval(data, confidence=0.95):
    a = 1.0 * np.array(data)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return m, m-h, m+h

if __name__=="__main__":
    list = []
    total = 0
    simulation_time = 1000
    for i in range(simulation_time):
        num = main()
        list.append(num)
        total += num
    a = np.array(list)
    m, small, big = mean_confidence_interval(a)
    print(f'Mean {m}, 95% confidence interval from {small} to {big}')
    print(f'25th percentile {np.percentile(a, 25)}, 50th percentile {np.percentile(a, 50)}, 75th percentile {np.percentile(a, 75)}')
        