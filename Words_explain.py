meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное",
            "ЛОЛ": "Что-то очень смешное",
            'ХЗ': 'Не знаю',
            'ПЖ': 'Пожалуйста'
            }
count = 0
while count <= 4:
    word = input('Введите непонятное слово (болшими буквами!)')
    if word in meme_dict.keys():
        print(meme_dict[word])
        count += 1
    else:
        print('Такого слово в словаре нет')
        count += 1
