
#define as regras conforme a tabela passada no classroom em um dicionario de dados
regras = {
    ('Quente', 'Elevada', 1): 'Não',
    ('Quente', 'Elevada', 0): 'Sim',
    ('Ameno', 'Elevada', 0): 'Sim',
    ('Fresco', 'Normal', 0): 'Sim',
    ('Fresco', 'Normal', 1): 'Não',
    ('Ameno', 'Normal', 0): 'Sim',
    ('Ameno', 'Elevada', 1): 'Não',
    ('Quente', 'Normal', 0): 'Sim',

}

def vel_vento(vento):


    while vento not in [0,1]:
        escolha = int(input('Qual a velocidade do vento?\n1 - Forte \n2 - Fraco '))
        match escolha:
            case 1:
                vento = 1
            case 2:
                vento = 0
            case _:
                print('Escolha uma opção válida!')
    return vento

def def_temperatura():

    temperatura = float(input('Digite a temperatura(Ex: 25): '))

    if temperatura > 26:
        class_temperatura = 'Quente'
    elif temperatura <= 26 and temperatura > 20:
        class_temperatura = 'Ameno'
    elif temperatura <= 20 and temperatura > 15:
        class_temperatura = 'Fresco'
    elif temperatura <= 15:
        class_temperatura = 'Frio'

    return class_temperatura

def def_umidade():

    umidade = float(input('Digite a umidade: '))

    if umidade >= 95:
        class_umidade = 'Elevada'
    elif umidade < 95 and umidade >= 70:
        class_umidade = 'Normal'
    elif umidade < 70:
        class_umidade = 'Fraca'

    return class_umidade

def jogar_tenis(class_temperatura, class_umidade, vento):

    chave = (class_temperatura, class_umidade, vento)
    resultado = regras.get(chave, 'Não')

    if resultado == 'Sim':
        print('Você deve ir jogar tênis')
    else:
        print('Você não deve ir jogar tênis')


v_vento = vel_vento(-1)
temp = def_temperatura()
umid = def_umidade()
jogar_tenis(temp, umid, v_vento)