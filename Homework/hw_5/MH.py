"""CS 210 - Sabrina Zhang 
   Monty Hall - More Doors Edition
   
   References: 
   Random int with excluded values: 
        https://stackoverflow.com/questions/42999093/generate-random-number-in-range-excluding-some-numbers
    Matplotlib Legend: 
        https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html
        
   """

import random
import matplotlib.pyplot as plt
import statistics

doors = [3, 5, 10, 25, 50, 100]

def monty_hall(i):

    car = random.randint(1, i)  
    player = random.randint(1, i)
    if player == car:
        monty = random.choice([i for i in range(1,i+1) if i not in [car]])
    else: 
        monty = car
    return player, monty, car

def outcome(i, trials):
    stay = 0
    switch = 0
    prop_sw = []
    prop_st = []
    for n in range(1, trials + 1):
        player, monty, car = monty_hall(i)
        if player == car:
            stay += 1 
        if  monty == car:
            switch += 1
        sw = switch/n
        st = stay/n 
        prop_sw.append(sw)
        prop_st.append(st)
    return prop_st, prop_sw

def main():
    n = 50000
    for i in doors:
        stay, switch = outcome(i, n)
        x = [i for i in range(n)]
        y1 = stay
        y2 = switch
        fig, ax = plt.subplots()
        line_stay = ax.plot(x, y1)
        line_switch = ax.plot(x, y2)
        plt.xlabel("trials")
        plt.ylabel("N Doors")
        plt.legend(["Stay", "Switch"])
        fig.savefig(f"plot_{i}")
        plt.show()
        print(f"{i} Doors : Stay = ({statistics.mean(stay)}), Switch = ({statistics.mean(switch)})")

if __name__ == "__main__":
    main()