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
                character = {'account_num': account_num, 'ID': None, 'nickname': None, 'faction': None}
                account_characters.append(character)
            elif line.startswith('ID:'):
                character['ID'] = int(line.split(':')[1].strip())
            elif line.startswith('Ник:'):
                character['nickname'] = line.split(':')[1].strip()
            elif line.startswith('Фракция:'):
                character['faction'] = line.split(':')[1].strip().split('(')[0].strip()

        if account_num is not None:
            save_account(account_num, account_characters)

    return result

filename = 'rm.txt'
target_fractions = ['Армянская Мафия', 'Medical Services', 'FIB', 'The Ballas Gang', 'Bloods', 'The Families', 'Marabunta Grande', 'Los Santos Vagos', 'LS Army', 'Мэрия ЛС', 'LSPD', 'LSSD', 'Мексиканская Мафия', 'Weazel News', 'Федеральная Тюрьма', 'Русская Мафия', 'Японская Мафия', 'Итальянская Мафия']
ignored_faction = 'Русская Мафия'
matching_accounts = find_characters(filename, target_fractions, ignored_faction)

if matching_accounts:
    print("Следующие аккаунты содержат персонажей, нарушающих правило в отношении фракций:", target_fractions, "за исключением фракции", ignored_faction)
    for account_num, account_characters in matching_accounts:
        print(f"Аккаунт: {account_num}")
        for character in account_characters:
            print(f"ID: {character['ID']}")
            print(f"Никнейм: {character['nickname']}")
            print(f"Фракция: {character['faction']}")
            print("------")
else:
    print("Совпадений не найдено.")