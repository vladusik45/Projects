from datetime import datetime
from datetime import timedelta
import codecs
from parser1 import parser
from gsheet import captures_add

with codecs.open('win_capt.txt', 'r', 'utf-8') as file: date_from = file.readlines()[-1]
date_from = (datetime.strptime(date_from, '%d.%m.%Y') + timedelta(days= 1)).strftime('%d.%m.%Y')

# , date_from_text= date_from
parser('null', 'captures\zabiv', 'Забивает ', True, enter_exit=False, date_from_text= date_from)
parser('null', 'captures\captures_guns', ' войн ', clear=True, enter_exit=True, date_from_text= date_from)

file_zabiv = codecs.open("captures\zabiv.txt", "r", "utf-8")
scores = file_zabiv.read().splitlines()
scores.pop(0)
file_captures_guns = codecs.open("captures\captures_guns.txt", "r", "utf-8")
captures_guns = file_captures_guns.read().splitlines()
captures_guns.pop(0)
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
        list_atack = score.split('Забивает')[0].split()[2:]
        atack = ''
        for i in range(len(list_atack)):
            if i != len(list_atack)-1:
                atack+= list_atack[i] + ' '
            else: atack += list_atack[i]
        defend = score.split(' против ')[1].split(' на ')[0]
        captures.append([score, [[], []], [], [atack, defend]])
        # 0 - строка забива, 1-0 - входы за атаку, 1-1 входы за защиту, 2 - добыча, 3 - стороны атаки и защиты
        time_log = score.split()[-2] + ' ' + score.split()[-1]
        time = datetime.strptime(time_log, '%d.%m.%Y, %H:%M:%S')
        ca_time.append(time)
        ca_scoring_number.append(time_log[6:10] + '-' + str(int(time_log[:2])) + '-' + str(int(time_log[3:5])) + '-' + score.split('#')[1].split()[0])
        ca_players_number_and_caliber.append(score.split(', ')[1])
        ca_square.append(score.split(' на ')[1].split()[1][3:])
        ca_winning_side.append('')
        ca_actual_players_number.append([0, 0])
    if 'стрелу' in score:
        list_atack = score.split('Забивает')[0].split()[2:]
        atack = ''
        for i in range(len(list_atack)):
            if i != len(list_atack)-1:
                atack+= list_atack[i] + ' '
            else: atack += list_atack[i]
        defend = score.split(' против ')[1].split(' на ')[0]
        bizwars.append([score, [[], []], [], [atack, defend]])
        time_log = score.split()[-2] + ' ' + score.split()[-1]
        time = datetime.strptime(time_log, '%d.%m.%Y, %H:%M:%S')
        b_time.append(time)
        b_scoring_number.append(time_log[6:10] + '-' + str(int(time_log[:2])) + '-' + str(int(time_log[3:5])) + '-' + score.split('#')[1].split()[0])
        b_players_number_and_caliber.append(score.split(', ')[1])
        b_square.append(score.split(' против ')[0].split(' за ')[1])
        b_winning_side.append('')
        b_actual_players_number.append([0, 0])

for log_c_g in captures_guns:
    time_log = log_c_g.split()[-2] + ' ' + log_c_g.split()[-1]
    time = datetime.strptime(time_log, '%d.%m.%Y, %H:%M:%S')
    if 'Входит' in log_c_g:
        if 'Мафия' in log_c_g:
            for b_num in range(0, len(b_time)):
                time_difference = time - b_time[b_num]
                minutes_difference = time_difference.total_seconds() / 60
                list_faction = log_c_g.split('Входит')[0].split()[2:]
                faction = ''
                for i in range(len(list_faction)):
                    if i != len(list_faction)-1:
                        faction+= list_faction[i] + ' '
                else: faction += list_faction[i]
                if minutes_difference < 34 and minutes_difference > 0 and faction in bizwars[b_num][0] and log_c_g.split('#')[1].split()[0] == bizwars[b_num][0].split('#')[1].split()[0]:
                    if bizwars[b_num][3][0] in log_c_g:
                        bizwars[b_num][1][0].append(log_c_g)
                    else:
                        bizwars[b_num][1][1].append(log_c_g)
        else:
            for ca_num in range(0, len(ca_time)):
                time_difference = time - ca_time[ca_num]
                minutes_difference = time_difference.total_seconds() / 60
                list_faction = log_c_g.split('Входит')[0].split()[2:]
                faction = ''
                for i in range(len(list_faction)):
                    if i != len(list_faction)-1:
                        faction+= list_faction[i] + ' '
                else: faction += list_faction[i]
                if minutes_difference < 34 and minutes_difference > 0 and faction in captures[ca_num][0] and log_c_g.split('#')[1].split()[0] == captures[ca_num][0].split('#')[1].split()[0]:
                    if captures[ca_num][3][0] in log_c_g:
                        captures[ca_num][1][0].append(log_c_g)
                    else:
                        captures[ca_num][1][1].append(log_c_g)
    if 'Добыча' in log_c_g:
        if 'Мафия' in log_c_g:
            for b_num in range(0, len(b_time)):
                time_difference = time - b_time[b_num]
                minutes_difference = time_difference.total_seconds() / 60
                list_faction = log_c_g.split('Добыча')[0].split()[2:]
                faction = ''
                for i in range(len(list_faction)):
                    if i != len(list_faction)-1:
                        faction+= list_faction[i] + ' '
                else: faction += list_faction[i]
                if minutes_difference < 46 and minutes_difference > 0 and faction in bizwars[b_num][0]:
                    bizwars[b_num][2].append(log_c_g)
        else:
            for ca_num in range(0, len(ca_time)):
                time_difference = time - ca_time[ca_num]
                minutes_difference = time_difference.total_seconds() / 60
                list_faction = log_c_g.split('Добыча')[0].split()[2:]
                faction = ''
                for i in range(len(list_faction)):
                    if i != len(list_faction)-1:
                        faction+= list_faction[i] + ' '
                else: faction += list_faction[i]
                if minutes_difference < 46 and minutes_difference > 0 and faction in captures[ca_num][0]:
                    captures[ca_num][2].append(log_c_g)
    if 'Отменяет' in log_c_g:
        if 'Мафия' in log_c_g:
            for b_num in range(0, len(b_time)):
                time_difference = time - b_time[b_num]
                minutes_difference = time_difference.total_seconds() / 60
                if minutes_difference < 29 and minutes_difference > 0 and log_c_g.split('#')[1].split()[0] in bizwars[b_num][0]:
                    b_winning_side[b_num] = 'ОТМЕНЕН'
        else: 
            for ca_num in range(0, len(ca_time)):
                time_difference = time - ca_time[ca_num]
                minutes_difference = time_difference.total_seconds() / 60
                if minutes_difference < 29 and minutes_difference > 0 and log_c_g.split('#')[1].split()[0] in captures[ca_num][0]:
                    ca_winning_side[ca_num] = 'ОТМЕНЕН'
        
