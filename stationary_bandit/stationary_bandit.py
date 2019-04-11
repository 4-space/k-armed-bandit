import numpy as np

"""
This is the testbed for the k-armed bandit problem
slot_number - a number from 1 to k that slects a slot
"""

class slot_machine:
    slots = []

    def __init__(self, k, ):
        for i in range(k):
            #generate random mean and standard deviation
            mean = np.random()
            std = np.random()
            #push this into slots
            self.slots.push((mean, std))

    def pick_slot(self, slot_number):
        m,s = slots[slot_number]
        return np.random.normal(m,s) #return reward based on result of slot

def k-armed-bandit(slot_machine, k):
    my_slot = slot_machine(k)

    best_slot = random() #random number between 1 and k
    num_episodes = 1000
    explore = random() #random chance to explore

    while(t < num_episodes):
    if(explore >= .9):
        next_slot = random()
    else:
        next_slot = best_slot

    current_reward = my_slot.pick_slot(next_slot)
    avg_reward = avg_reward + current_reward  #update equation for

def run-bandit(num_runs):


def main():
