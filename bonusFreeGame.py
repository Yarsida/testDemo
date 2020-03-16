import numpy as np

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
freebetTimes = 0
free_score = 0
pigNumCount = 0
pigNum = 0

pigChanceValue = [1, 10]            # pig中获取额外free game的随机模块
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
    else:
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
    else:
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
    else:
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
    else:
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
    else:
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


def bonus_free_game(x, y):
    global freebetTimes, coinNum, coinNumCount, free_score, betMoney, pigNum, pigNumCount, extraTime, freeGame, baseGame
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
                if status[freek][freej] == "W":
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
            if Row2Origin[pigI] == "PIG":
                extra_pig()
                extraTime = extraTime + pigMore
                pigNum = pigNum + 1
                pigNumCount = pigNumCount + freePigMoney
                free_score = free_score + freePigMoney
            if Row3Origin[pigI] == "PIG":
                extra_pig()
                extraTime = extraTime + pigMore
                pigNum = pigNum + 1
                pigNumCount = pigNumCount + freePigMoney
                free_score = free_score + freePigMoney

        print(Row1Origin, "\n", Row2Origin, "\n", Row3Origin)
        print("freePigMoney = ", freePigMoney, "  free_score = ", free_score, "  pig_score = ", pigNumCount)
        print("extra game = ", extraTime)

    freeGame = 0
    baseGame = 1
    return extraTime, free_score, Row1Origin, Row2Origin, Row3Origin, freePigMoney, pigNumCount


bonus_free_game(5, 1)