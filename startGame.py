import os
import csv

with open("./test.csv", 'a+', newline='') as t_file:
    csv_writer = csv.writer(t_file)
    csv_writer.writerow(["spin", "win", "coinTotal", 'meter', 'bonusBaseMoney', 'bonusEnhanceStatus_1', 'bonusEnhanceStatus_2','bonusEnhanceStatus_3','bonusEnhanceStatus_4','bonusEnhanceStatus_5'])
    csv_writer.writerow([0,0,0,0,0,0,0,0,0,0])

    # os.system('python ./baseGame.py')
