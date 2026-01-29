from datetime import datetime
from datetime import timedelta
import codecs
from parser1 import parser
from gsheet import captures_add

# parser('null', 'captures\zabiv', 'Забивает ', True)
# parser('null', 'captures\captures_guns', ' войн ', True)

file_zabiv = codecs.open("captures\zabiv.txt", "r", "utf-8")
scores = file_zabiv.read().splitlines()
file_captures_guns = codecs.open("captures\captures_guns.txt", "r", "utf-8")
captures_guns = file_captures_guns.read().splitlines()
scores.reverse()
captures_guns.reverse()
captures = []
ca_time = []
ca_scoring_number = []
ca_square = []
ca_winning_side = []
ca_players_number_and_caliber = []
ca_actual_players_number = []

bizwars = []
b_time = []
b_scoring_number = []
b_square = []
b_winning_side = []
b_players_number_and_caliber = []
b_actual_players_number = []

# 48	Shofer_Banhammer	Los Santos Vagos	Забивает войну за территорию #3 против The Ballas Gang на квадрат ID:51 на 16:47, 7x7 на 11.43mm, алкоголь/анальгетики, броня разрешены	04.02.2024, 16:17:51
# 52	Boketto_Inoue	Японская Мафия	Забивает стрелу #8 за Барбершоп #2 против Русская Мафия на 18:49, 8x8 на 11.43mm, алкоголь/анальгетики, косяки/SPANK разрешены	04.02.2024, 18:19:23

for score in scores:
    if 'войну за территорию' in score:
        log_split = score.split("\t")
        defend = log_split[3].split(' против ')[1].split(' на ')[0]
        captures.append([score, [[], []], [], [log_split[2], defend]])
        # 0 - строка забива, 1-0 - входы за атаку, 1-1 входы за защиту, 2 - добыча, 3 - стороны атаки и защиты
        time_log = datetime.strptime(log_split[-1], '%d.%m.%Y, %H:%M:%S')
        ca_time.append(time_log)
        ca_scoring_number.append(log_split[-1][6:10] + '-' + str(int(log_split[-1][:2])) + '-' + str(int(log_split[-1][3:5])) + '-' + log_split[3].split()[4][1:])
        ca_players_number_and_caliber.append(log_split[3].split(', ')[1])
        ca_square.append(log_split[3].split(' на ')[1].split()[1][3:])
        ca_winning_side.append('')
        ca_actual_players_number.append([0, 0])
    if 'стрелу' in score:
        log_split = score.split("\t")
        defend = log_split[3].split(' против ')[1].split(' на ')[0]
        bizwars.append([score, [[], []], [], [log_split[2], defend]])
        time_log = datetime.strptime(log_split[-1], '%d.%m.%Y, %H:%M:%S')
        b_time.append(time_log)
        b_scoring_number.append(log_split[-1][6:10] + '-' + str(int(log_split[-1][:2])) + '-' + str(int(log_split[-1][3:5])) + '-' + log_split[3].split()[2][1:])
        b_players_number_and_caliber.append(log_split[3].split(', ')[1])
        b_square.append(log_split[3].split(' против ')[0].split(' за ')[1])
        b_winning_side.append('')
        b_actual_players_number.append([0, 0])

