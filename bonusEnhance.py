import numpy as np
import csv

# values of bonus
bonusStatus = "None"
bonusWin = 0
bonus_1 = 10
bonus_2 = 10
bonus_3 = 10
bonus_4 = 10
bonus_1_win = 0.5
bonus_2_win = 1
bonus_3_win = 1.5
bonus_4_win = 2
bonus = [0, 0, 0, 0]
bonus[0] = bonus_1
bonus[1] = bonus[0] + bonus_2
bonus[2] = bonus[1] + bonus_3
bonus[3] = bonus[2] + bonus_4
# print(bonus)


def bonusEnhance():
    global bonus, bonusScore, bonusStatus, bonusWin
    j = np.random.randint(0, max(bonus))
    # print(j)
    bonusScore = 0
    if j < bonus[0]:
        bonusStatus = "bonus_1_win"
        bonusScore = bonus_1_win
    elif j < bonus[1]:
        bonusStatus = "bonus_2_win"
        bonusScore = bonus_2_win
    elif j < bonus[2]:
        bonusStatus = "bonus_3_win"
        bonusScore = bonus_3_win
    elif j < bonus[3]:
        bonusStatus = "bonus_4_win"
        bonusScore = bonus_4_win
    bonusWin = bonusWin + bonusScore
    return bonusWin, bonusStatus

bonusEnhance()

with open("./test.csv", 'a+', newline='') as t_file:
    csv_writer = csv.writer(t_file)
    csv_writer.writerow([bonusWin, bonusStatus])

print(bonusWin, bonusStatus)








