import numpy as np
import csv
from jackpot import jackpotScore, jackpotStatus
from bonusEnhance import bonusEnhance, bonusWin, bonusStatus
#from bonusFreeGame import bonus_free_game, extraTime, free_score, Row1Origin, Row2Origin, Row3Origin, pigNumCount

with open('D://Bole//Code//test_Demo//test.csv')as f:
    f_csv = csv.reader(f)
    targetLines = [row for row in f_csv]
    # betTimes, win, coinTotal, bonusEnhanceStatus, bonusBaseMoney
    betTimes = int(float(targetLines[-1][0]))
    win = float(targetLines[-1][1])
    coinTotal = int(float(targetLines[-1][2]))
    meter = int(float(targetLines[-1][3]))
    bonusBaseMoney = float(targetLines[-1][4])
    bonusEnhanceStatus_1 = int(float(targetLines[-1][5]))
    bonusEnhanceStatus_2 = int(float(targetLines[-1][6]))
    bonusEnhanceStatus_3 = int(float(targetLines[-1][7]))
    bonusEnhanceStatus_4 = int(float(targetLines[-1][8]))
    bonusEnhanceStatus_5 = int(float(targetLines[-1][9]))
    print(betTimes, win, coinTotal,meter,bonusBaseMoney,bonusEnhanceStatus_1,bonusEnhanceStatus_2,bonusEnhanceStatus_3,bonusEnhanceStatus_4,bonusEnhanceStatus_5)
    print(type(betTimes))

betMoney = 1            # spin 一次的金额
baseGame = 1            # 普通游戏模式
freeGame = 0            # free game模式
jackpotPart = 0         # Fast Jackpot部分获得金钱
# betTimes = 0            # spin的次数
# coinTotal = 0           # 出现coin的总数，用以计算累计条进程
freeGameTime = 0        # 暂空
coinMore = 0            # free game单个pig中获得额外次数
extraTime = 0           # free game中获得额外次数统计
# meter = 0               # 累计条进程
# bonusEnhanceStatus_1 = bonusEnhanceStatus_1        # bonus enhance 状况，代表：[加5次，加pig额度，加pig数，加row，加col]
# bonusBaseMoney = 0      # bonus 基于之前coin的额度
bonusWheelScore = 0          # bonus 轮盘的奖励
pigNum = 0
pigNumMoney = 0

#  weights of symbols
coinChanceValue = [0.5, 1, 1.5, 2, 2, 3, 5, 10, 20, 100, 500]            # coin面额的随机模块
coinValueLabel = [100, 50, 25, 10, 9, 8, 5, 3, 2, 1, 0.5]
coinChance = [0] * len(coinChanceValue)
for coinQ in range(0, len(coinChance)):
    for coinT in range(0, coinQ + 1):
        coinChance[coinQ] = coinChance[coinQ] + coinChanceValue[coinT]
print(coinChance)

pigChanceValue = [1, 9]            # pig中获取额外free game的随机模块
pigValueLabel = [1, 0]
pigChance = [0] * len(pigChanceValue)
for pigQ in range(0, len(pigChance)):
    for pigT in range(0, pigQ + 1):
        pigChance[pigQ] = pigChance[pigQ] + pigChanceValue[pigT]
# print(pigChance)

CoinWeight = baseGame * 10 + freeGame * 0                    # 生成基础游戏的面板
PiggyWeight = baseGame * 0 + freeGame * 10
R1 = [0, 5, 6, 23, 3, 15, 24, 25, CoinWeight, PiggyWeight]  # R for reel
R2 = [8, 3, 30, 3, 25, 3, 3, 25, CoinWeight, PiggyWeight]
R3 = [4, 20, 6, 9, 7, 25, 25, 5, CoinWeight, PiggyWeight]
R4 = [10, 20, 14, 7, 7, 8, 25, 10, CoinWeight, PiggyWeight]
R5 = [0, 15, 20, 15, 20, 10, 10, 10, CoinWeight, PiggyWeight]

P1 = [0]*10  # pool of 10 symbols in each reel
P2 = [0]*10
P3 = [0]*10
P4 = [0]*10
P5 = [0]*10

#  pay of Combos
A5 = 50  # "A" means the same symbol is "A", "5" means we got 5 "A"
A4 = 10
A3 = 1.5
B5 = 20
B4 = 5
B3 = 1
C5 = 10
C4 = 3
C3 = 1
D5 = 5
D4 = 1
D3 = 0.5

