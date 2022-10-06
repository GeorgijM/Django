import random
from django.shortcuts import render
from django import forms
from .models import Idzin


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

        hexagram_code = Idzin.objects.get(code_idzin=idzin_number)
        print(f'{hexagram_code=}')
        print(f'{hexagram_code.code_idzin=}')
        print(f'{hexagram_code.name=}')
        print(f'{hexagram_code.description=}')

        name = hexagram_code.name
        description = hexagram_code.description

        context = {"form": userform, "input_value": input_value, "line_1": line_1, "line_2": line_2, "line_3": line_3,
                   "line_4": line_4, "line_5": line_5, "line_6": line_6, "name": name, "description": description}
        return render(request, "index.html", context)
    return render(request, "index.html", {"form": userform})


def randomizer():
    global value_generated
    random_int = random.randint(1, 1000)
    random_int2 = random.randint(1, 1000)
    print(f'{random_int=}')
    value_generated = (int(input_value) * random_int + random_int2) % 2
    return value_generated


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
