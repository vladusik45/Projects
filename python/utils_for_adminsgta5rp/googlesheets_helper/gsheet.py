import gspread

sa = gspread.service_account()
sh = sa.open("TestTable")

factions = [["Marabunta Grande", "Marabunta"], ["The Families", "Families"], ["Los Santos Vagos", "Los"], ["Bloods", "Bloods"], ["The Ballas Gang", "Ballas"], 
            ["Русская Мафия", "Русская"], ["Армянская Мафия", "Армянская"], ["Мексиканская Мафия", "Мексиканская"], ["Итальянская Мафия", "Итальянская"], ["Японская Мафия", "Японская"], 
            ["LSPD", ""], ["LSSD", ""], ["FIB", ""], ["LS Army", ""], ["Федеральная тюрьма", ""], ["Мэрия ЛС", ""], ["Medical Services", ""]]

army_supply = [[1, 2, ['ghbdn']], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []], [0, 0, []]]
num = 0
count = 3
date = '21.01'
# wks.update('B2:Q2', [['Поставки Army', 'Поставки EMS', 'FZ', 'FP', 'Ганшоп', 'Победы GW', 'Поезд', 'ВЗХ', 'win cpt', 'Похищения', 'Проезд мимо', 'Мп / ГМП', 'Флаг', 'Вагонетка', '', 'Дополнительная иформация']])

lists_table = ['MG', 'FAM', 'LSV', 'BSG', 'ESB']

def add_header(list_table):
    wks = sh.worksheet(lists_table[list_table])
    wks.update('B2:Q2', [['Поставки Army', 'Поставки EMS', 'FZ', 'FP', 'Ганшоп', 'Победы GW', 'Поезд', 'ВЗХ', 'win cpt', 'Похищения', 'Проезд мимо', 'Мп / ГМП', 'Флаг', 'Вагонетка', '', 'Дополнительная иформация']])

def add_text_cell(list_table, row, col, text):
    wks = sh.worksheet(lists_table[list_table])
    wks.update_cell(row, col, text)

# for i in range(1, 11):
#     wks.update_cell(i+2, 1, f'{i+20}.01')
