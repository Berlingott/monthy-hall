import random
    #if 1 selected, it is a win
    #if not, loose
def run_trial_no_switch(ndoor,ntry):
    win = 0
    ntest = 0
    while ntry >= ntest:
        chosen_door = random.randint(1, ndoor)
        if chosen_door == 1 :
            win += 1
        ntest += 1
    return win

def run_trial_with_switch(ndoor,ntry):
    win = 0
    ntest = 0
    while ntry >= ntest:
        chosen_door = random.randint(1, ndoor)
        if chosen_door == 1:
            chosen_door = 2
        elif chosen_door == 2:
            chosen_door = 1
        elif chosen_door == 3:
            chosen_door = 1
        if chosen_door == 1:
            win += 1
        ntest += 1
    return win

ntry = 100000000
ndoor = 3
winNumberNoSwitch = run_trial_no_switch(ndoor,ntry)
winNumberWithSwitch = run_trial_with_switch(ndoor,ntry)
print('Nombre de manche gagnante sans changer de porte:', winNumberNoSwitch)
print('Nombre de manches gagnantes en changeant de porte:', winNumberWithSwitch)