# status of game reel 初始部分
S1 = "Nothing"
S2 = "Nothing"
S3 = "Nothing"
S4 = "Nothing"
S5 = "Nothing"
SO1 = "Nothing"
SO2 = "Nothing"
SO3 = "Nothing"
SO4 = "Nothing"
SO5 = "Nothing"
status = [S1, S2, S3, S4, S5]
statusOrigin = [SO1, SO2, SO3, SO4, SO5]
Row1Origin = [SO1, SO2, SO3, SO4, SO5]
Row2Origin = [SO1, SO2, SO3, SO4, SO5]
Row3Origin = [SO1, SO2, SO3, SO4, SO5]
Row1 = [S1, S2, S3, S4, S5]
Row2 = [S1, S2, S3, S4, S5]
Row3 = [S1, S2, S3, S4, S5]
Line01 = [S1, S2, S3, S4, S5]
Line02 = [S1, S2, S3, S4, S5]
Line03 = [S1, S2, S3, S4, S5]
Line04 = [S1, S2, S3, S4, S5]
Line05 = [S1, S2, S3, S4, S5]
Line06 = [S1, S2, S3, S4, S5]
Line07 = [S1, S2, S3, S4, S5]
Line08 = [S1, S2, S3, S4, S5]
Line09 = [S1, S2, S3, S4, S5]
Line10 = [S1, S2, S3, S4, S5]
Line11 = [S1, S2, S3, S4, S5]
Line12 = [S1, S2, S3, S4, S5]
Line13 = [S1, S2, S3, S4, S5]
Line14 = [S1, S2, S3, S4, S5]
Line15 = [S1, S2, S3, S4, S5]
Line16 = [S1, S2, S3, S4, S5]
Line17 = [S1, S2, S3, S4, S5]
Line18 = [S1, S2, S3, S4, S5]
Line19 = [S1, S2, S3, S4, S5]
Line20 = [S1, S2, S3, S4, S5]

for q in range(0, len(R1)):                  # 根据权重生成随机数检测部分
    for t in range(0, q + 1):
        P1[q] = P1[q] + R1[t]
    for t in range(0, q + 1):
        P2[q] = P2[q] + R2[t]
    for t in range(0, q + 1):
        P3[q] = P3[q] + R3[t]
    for t in range(0, q + 1):
        P4[q] = P4[q] + R4[t]
    for t in range(0, q + 1):
        P5[q] = P5[q] + R5[t]
#  print(P1, '\n', P2, '\n', P3, '\n', P4, '\n', P5)


def coin_value():                           # coin额度生成函数
    global coinMore, coinChance
    coinMore = 0
    coinr = np.random.randint(0, max(coinChance), 1)
    if coinr < coinChance[0]:
        coinMore = coinValueLabel[0]
    elif coinr < coinChance[1]:
        coinMore = coinValueLabel[1]
    elif coinr < coinChance[2]:
        coinMore = coinValueLabel[2]
    elif coinr < coinChance[3]:
        coinMore = coinValueLabel[3]
    elif coinr < coinChance[4]:
        coinMore = coinValueLabel[4]
    elif coinr < coinChance[5]:
        coinMore = coinValueLabel[5]
    elif coinr < coinChance[6]:
        coinMore = coinValueLabel[6]
    elif coinr < coinChance[7]:
        coinMore = coinValueLabel[7]
    elif coinr < coinChance[8]:
        coinMore = coinValueLabel[8]
    elif coinr < coinChance[9]:
        coinMore = coinValueLabel[9]
    else:
        coinMore = coinValueLabel[10]
    return coinMore


def extra_pig():                          # pig中额外游戏生成函数
    global pigMore, pigChance
    pigMore = 0
    pigr = np.random.randint(0, max(pigChance), 1)
    if pigr < pigChance[0]:
        pigMore = pigValueLabel[0]
    else:
        pigMore = pigValueLabel[1]
    return pigMore


# spin part
def reel_1():
    global S1, P1, SO1
    k1 = np.random.randint(0, max(P1), 1)
    if k1 < P1[0]:
        S1 = "W"
        SO1 = "WILD"
    elif k1 < P1[1]:
        S1 = "A"
        SO1 = "BANK"
    elif k1 < P1[2]:
        S1 = "B_1"
        SO1 = "COP"
    elif k1 < P1[3]:
        S1 = "B_2"
        SO1 = "DOG"
    elif k1 < P1[4]:
        S1 = "C_1"
        SO1 = "BOX"
    elif k1 < P1[5]:
        S1 = "C_2"
        SO1 = "KEY"
    elif k1 < P1[6]:
        S1 = "D_1"
        SO1 = "GOLD"
    elif k1 < P1[7]:
        S1 = "D_2"
        SO1 = "MONEY"
    elif k1 < P1[8] and freeGame == 0:
        S1 = "COIN"
        SO1 = "COIN"
    elif k1 < P1[9] and freeGame == 1:
        S1 = "PIG"
        SO1 = "PIG"
    return S1, SO1


