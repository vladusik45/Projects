import gspread
from time import sleep

sa = gspread.service_account()
shGhetto = sa.open("Ghetto Hawick")
shMafia = sa.open("Mafia Hawick")
wksGhetto = shGhetto.worksheet('Capture')
wksMafia = shMafia.worksheet('Bizwar')

def faction_activity():
    wks = shGhetto.worksheet('MG')

    mg = 0
    army_supply = [[1, 2, ['ghbdn']], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []]]

    wks.update('A2:M2', [['', 'Army/EMS', 'Нападения FZ/FP', 'Ганшоп', 'GW за день', 'Поезд', 'ВЗХ', 'win cpt', 'Похищения', 'Проезд мимо', 'Мп / ГМП', '', 'Дополнительная иформация']])
    wks.update('A3:M3', [['', f'{army_supply[mg][0]} ({army_supply[mg][2]})']])

    for i in range(1, 11):
        wks.update_cell(i+2, 1, f'{i+20}.01')

    wks.update('O3:O4', [['=B3*4'], ['=B4*5']])

factions = ['MG', 'BSG', 'ESB', 'LSV', 'FAM', 'Capture']

def captures_add(number_zabiv, territory, conditional, winner, f_def, count_def, f_atack, count_atack, players_def, players_atack, capt_biz):
    row_values = [number_zabiv, territory, conditional, winner, f_def, count_def, f_atack, count_atack, players_def, players_atack]
    sleep(2)
    if capt_biz == 'capt':
        wksGhetto.append_row(value_input_option='USER_ENTERED', values= row_values)
    else:
        wksMafia.append_row(value_input_option='USER_ENTERED', values= row_values)
    
    

# Поставки Army	Поставки EMS	FZ	FP	Ганшоп	Победы GW	Поезд	ВЗХ	win cpt	Флаг	Вагонетка

def append_faction_logs(list_table, date, count_army_supply, army_supplys, count_ems_supply, ems_supplys, count_fz, materials_fz, count_ft, 
                        ft, win_ammun, all_amun, materials_ammun, gw, win_train, all_train, res_train, hammers, captures, flag, cargo_escort, airdrop):
    wks = shGhetto.worksheet(list_table)

    row_values = [date, count_army_supply, army_supplys, count_ems_supply, ems_supplys, count_fz, materials_fz, count_ft, 
                  ft, win_ammun, all_amun, materials_ammun, gw, win_train, all_train, res_train, hammers, captures, flag, cargo_escort, airdrop]
    wks.append_row(value_input_option='USER_ENTERED', values= row_values)

def append_empty_row(list_table):
    wks = shGhetto.worksheet(list_table)
    row_values = ['_']
    wks.append_row(value_input_option='USER_ENTERED', values= row_values)
