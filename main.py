vento = -1
temperatura = 0
class_temperatura = ''
umidade = 0
class_umidade = ''
def vel_vento():
    global vento

    while vento not in[0,1]:
        escolha = int(input('Qual a velocidade do vento?\n1 - Forte \n2 - Fraco '))
        match escolha:
            case 1:
                vento = 1
            case 2:
                vento = 0
            case _:
                print('Escolha uma opção válida!')

def def_temperatura():
    global temperatura
    global class_temperatura
    temperatura = float(input('Digite a temperatura(Ex: 25): '))

    if temperatura > 26:
        class_temperatura = 'Quente'
    elif temperatura <= 26 and temperatura > 20:
        class_temperatura = ('Ameno')
    elif temperatura <= 20 and temperatura > 15:
        class_temperatura = ('Fresco')
    elif temperatura <= 15:
        class_temperatura = ('Frio')

def def_umidade():
    global umidade
    global class_umidade
    umidade = float(input('Digite a umidade: '))
    if umidade >= 95:
        class_umidade = 'Elevada'
    elif umidade < 95 and umidade >= 70:
        class_umidade = 'Normal'
    elif umidade < 70:
        class_umidade = 'Fraca'

def JogarTenis():
    global class_temperatura
    global class_umidade
    global vento


    if class_temperatura == 'Quente' and class_umidade == 'Elevada' and vento == 1:
        print('Você não deve ir jogar tênis')
    elif class_temperatura == 'Quente' and class_umidade == 'Elevada' and vento == 0:
        print('Você deve ir jogar tênis')
    elif class_temperatura == 'Ameno' and class_umidade == 'Elevada' and vento == 0:
        print('Você deve ir jogar tênis')
    elif class_temperatura == 'Fresco' and class_umidade == 'Normal' and vento == 0:
        print('Você deve ir jogar tênis')
    elif class_temperatura == 'Fresco' and class_umidade == 'Normal' and vento == 1:
        print('Você não deve ir jogar tênis')
    elif class_temperatura == 'Ameno' and class_umidade == 'Normal' and vento == 0:
        print('Você deve ir jogar tênis')
    elif class_temperatura == 'Ameno' and class_umidade == 'Elevada' and vento == 1:
        print('Você não deve ir jogar tênis')
    elif class_temperatura == 'Quente' and class_umidade == 'Normal' and vento == 0:
        print('Você deve ir jogar tênis')
    else:
        print('Você não deve ir jogar tênis')

vel_vento()
def_temperatura()
def_umidade()
JogarTenis()