def reel_2():
    global S2, P2, SO2
    k2 = np.random.randint(0, max(P2), 1)
    if k2 < P2[0]:
        S2 = "W"
        SO2 = "WILD"
    elif k2 < P2[1]:
        S2 = "A"
        SO2 = "BANK"
    elif k2 < P2[2]:
        S2 = "B_1"
        SO2 = "COP"
    elif k2 < P2[3]:
        S2 = "B_2"
        SO2 = "DOG"
    elif k2 < P2[4]:
        S2 = "C_1"
        SO2 = "BOX"
    elif k2 < P2[5]:
        S2 = "C_2"
        SO2 = "KEY"
    elif k2 < P2[6]:
        S2 = "D_1"
        SO2 = "GOLD"
    elif k2 < P2[7]:
        S2 = "D_2"
        SO2 = "MONEY"
    elif k2 < P2[8] and freeGame == 0:
        S2 = "COIN"
        SO2 = "COIN"
    elif k2 < P1[9] and freeGame == 1:
        S2 = "PIG"
        SO2 = "PIG"
    return S2, SO2


def reel_3():
    global S3, P3, SO3
    k3 = np.random.randint(0, max(P3), 1)
    if k3 < P3[0]:
        S3 = "W"
        SO3 = "WILD"
    elif k3 < P3[1]:
        S3 = "A"
        SO3 = "BANK"
    elif k3 < P3[2]:
        S3 = "B_1"
        SO3 = "COP"
    elif k3 < P3[3]:
        S3 = "B_2"
        SO3 = "DOG"
    elif k3 < P3[4]:
        S3 = "C_1"
        SO3 = "BOX"
    elif k3 < P3[5]:
        S3 = "C_2"
        SO3 = "KEY"
    elif k3 < P3[6]:
        S3 = "D_1"
        SO3 = "GOLD"
    elif k3 < P3[7]:
        S3 = "D_2"
        SO3 = "MONEY"
    elif k3 < P3[8] and freeGame == 0:
        S3 = "COIN"
        SO3 = "COIN"
    elif k3 < P1[9] and freeGame == 1:
        S3 = "PIG"
        SO3 = "PIG"
    return S3, SO3


def reel_4():
    global S4, P4, SO4
    k4 = np.random.randint(0, max(P4), 1)
    if k4 < P4[0]:
        S4 = "W"
        SO4 = "WILD"
    elif k4 < P4[1]:
        S4 = "A"
        SO4 = "BANK"
    elif k4 < P4[2]:
        S4 = "B_1"
        SO4 = "COP"
    elif k4 < P4[3]:
        S4 = "B_2"
        SO4 = "DOG"
    elif k4 < P4[4]:
        S4 = "C_1"
        SO4 = "BOX"
    elif k4 < P4[5]:
        S4 = "C_2"
        SO4 = "KEY"
    elif k4 < P4[6]:
        S4 = "D_1"
        SO4 = "GOLD"
    elif k4 < P4[7]:
        S4 = "D_2"
        SO4 = "MONEY"
    elif k4 < P4[8] and freeGame == 0:
        S4 = "COIN"
        SO4 = "COIN"
    elif k4 < P1[9] and freeGame == 1:
        S4 = "PIG"
        SO4 = "PIG"
    return S4, SO4


def reel_5():
    global S5, P5, SO5
    k5 = np.random.randint(0, max(P5), 1)
    if k5 < P5[0]:
        S5 = "W"
        SO5 = "WILD"
    elif k5 < P5[1]:
        S5 = "A"
        SO5 = "BANK"
    elif k5 < P5[2]:
        S5 = "B_1"
        SO5 = "COP"
    elif k5 < P5[3]:
        S5 = "B_2"
        SO5 = "DOG"
    elif k5 < P5[4]:
        S5 = "C_1"
        SO5 = "BOX"
    elif k5 < P5[5]:
        S5 = "C_2"
        SO5 = "KEY"
    elif k5 < P5[6]:
        S5 = "D_1"
        SO5 = "GOLD"
    elif k5 < P5[7]:
        S5 = "D_2"
        SO5 = "MONEY"
    elif k5 < P5[8] and freeGame == 0:
        S5 = "COIN"
        SO5 = "COIN"
    elif k5 < P1[9] and freeGame == 1:
        S5 = "PIG"
        SO5 = "PIG"
    return S5, SO5


def row_1():
    global Row1, Row1Origin
    reel_1()
    reel_2()
    reel_3()
    reel_4()
    reel_5()
    Row1 = [S1, S2, S3, S4, S5]
    Row1Origin = [SO1, SO2, SO3, SO4, SO5]
    return Row1, Row1Origin


def row_2():
    global Row2, Row2Origin
    reel_1()
    reel_2()
    reel_3()
    reel_4()
    reel_5()
    Row2 = [S1, S2, S3, S4, S5]
    Row2Origin = [SO1, SO2, SO3, SO4, SO5]
    return Row2, Row2Origin