for log_c_g in captures_guns:
    log_split = log_c_g.split("\t")
    time_log = datetime.strptime(log_split[-1], '%d.%m.%Y, %H:%M:%S')
    if 'Входит' in log_c_g:
        if 'Мафия' in log_c_g:
            for b_num in range(0, len(b_time)):
                time_difference = time_log - b_time[b_num]
                minutes_difference = time_difference.total_seconds() / 60
                if minutes_difference < 34 and minutes_difference > 0 and log_split[2] in bizwars[b_num][0]:
                    if bizwars[b_num][3][0] in log_c_g:
                        bizwars[b_num][1][0].append(log_c_g)
                    else:
                        bizwars[b_num][1][1].append(log_c_g)
        else:
            for ca_num in range(0, len(ca_time)):
                time_difference = time_log - ca_time[ca_num]
                minutes_difference = time_difference.total_seconds() / 60
                if minutes_difference < 34 and minutes_difference > 0 and log_split[2] in captures[ca_num][0]:
                    if captures[ca_num][3][0] in log_c_g:
                        captures[ca_num][1][0].append(log_c_g)
                    else:
                        captures[ca_num][1][1].append(log_c_g)
    if 'Добыча' in log_c_g:
        if 'Мафия' in log_c_g:
            for b_num in range(0, len(b_time)):
                time_difference = time_log - b_time[b_num]
                minutes_difference = time_difference.total_seconds() / 60
                if minutes_difference < 46 and minutes_difference > 0 and log_split[2] in bizwars[b_num][0]:
                    bizwars[b_num][2].append(log_c_g)
        else:
            for ca_num in range(0, len(ca_time)):
                time_difference = time_log - ca_time[ca_num]
                minutes_difference = time_difference.total_seconds() / 60
                if minutes_difference < 46 and minutes_difference > 0 and log_split[2] in captures[ca_num][0]:
                    captures[ca_num][2].append(log_c_g)
    if 'Отменяет' in log_c_g:
        if 'Мафия' in log_c_g:
            for b_num in range(0, len(b_time)):
                time_difference = time_log - b_time[b_num]
                minutes_difference = time_difference.total_seconds() / 60
                if minutes_difference < 29 and minutes_difference > 0 and log_split[3].split()[2] in bizwars[b_num][0]:
                    b_winning_side[b_num] = 'ОТМЕНЕН'
        else: 
            for ca_num in range(0, len(ca_time)):
                time_difference = time_log - ca_time[ca_num]
                minutes_difference = time_difference.total_seconds() / 60
                if minutes_difference < 29 and minutes_difference > 0 and log_split[3].split()[2] in captures[ca_num][0]:
                    ca_winning_side[ca_num] = 'ОТМЕНЕН'
        
for ca_num in range(0, len(captures)):
    if ca_winning_side[ca_num] != 'ОТМЕНЕН':
        if len(captures[ca_num][1][0]) > 0:
            if len(captures[ca_num][1][1]) > 0:
                if captures[ca_num][3][1] in captures[ca_num][2][1]:
                    ca_winning_side[ca_num] = captures[ca_num][3][1]
                else:
                    ca_winning_side[ca_num] = captures[ca_num][3][0]
            else: ca_winning_side[ca_num] = captures[ca_num][3][0]
        else: ca_winning_side[ca_num] = captures[ca_num][3][1]
        ca_actual_players_number[ca_num][0] = len(captures[ca_num][1][0])
        ca_actual_players_number[ca_num][1] = len(captures[ca_num][1][1])

for b_num in range(0, len(bizwars)):
    if b_winning_side[b_num] != 'ОТМЕНЕН':
        if len(bizwars[b_num][1][0]) > 0:
            if len(bizwars[b_num][1][1]) > 0:
                if bizwars[b_num][3][1] in bizwars[b_num][2][1]:
                    b_winning_side[b_num] = bizwars[b_num][3][1]
                else:
                    b_winning_side[b_num] = bizwars[b_num][3][0]
            else: b_winning_side[b_num] = bizwars[b_num][3][0]
        else: b_winning_side[b_num] = bizwars[b_num][3][1]
        b_actual_players_number[b_num][0] = len(bizwars[b_num][1][0])
        b_actual_players_number[b_num][1] = len(bizwars[b_num][1][1])

for ca_num in range(0, len(captures)):
    players_atack = ''
    players_def = ''
    for i in captures[ca_num][1][0]:
        players_atack += i.split('\t')[1] + '\n'
    for i in captures[ca_num][1][1]:
        players_def += i.split('\t')[1] + '\n'
    captures_add(ca_scoring_number[ca_num], ca_square[ca_num], ca_players_number_and_caliber[ca_num], ca_winning_side[ca_num], captures[ca_num][3][1], 
                 str(ca_actual_players_number[ca_num][1]), captures[ca_num][3][0], str(ca_actual_players_number[ca_num][0]), players_def, players_atack)


# for b_num in range(0, len(bizwars)):
#     players_atack = ''
#     players_def = ''
#     for i in bizwars[b_num][1][0]:
#         players_atack += i.split('\t')[1] + '\n'
#     for i in bizwars[b_num][1][1]:
#         players_def += i.split('\t')[1] + '\n'
#     captures_add(b_scoring_number[b_num], b_square[b_num], b_players_number_and_caliber[b_num], b_winning_side[b_num], bizwars[b_num][3][1], 
#                  str(b_actual_players_number[b_num][1]), bizwars[b_num][3][0], str(b_actual_players_number[b_num][0]), players_def, players_atack)
