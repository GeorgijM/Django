import random

from django.shortcuts import render
from django import forms


class UserForm(forms.Form):
    number = forms.IntegerField(label="Ваше число")


def index(request):
    global input_value
    userform = UserForm()
    if request.method == "POST":
        input_value = request.POST.get("number")
        print(f'{input_value=}')
        print(randomizer())

#         line_1 = """<p><span style="background-color:rgb(178, 34, 34)">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<span style="background-color:#A52A2A">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span></p>
# """
#         line_2 = """<p><span style="background-color:rgb(178, 34, 34)">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span></p>
# """
        idzin_pack = []
        line_1 = set_line(randomizer())
        idzin_pack.append(value_generated)
        line_2 = set_line(randomizer())
        idzin_pack.append(value_generated)
        line_3 = set_line(randomizer())
        idzin_pack.append(value_generated)
        line_4 = set_line(randomizer())
        idzin_pack.append(value_generated)
        line_5 = set_line(randomizer())
        idzin_pack.append(value_generated)
        line_6 = set_line(randomizer())
        idzin_pack.append(value_generated)
        idzin_number = ''.join(map(str, idzin_pack))
        print(f'{idzin_pack=}')
        print(f'{idzin_number=}')
        # print(f'{dict_idzin['111111']=}')
        print(dict_idzin['111111'])


        context = {"form": userform, "input_value": input_value, "line_1": line_1, "line_2": line_2, "line_3": line_3,
                   "line_4": line_4, "line_5": line_5, "line_6": line_6, "dict_idzin": dict_idzin }
        return render(request, "index.html", context)
    return render(request, "index.html", {"form": userform})


def randomizer():
    global value_generated
    random_int = random.randint(1, 1000)
    random_int2 = random.randint(1, 1000)
    print(f'{random_int=}')
    value_generated = (int(input_value) * random_int + random_int2) % 2
    return  value_generated

def set_line(flag):
    # randomizer()
    # print(value_generated)
    line = """<p><span style="background-color:rgb(178, 34, 34)">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span></p>
    """
    line_line = """<p><span style="background-color:rgb(178, 34, 34)">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span>&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;<span style="background-color:#A52A2A">&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;</span></p>
    """
    if flag == 0:
        set_line = line_line
    else:
        set_line = line
    return set_line



codes_idzin = {
"111111" : "Творчество (Цянь)",
"000000" : "Исполнение (Кунь)",
"010001" : "Тунь (“Стяжательство”)",
"100010" : "Мэн (“Незрелость”, “Невежество”)",
"010111" : "Сюй (“Выжидание”)",
"111010" : "Сун (“Спор”, “Обличение”)",
"000010" : "Ши (“Войско”)",
"010000" : "Би (“Близость”)",
"110111" : "Сяо чу (“Малое воспитание”)",
"111011" : "Ли (“Поступок”, “Наступление”)",
"000111" : "Тай (“Процветание”)",
"111000" : "Пи (“Упадок”)",
"111101" : "Тун жэнь (“Содружество”, “Союзники”)",
"101111" : "Да ю (“Большое владение”)",

"000100" : "Цянь (“Уступчивость”, “Кротость”)"
"001000" : "Юй (“Беспечность”)"
"011001" : "Суй (“Следование”)"
"100110" : "Гу (“Порча”)"
"000011" : "Линь (“Вторжение”, “Посещение”)"
"110000" : "Гуань (“Рассматривание”, Наблюдение”)"
"101001" : "Ши хо (“Раскусывание”)"
"100101" : "Би (“Светлость”, “Красота”, “Украшение”)"
"100000" : "Бо (“Разрушение”)"
"000001" : "Фу (“Возврат”)"
"111001" : "У ван (“Непроизвольность”)"
"100111" : "Да чу (“Великое воспитание”)"
"100001" : "И (“Питание”, “Челюсти”)"
"011110" : "Да го (“Большой переход”)"
"010010" : "Кань ("Повторная опасность")"
"101101" : "Ли ("Сияние")"
"011100" : "Сянь (“Взаимодействие”, “Приспосабливание”)"
"001110" : "Хэн (“Неподвижность”, “Постоянство”)"
"111100" : "Дунь (“Уход”, “Бегство”)"
"001111" : "Да чжуан (“Великая сила”)"
"101000" : "Цзинь (“Выпячивание”, “Восход”)"
"000101" : "Мин и (“Помрачение”, “Угасание света”)"
"110101" : "Цзя жэнь (“Семья”)"
"101011" : "Куй (“Отстранение”)"
"010100" : "Цзянь (“Препятствие”)"
"001010" : "Цзе (“Разнузданность”, “Освобождение”)"
"100011" : "Сунь (“Убыток”)"
"110001" : "И (“Прибыль”)"
"011111" : "Гуай (“Решимость”)"
"111110" : "Гоу (“Встреча”)"
"011000" : "Цуй (“Сборище”, “Скопление”)"
"000110" : "Шэн (“Подъем”)"
"011010" : "Кунь (“Изнеможение”, “Истощение”)"
"010110" : "Цзин (“Колодец”)"
"011101" : "Гэ (“Обновление”, “Смена”)"
"101110" : "Дин (“Треножник”)"
"001001" : "Чжэнь ("Молния")"
"100100" : "Гэнь ("Сосредоточенность")"
"110100" : "Цзянь (“Неспешность”, “Течение”)"
"001011" : "Гуй мэй (“Невеста”)"
"001101" : "Фэн (“Изобилие”)"
"101100" : "Люй (“Странствие”)"
"110110" : "Сунь ("Проникновение")"
"011011" : "Дуй ("Радость")"
"110010" : "Хуань (“Распад”)"
"010011" : "Цзе (“Ограничение”)"
"110011" : "Чжун фу (“Верность срединности”)"
"001100" : "Сяо го (“Малый переход”)"
"010101" : "Цзи цзи (“Завершенность”)"
"101010" : "Вэй цзи (“Незавершенность”)"


}