def row_3():
    global Row3, Row3Origin
    reel_1()
    reel_2()
    reel_3()
    reel_4()
    reel_5()
    Row3 = [S1, S2, S3, S4, S5]
    Row3Origin = [SO1, SO2, SO3, SO4, SO5]
    return Row3, Row3Origin


def free_game(x, y):                       # free game模块，进行x次free game
    global freebetTimes, coinNum, coinNumCount, free_score, betMoney, pigNum, pigNumCount, extraTime,freeGame,baseGame, pigNumMoney
    global Line01, Line02, Line03, Line04, Line05, Line06, Line07, Line08, Line09, Line10, Line11, Line12, Line13, Line14, Line15, Line16, Line17, Line18, Line19, Line20
    extraTime = 0
    freeGame = 1
    baseGame = 0
    freePigMoney = y
    for freei in range(0, x):
        freebetTimes = freebetTimes + 1
        # print("here comes free game", freebetTimes)
        row_1()
        row_2()
        row_3()
        Line01 = [Row1[0], Row1[1], Row1[2], Row1[3], Row1[4]]
        Line02 = [Row2[0], Row2[1], Row2[2], Row2[3], Row2[4]]
        Line03 = [Row3[0], Row3[1], Row3[2], Row3[3], Row3[4]]
        Line04 = [Row1[0], Row2[1], Row3[2], Row2[3], Row1[4]]
        Line05 = [Row3[0], Row2[1], Row1[2], Row2[3], Row3[4]]
        Line06 = [Row1[0], Row1[1], Row2[2], Row1[3], Row1[4]]
        Line07 = [Row3[0], Row3[1], Row2[2], Row3[3], Row3[4]]
        Line08 = [Row1[0], Row2[1], Row2[2], Row2[3], Row1[4]]
        Line09 = [Row3[0], Row2[1], Row2[2], Row2[3], Row3[4]]
        Line10 = [Row1[0], Row3[1], Row1[2], Row3[3], Row1[4]]
        Line11 = [Row3[0], Row1[1], Row3[2], Row1[3], Row3[4]]
        Line12 = [Row2[0], Row1[1], Row1[2], Row1[3], Row2[4]]
        Line13 = [Row2[0], Row3[1], Row3[2], Row3[3], Row2[4]]
        Line14 = [Row3[0], Row3[1], Row1[2], Row3[3], Row3[4]]  # only this
        Line15 = [Row2[0], Row1[1], Row2[2], Row1[3], Row2[4]]
        Line16 = [Row2[0], Row3[1], Row2[2], Row3[3], Row2[4]]
        Line17 = [Row2[0], Row2[1], Row1[2], Row2[3], Row2[4]]
        Line18 = [Row2[0], Row2[1], Row3[2], Row2[3], Row2[4]]
        Line19 = [Row1[0], Row2[1], Row1[2], Row2[3], Row1[4]]
        Line20 = [Row3[0], Row2[1], Row3[2], Row2[3], Row3[4]]
        status = [Line01, Line02, Line03, Line04, Line05, Line06, Line07, Line08, Line09, Line10, Line11, Line12,
                  Line13, Line14, Line15, Line16, Line17, Line18, Line19, Line20]

        for freek in range(0, len(status)):
            for freej in range(1, len(status[freek]) - 1):
                if status[freek][freej] == "W" and status[freek][freej - 1] != "PIG":
                    status[freek][freej] = status[freek][freej - 1]
            if status[freek][0] == status[freek][1] == status[freek][2] == status[freek][3] == status[freek][4]:
                if status[freek][0] == "A":
                    free_score = free_score + A5 * betMoney
                elif status[freek][0] == "B_1" or status[freek][0] == "B_2":
                    free_score = free_score + B5 * betMoney
                elif status[freek][0] == "C_1" or status[freek][0] == "C_2":
                    free_score = free_score + C5 * betMoney
                elif status[freek][0] == "D_1" or status[freek][0] == "D_2":
                    free_score = free_score + D5 * betMoney
            elif status[freek][0] == status[freek][1] == status[freek][2] == status[freek][3]:
                if status[freek][0] == "A":
                    free_score = free_score + A4 * betMoney
                elif status[freek][0] == "B_1" or status[freek][0] == "B_2":
                    free_score = free_score + B4 * betMoney
                elif status[freek][0] == "C_1" or status[freek][0] == "C_2":
                    free_score = free_score + C4 * betMoney
                elif status[freek][0] == "D_1" or status[freek][0] == "D_2":
                    free_score = free_score + D4 * betMoney
            elif status[freek][0] == status[freek][1] == status[freek][2]:
                if status[freek][0] == "A":
                    free_score = free_score + A3 * betMoney
                elif status[freek][0] == "B_1" or status[freek][0] == "B_2":
                    free_score = free_score + B3 * betMoney
                elif status[freek][0] == "C_1" or status[freek][0] == "C_2":
                    free_score = free_score + C3 * betMoney
                elif status[freek][0] == "D_1" or status[freek][0] == "D_2":
                    free_score = free_score + D3 * betMoney

        for pigI in range(0, 5):
            if Row1Origin[pigI] == "PIG":
                extra_pig()
                extraTime = extraTime + pigMore
                pigNum = pigNum + 1
                pigNumCount = pigNumCount + freePigMoney
                free_score = free_score + freePigMoney
                pigNumMoney= pigNumMoney + freePigMoney
                print(freePigMoney)
            if Row2Origin[pigI] == "PIG":
                extra_pig()
                extraTime = extraTime + pigMore
                pigNum = pigNum + 1
                pigNumCount = pigNumCount + freePigMoney
                free_score = free_score + freePigMoney
                pigNumMoney = pigNumMoney + freePigMoney
                print(freePigMoney)
            if Row3Origin[pigI] == "PIG":
                extra_pig()
                extraTime = extraTime + pigMore
                pigNum = pigNum + 1
                pigNumCount = pigNumCount + freePigMoney
                free_score = free_score + freePigMoney
                pigNumMoney = pigNumMoney + freePigMoney
                print(freePigMoney)

        print(Row1Origin, "\n", Row2Origin, "\n", Row3Origin)
        print("freePigMoney = ", freePigMoney, "  free_score = ", free_score, "  pig_score = ", pigNumCount)
        print("extra game = ", extraTime)

    freeGame = 0
    baseGame = 1
    return extraTime, free_score, Row1Origin, Row2Origin, Row3Origin, freePigMoney, pigNumCount, pigNum, pigNumMoney


