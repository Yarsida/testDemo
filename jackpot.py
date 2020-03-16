import numpy as np

# values of Jackpot
jackpotStatus = "None"
jackpotWin = 0
GRAND = 1
MAJOR = 50
MINOR = 500
MINI = 5000
NOTHING = 10000000
grandWin = 5000
majorWin = 200
minorWin = 50
miniWin = 10
nothingWin = 0
jackpot = [0, 0, 0, 0, 0]
jackpot[0] = GRAND
jackpot[1] = jackpot[0] + MAJOR
jackpot[2] = jackpot[1] + MINOR
jackpot[3] = jackpot[2] + MINI
jackpot[4] = jackpot[3] + NOTHING

# print(jackpot)

j = np.random.randint(0, max(jackpot))
# print(j)
jackpotScore = 0
if j < jackpot[0]:
    jackpotStatus = "Grand"
    jackpotScore = grandWin
elif j < jackpot[1]:
    jackpotStatus = "Major"
    jackpotScore = majorWin
elif j < jackpot[2]:
    jackpotStatus = "Minor"
    jackpotScore = minorWin
elif j < jackpot[3]:
    jackpotStatus = "Mini"
    jackpotScore = miniWin
else:
    jackpotStatus = "Nothing"
    jackpotScore = nothingWin
jackpotWin = jackpotWin + jackpotScore
print(jackpotStatus)
print(jackpotScore)
print(jackpotWin)
print(" ")

print(jackpot)

