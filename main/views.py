from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def genres(request):
    genres_list = [
        {
            'id': 1,
            'name_en': 'Pop',
            'name_ru': 'Поп',
            'description': 'Мелодичная музыка с простой структурой, ориентированная на массового слушателя.'
        },
        {
            'id': 2,
            'name_en': 'Rock',
            'name_ru': 'Рок',
            'description': 'Музыка с акцентом на электрогитару, ударные и энергичный ритм.'
        },
        {
            'id': 3,
            'name_en': 'Hip-Hop',
            'name_ru': 'Хип-хоп',
            'description': 'Стиль, основанный на ритмичном речитативе под биты и сэмплы.'
        },
        {
            'id': 4,
            'name_en': 'Electronic',
            'name_ru': 'Электронная',
            'description': 'Музыка, созданная с помощью электронных инструментов и синтезаторов.'
        },
        {
            'id': 5,
            'name_en': 'Jazz',
            'name_ru': 'Джаз',
            'description': 'Музыка, характеризующаяся импровизацией и сложной гармонией.'
        },
    ]

    return render(request, 'genres.html', {'genres': genres_list})