for ca_num in range(0, len(captures)):
    if ca_winning_side[ca_num] != 'ОТМЕНЕН':
        if len(captures[ca_num][1][0]) > 0:
            if len(captures[ca_num][1][1]) > 0:
                if len(captures[ca_num][2]) > 0:
                    if captures[ca_num][3][1] in captures[ca_num][2][0]:
                        ca_winning_side[ca_num] = captures[ca_num][3][1]
                    else:
                        ca_winning_side[ca_num] = captures[ca_num][3][0]
                else: ca_winning_side[ca_num] = 'Нет информации'
            else: ca_winning_side[ca_num] = captures[ca_num][3][0]
        else: ca_winning_side[ca_num] = captures[ca_num][3][1]
        ca_actual_players_number[ca_num][0] = len(captures[ca_num][1][0])
        ca_actual_players_number[ca_num][1] = len(captures[ca_num][1][1])

for b_num in range(0, len(bizwars)):
    if b_winning_side[b_num] != 'ОТМЕНЕН':
        if len(bizwars[b_num][1][0]) > 0:
            if len(bizwars[b_num][1][1]) > 0:
                if len(bizwars[b_num][2]) > 0:
                    if bizwars[b_num][3][1] in bizwars[b_num][2][0]:
                        b_winning_side[b_num] = bizwars[b_num][3][1]
                    else:
                        b_winning_side[b_num] = bizwars[b_num][3][0]
                else: b_winning_side[b_num] = 'Нет информации'
            else: b_winning_side[b_num] = bizwars[b_num][3][0]
        else: b_winning_side[b_num] = bizwars[b_num][3][1]
        b_actual_players_number[b_num][0] = len(bizwars[b_num][1][0])
        b_actual_players_number[b_num][1] = len(bizwars[b_num][1][1])

def write_win_captures(num, _time, _scoring_number, _winning_side):
    with codecs.open('win_capt.txt', 'a', "utf-8") as file:
        time = _time[num].strftime('%d.%m')
        file.write('\n'+ time + '_' + _scoring_number[num] + '_' + _winning_side[num])

for ca_num in range(0, len(captures)):
    players_atack = ''
    players_def = ''
    for i in captures[ca_num][1][0]:
        players_atack += i.split('_')[0].split()[-1] + '_' + i.split('_')[1].split()[0] + '\n'
    for i in captures[ca_num][1][1]:
        players_def += i.split('_')[0].split()[-1] + '_' + i.split('_')[1].split()[0] + '\n'
    captures_add(ca_scoring_number[ca_num], ca_square[ca_num], ca_players_number_and_caliber[ca_num], ca_winning_side[ca_num], captures[ca_num][3][1], 
                 str(ca_actual_players_number[ca_num][1]), captures[ca_num][3][0], str(ca_actual_players_number[ca_num][0]), players_def, players_atack, 'capt')
    write_win_captures(ca_num, ca_time, ca_scoring_number, ca_winning_side)
    print(ca_num)

for b_num in range(0, len(bizwars)):
    players_atack = ''
    players_def = ''
    for i in bizwars[b_num][1][0]:
        players_atack += i.split('_')[0].split()[-1] + '_' + i.split('_')[1].split()[0] + '\n'
    for i in bizwars[b_num][1][1]:
        players_def += i.split('_')[0].split()[-1] + '_' + i.split('_')[1].split()[0] + '\n'
    captures_add(b_scoring_number[b_num], b_square[b_num], b_players_number_and_caliber[b_num], b_winning_side[b_num], bizwars[b_num][3][1], 
                 str(b_actual_players_number[b_num][1]), bizwars[b_num][3][0], str(b_actual_players_number[b_num][0]), players_def, players_atack, 'biz')
    write_win_captures(b_num, b_time, b_scoring_number, b_winning_side)
    print(b_num)
with codecs.open('win_capt.txt', 'a', "utf-8") as file: file.write('\n' + b_time[len(bizwars)-1].strftime('%d.%m.%Y'))