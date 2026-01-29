import re
def find_characters(filename, target_fractions, ignored_faction):
    result = []

    with open(filename, 'r') as file:
        lines = file.readlines()

        account_num = None
        account_characters = []

        def save_account(account_num, account_characters):
            matching_chars = [char for char in account_characters if char['faction'] in target_fractions and char['faction'] != ignored_faction]
            if matching_chars:
                result.append((account_num, account_characters))  # сохраняем данные аккаунта

        for line in lines:
            if line.startswith('ACC:'):
                if account_num is not None:
                    save_account(account_num, account_characters)

                account_num = int(line.split(':')[1].strip())
                account_characters = []
            elif line.startswith('#'):
                character = {'account_num': account_num, 'ID': None, 'nickname': None, 'faction': None, 'rank': None}  # добавляем поле 'rank' в словарь характеристик
                account_characters.append(character)
            elif line.startswith('ID:'):
                character['ID'] = int(line.split(':')[1].strip())
            elif line.startswith('Ник:'):
                character['nickname'] = line.split(':')[1].strip()
            elif line.startswith('Фракция:'):
                character['faction'] = line.split(':')[1].strip().split('(')[0].strip()
                match = re.search(r'\(rank: (\d+)\)', line)  # находим информацию о ранге
                if match:
                    character['rank'] = int(match.group(1))
                else:
                    character['rank'] = None

        if account_num is not None:
            save_account(account_num, account_characters)

    return result


def write_results_to_file(filename, matching_accounts):
    with open(filename, 'w') as file:
        if matching_accounts:
            file.write("Следующие аккаунты содержат персонажей, нарушающих правило:\n")
            for account_num, account_characters in matching_accounts:
                file.write(f"Аккаунт: {account_num}\n")
                for character in account_characters:
                    file.write(f"ID: {character['ID']}\n")
                    file.write(f"Никнейм: {character['nickname']}\n")
                    file.write(f"Фракция: {character['faction']} (rank: {character['rank']})\n")
                    file.write("------\n\n")
        else:
            file.write("Совпадений не найдено.\n")

def check_nickname_endings(matching_accounts, ignored_faction):
    high_ranked_characters = []
    endings = {
        'Итальянская Мафия': ['ossa', 'eri', 'ino', 'ini', 'ito', 'chi', 'te', 'li', 'ne', 'lo', 'no', 'o'],
        'Японская Мафия': ['sato', 'yki', 'asi', 'yra', 'ida', 'ato', 'ito', 'yti', 'aki'],
        'Мексиканская Мафия': ['ez', 'az', 'oz', 'is', 'ero', 'er', 'ona'],
        'Армянская Мафия': ['yan', 'yanc', 'yn', 'enc'],
        'Русская Мафия': ['ov', 'ev', 'v', 'ova']
    }
    with open(filename, 'r') as file:
        lines = file.readlines()
    with open(nicknamechecker, 'w') as file:
        account_num = None
        account_characters = []

        for line in lines:
            if line.startswith('ACC:'):
                if account_num is not None:
                    for character in account_characters:
                        faction = character['faction']
                        if faction == ignored_faction:  # проверка фракции на соответствие ignored_faction
                            nickname = character['nickname']
                            if faction in endings:
                                matched = False
                                for ending in endings[faction]:
                                    if nickname.endswith(ending):
                                        matched = True
                                        break
                                if not matched:
                                    file.write(f"Аккаунт: {account_num}\n")
                                    file.write(f"ID: {character['ID']}\n")
                                    file.write(f"Никнейм: {nickname}\n")
                                    file.write(f"Фракция: {character['faction']} (rank: {character['rank']})\n")
                                    file.write("------\n\n")
                account_num = int(line.split(':')[1].strip())
                account_characters = []
            elif line.startswith('#'):
                character = {'account_num': account_num, 'ID': None, 'nickname': None, 'faction': None, 'rank': None}
                account_characters.append(character)
            elif line.startswith('ID:'):
                character['ID'] = int(line.split(':')[1].strip())
            elif line.startswith('Ник:'):
                character['nickname'] = line.split(':')[1].strip()
            elif line.startswith('Фракция:'):
                character['faction'] = line.split(':')[1].strip().split('(')[0].strip()

                match = re.search(r'\(rank: (\d+)\)', line)  # находим информацию о ранге
                if match:
                    character['rank'] = int(match.group(1))
                else:
                    character['rank'] = None

        if account_num is not None:
            for character in account_characters:
                faction = character['faction']
                if faction == ignored_faction:  # проверка фракции на соответствие ignored_faction
                    nickname = character['nickname']
                    if faction in endings:
                        matched = False
                        for ending in endings[faction]:
                            if nickname.endswith(ending):
                                matched = True
                                break
                        if not matched:
                            file.write(f"Аккаунт: {account_num}\n")
                            file.write(f"ID: {character['ID']}\n")
                            file.write(f"Никнейм: {nickname}\n")
                            file.write(f"Фракция: {character['faction']} (rank: {character['rank']})\n")
                            file.write("------\n\n")

filename = input("Название отпарсенного файла : ")
target_fractions = ['Армянская Мафия', 'Medical Services', 'FIB', 'The Ballas Gang', 'Bloods', 'The Families', 'Marabunta Grande', 'Los Santos Vagos', 'LS Army', 'Мэрия ЛС', 'LSPD', 'LSSD', 'Мексиканская Мафия', 'Weazel News', 'Федеральная Тюрьма', 'Русская Мафия', 'Японская Мафия', 'Итальянская Мафия']
print("Выберите игнорируемую фракцию из списка:")
for i, fraction in enumerate(target_fractions, start=1):
    print(f"{i}. {fraction}")
selection = int(input("> "))
ignored_faction = target_fractions[selection-1]
matching_accounts = find_characters(filename, target_fractions, ignored_faction)
output_file = input("Введите название итогового файла: ")
nicknamechecker = input("Введите название файла с никнеймами: ")
write_results_to_file(output_file, matching_accounts)
check_nickname_endings(matching_accounts, ignored_faction)