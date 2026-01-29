def find_actions(input_file1, input_file2, input_file3, output_file):
    with open(input_file1, 'r', encoding='utf-8') as file1:
        lines1 = file1.readlines()

    with open(input_file2, 'r', encoding='utf-8') as file2:
        lines2 = file2.readlines()

    with open(input_file3, 'r', encoding='utf-8') as file3:
        lines3 = file3.readlines()

    nicknames = set()
    nicknames1= set()

    for line1 in lines1:
        nickname = line1.split()[5].split(']')[0].split('[')[-1]
        nicknames.add(nickname)
        nicknamenew = line1.split()[1]
        nicknames1.add(nicknamenew)
    for line3 in lines3:
        nickname = line3.split()[6].split(']')[0].split('[')[-1]
        nicknamenew = line3.split()[1]
        if nickname:
            nicknames.add(nickname)
            nicknames1.add(nicknamenew)
        print(nicknames)
        print('-------------------------')

    with open(output_file, 'w') as file:
        for line2 in lines2:
            for nickname in nicknames:
                if ('TRANSFER FROM' in line2 or 'Trade with' in line2 or 'PAY FROM') and nickname in line2:
                    file.write(line2)
                    print('-------------------------')
                    print(line2)


# Указываем пути к файлам
input_file1 = 'logs.txt'
input_file5 = input('Название лога: ')
input_file2 = f'{input_file5}.txt'
input_file3 = 'loginvite.txt'
output_file = 'logslines.txt'

# Вызываем функцию для выполнения задачи
find_actions(input_file1, input_file2, input_file3, output_file)