#  Let go!
gameTimes = 1
# win = 0
freeTime = 5
freebetTimes = 0
win2 = 0
win3 = 0
win4 = 0

for i in range(0, gameTimes):
    score = 0
    betTimes = betTimes + 1
    coinNum = 0
    coinNumCount = 0
    free_score = 0

    row_1()
    row_2()
    row_3()

    Line01 = [Row1[0], Row1[1], Row1[2], Row1[3], Row1[4]]
    Line02 = [Row2[0], Row2[1], Row2[2], Row2[3], Row2[4]]
    Line03 = [Row3[0], Row3[1], Row3[2], Row3[3], Row3[4]]
    Line04 = [Row1[0], Row2[1], Row3[2], Row2[3], Row1[4]]
    Line05 = [Row3[0], Row2[1], Row1[2], Row2[3], Row3[4]]
    Line06 = [Row1[0], Row1[1], Row2[2], Row1[3], Row1[4]]
    Line07 = [Row3[0], Row3[1], Row2[2], Row3[3], Row3[4]]
    Line08 = [Row1[0], Row2[1], Row2[2], Row2[3], Row1[4]]
    Line09 = [Row3[0], Row2[1], Row2[2], Row2[3], Row3[4]]
    Line10 = [Row1[0], Row3[1], Row1[2], Row3[3], Row1[4]]
    Line11 = [Row3[0], Row1[1], Row3[2], Row1[3], Row3[4]]
    Line12 = [Row2[0], Row1[1], Row1[2], Row1[3], Row2[4]]
    Line13 = [Row2[0], Row3[1], Row3[2], Row3[3], Row2[4]]
    Line14 = [Row3[0], Row3[1], Row1[2], Row3[3], Row3[4]]  # only this
    Line15 = [Row2[0], Row1[1], Row2[2], Row1[3], Row2[4]]
    Line16 = [Row2[0], Row3[1], Row2[2], Row3[3], Row2[4]]
    Line17 = [Row2[0], Row2[1], Row1[2], Row2[3], Row2[4]]
    Line18 = [Row2[0], Row2[1], Row3[2], Row2[3], Row2[4]]
    Line19 = [Row1[0], Row2[1], Row1[2], Row2[3], Row1[4]]
    Line20 = [Row3[0], Row2[1], Row3[2], Row2[3], Row3[4]]
    status = [Line01,Line02,Line03,Line04,Line05,Line06,Line07,Line08,Line09,Line10,Line11,Line12,Line13,Line14,Line15,Line16,Line17,Line18,Line19,Line20]

    for k in range(0, len(status)):
        for j in range(1, len(status[k])-1):
            if status[k][j] == "W" and status[k][j - 1] != "COIN":
                status[k][j] = status[k][j - 1]
        if status[k][0] == status[k][1] == status[k][2] == status[k][3] == status[k][4]:
            if status[k][0] == "A":
                score = score + A5 * betMoney
            elif status[k][0] == "B_1" or status[k][0] == "B_2":
                score = score + B5 * betMoney
            elif status[k][0] == "C_1" or status[k][0] == "C_2":
                score = score + C5 * betMoney
            elif status[k][0] == "D_1" or status[k][0] == "D_2":
                score = score + D5 * betMoney
        elif status[k][0] == status[k][1] == status[k][2] == status[k][3]:
            if status[k][0] == "A":
                score = score + A4 * betMoney
            elif status[k][0] == "B_1" or status[k][0] == "B_2":
                score = score + B4 * betMoney
            elif status[k][0] == "C_1" or status[k][0] == "C_2":
                score = score + C4 * betMoney
            elif status[k][0] == "D_1" or status[k][0] == "D_2":
                score = score + D4 * betMoney
        elif status[k][0] == status[k][1] == status[k][2]:
            if status[k][0] == "A":
                score = score + A3 * betMoney
            elif status[k][0] == "B_1" or status[k][0] == "B_2":
                score = score + B3 * betMoney
            elif status[k][0] == "C_1" or status[k][0] == "C_2":
                score = score + C3 * betMoney
            elif status[k][0] == "D_1" or status[k][0] == "D_2":
                score = score + D3 * betMoney

    for coinI in range(0, 5):
        if Row1Origin[coinI] == "COIN":
            coin_value()
            coinNum = coinNum + 1
            coinNumCount = coinNumCount + betMoney * coinMore
        if Row2Origin[coinI] == "COIN":
            coin_value()
            coinNum = coinNum + 1
            coinNumCount = coinNumCount + betMoney * coinMore
        if Row3Origin[coinI] == "COIN":
            coin_value()
            coinNum = coinNum + 1
            coinNumCount = coinNumCount + betMoney * coinMore

    if coinNum > 4:         # enter free game
        freeGameTime = freeGameTime + 1
        # pigNum = 0
        pigNumCount = 0
        coinNum = 0
        print("we get one", "betMoney * coinMore = ", betMoney * coinMore, coinMore)
        print(Row1Origin, "\n", Row2Origin, "\n", Row3Origin)

        free_game(freeTime, coinNumCount)

        while extraTime > 0:
            free_game(extraTime, coinNumCount)

    # bonus 部分模块
    coinTotal = coinTotal + coinNum                   # bonus 部分模块
    meter = meter + coinNum                           # meter 渐进
    if coinTotal > 0:
        bonusBaseMoney = (bonusBaseMoney * (coinTotal - coinNum) + coinNumCount) / coinTotal    # bonus中奖励面额数值基于获得coin的bet数
    if 100 <= meter < 116 and 100 <= coinTotal < 116:                         # bonus 奖励1-1
        bonusEnhance()
        meter = 0                           # 累积进度清空
        bonusWheelScore = bonusWheelScore + bonusWin * bonusBaseMoney         # bonus轮盘获得奖励
        print(bonusWheelScore)
        if bonusStatus == "bonus_1_win":
            bonusEnhanceStatus_1 = 1
    # elif 100 <= meter < 116 and 200 <= coinTotal < 216:                         # bonus 奖励1-2
    #     bonusEnhance()
    #     meter = 0                           # 累积进度清空
    #     bonusWheelScore = bonusWheelScore + bonusWin * bonusBaseMoney         # bonus轮盘获得奖励
    #     print(bonusWheelScore)
    #     if bonusStatus == "bonus_1_win":
    #         bonusEnhanceStatus_2 = 1
    # elif 100 <= meter < 116 and 300 <= coinTotal < 316:                         # bonus 银行01
    #     bonusEnhance()
    #     meter = 0                           # 累积进度清空
    #     # [加5次，加pig额度，加pig数，加row，加col]
    #     if bonusEnhanceStatus_1 == 1:
    #         freeTime = freeTime + 5
    #     if bonusEnhanceStatus_2 == 1:
    #         bonusBaseMoney = bonusBaseMoney * 2
    #     bonus_free_game(freeTime, bonusBaseMoney)
    #     while extraTime > 0:
    #         bonus_free_game(extraTime, bonusBaseMoney)
    #     if bonusEnhanceStatus_2 == 1:
    #         bonusBaseMoney = bonusBaseMoney / 2
    #     bonusEnhanceStatus_1 = 0
    #     bonusEnhanceStatus_2 = 0
    #     # 放一个free game
    # elif 100 <= meter < 116 and 400 <= coinTotal < 416:                         # bonus 奖励2-1
    #     bonusEnhance()
    #     meter = 0                           # 累积进度清空
    #     bonusWheelScore = bonusWheelScore + bonusWin * bonusBaseMoney         # bonus轮盘获得奖励
    #     if bonusStatus == "bonus_1_win":
    #         bonusEnhanceStatus_1 = 1
    # elif 100 <= meter < 116 and 500 <= coinTotal < 516:                         # bonus 奖励2-2
    #     bonusEnhance()
    #     meter = 0                           # 累积进度清空
    #     bonusWheelScore = bonusWheelScore + bonusWin * bonusBaseMoney         # bonus轮盘获得奖励
    #     if bonusStatus == "bonus_1_win":
    #         bonusEnhanceStatus_2 = 1
    # elif 100 <= meter < 116 and 600 <= coinTotal < 616:                         # bonus 奖励2-3
    #     bonusEnhance()
    #     meter = 0                           # 累积进度清空
    #     bonusWheelScore = bonusWheelScore + bonusWin * bonusBaseMoney         # bonus轮盘获得奖励
    #     if bonusStatus == "bonus_1_win":
    #         bonusEnhanceStatus_3 = 1
    # elif 100 <= meter < 116 and 700 <= coinTotal < 716:                         # bonus 银行02
    #     bonusEnhance()
    #     meter = 0                           # 累积进度清空
    #     # [加5次，加pig额度，加pig数，加row，加col]
    #     if bonusEnhanceStatus_1 == 1:
    #         freeTime = freeTime + 5
    #     if bonusEnhanceStatus_2 == 1:
    #         bonusBaseMoney = bonusBaseMoney * 2
    #     if bonusEnhanceStatus_3 == 1:
    #         PiggyWeight = PiggyWeight * 2
    #     bonus_free_game(freeTime, bonusBaseMoney)
    #     while extraTime > 0:
    #         bonus_free_game(extraTime, bonusBaseMoney)
    #     if bonusEnhanceStatus_2 == 1:
    #         bonusBaseMoney = bonusBaseMoney / 2
    #     if bonusEnhanceStatus_3 == 1:
    #         PiggyWeight = PiggyWeight / 2
    #     bonusEnhanceStatus_1 = 0
    #     bonusEnhanceStatus_2 = 0
    #     bonusEnhanceStatus_3 = 0
    #
    # elif 100 <= meter < 116 and 800 <= coinTotal < 816:                         # bonus 奖励3-1
    #     bonusEnhance()
    #     meter = 0                           # 累积进度清空
    #     bonusWheelScore = bonusWheelScore + bonusWin * bonusBaseMoney         # bonus轮盘获得奖励
    #     if bonusStatus == "bonus_1_win":
    #         bonusEnhanceStatus_1 = 1
    # elif 100 <= meter < 116 and 900 <= coinTotal < 916:                         # bonus 奖励3-2
    #     bonusEnhance()
    #     meter = 0                           # 累积进度清空
    #     bonusWheelScore = bonusWheelScore + bonusWin * bonusBaseMoney         # bonus轮盘获得奖励
    #     if bonusStatus == "bonus_1_win":
    #         bonusEnhanceStatus_2 = 1
    # elif 100 <= meter < 116 and 1000 <= coinTotal < 1016:                         # bonus 奖励3-3
    #     bonusEnhance()
    #     meter = 0                           # 累积进度清空
    #     bonusWheelScore = bonusWheelScore + bonusWin * bonusBaseMoney         # bonus轮盘获得奖励
    #     if bonusStatus == "bonus_1_win":
    #         bonusEnhanceStatus_3 = 1
    # elif 100 <= meter < 116 and 1100 <= coinTotal < 1016:                         # bonus 奖励3-4
    #     bonusEnhance()
    #     meter = 0                           # 累积进度清空
    #     bonusWheelScore = bonusWheelScore + bonusWin * bonusBaseMoney         # bonus轮盘获得奖励
    #     if bonusStatus == "bonus_1_win":
    #         bonusEnhanceStatus_4 = 1
    # elif 100 <= meter < 116 and 1200 <= coinTotal < 1216:                         # bonus 银行03
    #     bonusEnhance()
    #     meter = 0                           # 累积进度清空
    #     # [加5次，加pig额度，加pig数，加row，加col]
    #     if bonusEnhanceStatus_1 == 1:
    #         freeTime = freeTime + 5
    #     if bonusEnhanceStatus_2 == 1:
    #         bonusBaseMoney = bonusBaseMoney * 2
    #     if bonusEnhanceStatus_3 == 1:
    #         PiggyWeight = PiggyWeight * 2
    #     bonus_free_game(freeTime, bonusBaseMoney)
    #     while extraTime > 0:
    #         bonus_free_game(extraTime, bonusBaseMoney)
    #     if bonusEnhanceStatus_2 == 1:
    #         bonusBaseMoney = bonusBaseMoney / 2
    #     if bonusEnhanceStatus_3 == 1:
    #         PiggyWeight = PiggyWeight / 2
    #     bonusEnhanceStatus_1 = 0
    #     bonusEnhanceStatus_2 = 0
    #     bonusEnhanceStatus_3 = 0
    #     bonusEnhanceStatus_4 = 0
    #
    # elif 100 <= meter < 116 and 1300 <= coinTotal < 1316:                         # bonus 奖励4-1
    #     bonusEnhance()
    #     meter = 0                           # 累积进度清空
    #     bonusWheelScore = bonusWheelScore + bonusWin * bonusBaseMoney         # bonus轮盘获得奖励
    #     if bonusStatus == "bonus_1_win":
    #         bonusEnhanceStatus_1 = 1
    # elif 100 <= meter < 116 and 1400 <= coinTotal < 1416:                         # bonus 奖励4-2
    #     bonusEnhance()
    #     meter = 0                           # 累积进度清空
    #     bonusWheelScore = bonusWheelScore + bonusWin * bonusBaseMoney         # bonus轮盘获得奖励
    #     if bonusStatus == "bonus_1_win":
    #         bonusEnhanceStatus_2 = 1
    # elif 100 <= meter < 116 and 1500 <= coinTotal < 1516:                         # bonus 奖励4-3
    #     bonusEnhance()
    #     meter = 0                           # 累积进度清空
    #     bonusWheelScore = bonusWheelScore + bonusWin * bonusBaseMoney         # bonus轮盘获得奖励
    #     if bonusStatus == "bonus_1_win":
    #         bonusEnhanceStatus_3 = 1
    # elif 100 <= meter < 116 and 1600 <= coinTotal < 1616:                         # bonus 奖励4-4
    #     bonusEnhance()
    #     meter = 0                           # 累积进度清空
    #     bonusWheelScore = bonusWheelScore + bonusWin * bonusBaseMoney         # bonus轮盘获得奖励
    #     if bonusStatus == "bonus_1_win":
    #         bonusEnhanceStatus_4 = 1
    # elif 100 <= meter < 116 and 1700 <= coinTotal < 1716:                         # bonus 奖励4-5
    #     bonusEnhance()
    #     meter = 0                           # 累积进度清空
    #     bonusWheelScore = bonusWheelScore + bonusWin * bonusBaseMoney         # bonus轮盘获得奖励
    #     if bonusStatus == "bonus_1_win":
    #         bonusEnhanceStatus_5 = 1
    # elif 100 <= meter < 116 and 1800 <= coinTotal < 1816:                         # bonus 银行05
    #     bonusEnhance()
    #     meter = 0                           # 累积进度清空
    #     coinTotal = 0                       # coin计算清空
    #     # [加5次，加pig额度，加pig数，加row，加col]
    #     if bonusEnhanceStatus_1 == 1:
    #         freeTime = freeTime + 5
    #     if bonusEnhanceStatus_2 == 1:
    #         bonusBaseMoney = bonusBaseMoney * 2
    #     if bonusEnhanceStatus_3 == 1:
    #         PiggyWeight = PiggyWeight * 2
    #     bonus_free_game(freeTime, bonusBaseMoney)
    #     while extraTime > 0:
    #         bonus_free_game(extraTime, bonusBaseMoney)
    #     if bonusEnhanceStatus_2 == 1:
    #         bonusBaseMoney = bonusBaseMoney / 2
    #     if bonusEnhanceStatus_3 == 1:
    #         PiggyWeight = PiggyWeight / 2
    #     bonusEnhanceStatus_1 = 0
    #     bonusEnhanceStatus_2 = 0
    #     bonusEnhanceStatus_3 = 0
    #     bonusEnhanceStatus_4 = 0
    #     bonusEnhanceStatus_5 = 0

    jackpotPart = jackpotPart + jackpotScore
    print("Jackpot = ", jackpotStatus, "   ", "free Game Time = ", freeGameTime, "   ","meter = ", meter)
    print(Row1Origin, "\n", Row2Origin, "\n", Row3Origin)
    print("score = ", score, "   ", "jackpot = ", jackpotPart, "   ", "coinNum = ", coinNum)
    win = win + free_score + score + jackpotPart   #    + bonusWheelScore
    win2 = win2 + score
    win3 = win3 + free_score
    win4 = win4 + jackpotPart
    print("win = ", win, "   ", "spin times = ", betTimes, "   ", "free times = ", freebetTimes, "\n", "   ")
    print("win = ", win, "   ", 'score = ', win2, "   ", "free_score = ", win3, "   ", "jackpotPart = ", win4)
    with open("D://Bole//Code//test_Demo//test.csv", 'a+', newline='') as t_file:
        csv_writer = csv.writer(t_file)
        csv_writer.writerow([betTimes, win, coinTotal,meter,bonusBaseMoney,bonusEnhanceStatus_1,bonusEnhanceStatus_2,bonusEnhanceStatus_3,bonusEnhanceStatus_4,bonusEnhanceStatus_5])

    print("pigNum = ", pigNum, "pigNumMoney = ", pigNumMoney)



