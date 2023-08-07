import PySimpleGUI as sg

#Modificaveis
Money = 10000
Guardado = 0

#investimentos
Vmaçã = 0
Vlimão = 0
Vapartamento = 0
Vfutebol_team = 0
Vlava_jato = 0

Investidos = 0

#rendimento bancario
Depositando = 0
Vrendimentos = 0

#lucros
lucros = 0

#janela 1
def Carteira():
    sg.theme('BrownBlue')
    layout = [
        [sg.Text('Dinheiro', size=(10, 2)), sg.Text(f'R$ {Money:.2f}', size=(20, 2))],
        [sg.Text('Depositado', size=(10, 2)), sg.Text(f'R$ {Guardado:.2f}', size=(20, 2))],
        [sg.Text('Investido', size=(10, 2)), sg.Text(f'R$ {Investidos:.2f}', size=(20, 2))],
        [sg.Button('Comprar'), sg.Button('Vender'), sg.Button('Investimentos'), sg.Button('Banco'), sg.Button('Falência')],
    ]
    return sg.Window('Marcinho Wallet', layout=layout, finalize=True)

#janela 2
def Compras():
    sg.theme('Dark')
    layout = [
        [sg.Button('Maçã', size=(10, 3)), sg.Button('limão', size=(10, 3)), sg.Button('apartamento', size=(10, 3))],
        [sg.Button('time de futebol', size=(10, 3)), sg.Button('lava jato', size=(10, 3))],
        [sg.Button('Voltar', size=(10, 3))],
    ]
    return sg.Window('Mercadão do Marcão', layout=layout, finalize=True)

#janela 3
def Vendas():
    sg.theme('Dark')
    layout = [
        [sg.Button('Maçã', size=(10, 3)), sg.Button('limão', size=(10, 3)), sg.Button('apartamento', size=(10, 3))],
        [sg.Button('time de futebol', size=(10, 3)), sg.Button('lava jato', size=(10, 3))],
        [sg.Button('Voltar', size=(10, 3))],
    ]
    return sg.Window('Vendinha da Lurdes', layout=layout, finalize=True)

#janela 4
def Investimentos():
    sg.theme('Dark')
    layout = [
        [sg.Text('maça', size=(10, 2)), sg.Text(f'{Vmaçã}', size=(20, 2)), sg.Text(f'R$ {Imaçã:.2f}', size=(20, 2))],
        [sg.Text('limão', size=(10, 2)), sg.Text(f'{Vlimão}', size=(20, 2)), sg.Text(f'R$ {Ilimão:.2f}', size=(20, 2))],
        [sg.Text('apartamentos', size=(10, 2)), sg.Text(f'{Vapartamento}', size=(20, 2)), sg.Text(f'R$ {Iapartamento:.2f}', size=(20, 2))],
        [sg.Text('Times', size=(10, 2)), sg.Text(f'{Vfutebol_team}', size=(20, 2)), sg.Text(f'R$ {Ifutebol_team:.2f}', size=(20, 2))],
        [sg.Text('lava jatos', size=(10, 2)), sg.Text(f'{Vlava_jato}', size=(20, 2)), sg.Text(f'R$ {Ilava_jato:.2f}', size=(20, 2))],
        [sg.Button('Voltar'), sg.Button('Teste')],
    ]
    return sg.Window('Posses', layout=layout, finalize=True)

#janela 5
def Banco():
    sg.theme('Green')
    layout = [
        [sg.Text('Depositar', size=(10, 0)), sg.Button('R$ -50'), sg.Button('R$ -100'), sg.Button('R$ -500'), sg.Button('R$ -1.000')],
        [sg.Text('Retirar', size=(10, 0)), sg.Button('R$ +50'), sg.Button('R$ +100'), sg.Button('R$ +500'), sg.Button('R$ +1.000')],
        [sg.Text('Rendimentos', size=(10, 0)), sg.Text(f'R$ {Vrendimentos}')],
        [sg.Button('Voltar', size=(7, 2))],
        [sg.Output(size=(30, 15))]
    ]
    return sg.Window('BancoNU', layout=layout, finalize=True)

janela1, janela2, janela3, janela4, janela5 = Carteira(), None, None, None, None
while True:
    window, event, values = sg.read_all_windows()

    Imaçã = Vmaçã * 0.30
    Ilimão = Vlimão * 0.60
    Iapartamento = Vapartamento * 800
    Ifutebol_team = Vfutebol_team * 1300
    Ilava_jato = Vlava_jato * 950

    Investidos = (Imaçã + Ilimão + Iapartamento + Ifutebol_team + Ilava_jato)

    #Se a janela for fechada
    if event == sg.WIN_CLOSED:
        break
    if event == 'Falência':
        sg.popup('Faliu maluco, não tankou')
        break

    #voltar
    if window == janela2 and event == "Voltar":
        janela1 = Carteira()
        janela2.hide()
    if window == janela3 and event == "Voltar":
        janela1 = Carteira()
        janela3.hide()
    if window == janela4 and event == "Voltar":
        janela1 = Carteira()
        janela4.hide()
    if window == janela5 and event == "Voltar":
        janela1 = Carteira()
        janela5.hide()




    #Janela1 - Carteira
    if window == janela1 and event == 'Comprar':
        janela1.hide()
        janela2 = Compras()
    if window == janela1 and event == 'Vender':
        janela1.hide()
        janela3 = Vendas()
    if window == janela1 and event == 'Investimentos':
        janela1.hide()
        janela4 = Investimentos()
    if window == janela1 and event == 'Banco':
        janela1.hide()
        janela5 = Banco()

    #Janela2 - Compras
    if window == janela2 and event == 'Maçã' and Money >= 0.30: #não pode ficar negativo
        Vmaçã += 1
        Money -= 0.30
    if window == janela2 and event == 'limão' and Money >= 0.60:
        Vlimão += 1
        Money -= 0.60
    if window == janela2 and event == 'apartamento' and Money >= 800:
        Vapartamento += 1
        Money -= 800
    if window == janela2 and event == 'time de futebol' and Money >= 1300:
        Vfutebol_team += 1
        Money -= 1300
    if window == janela2 and event == 'lava jato' and Money >= 950:
        Vlava_jato += 1
        Money -= 950

    #janela3 - Vendas
    if window == janela3 and event == 'Maçã' and Vmaçã >=1:
        Vmaçã -= 1
        Money += 0.30
    if window == janela3 and event == 'limão' and Vlimão >=1:
        Vlimão -= 1
        Money += 0.60
    if window == janela3 and event == 'apartamento' and Vapartamento >=1:
        Vapartamento -= 1
        Money += 800
    if window == janela3 and event == 'time de futebol' and Vfutebol_team >=1:
        Vfutebol_team -= 1
        Money += 1300
    if window == janela3 and event == 'lava jato' and Vlava_jato >=1:
        Vlava_jato -= 1
        Money += 950

    #janela 4 - Investimentos
    #observação

    #janela5 - Banco
    #Depositos
    if window == janela5 and event == 'R$ -50':
        if Money >= 50:
            Money -= 50
            Guardado += 50
            print('Você depositou 50 conto')
        else:
            print(f'Você não tem dinheiro o suficiente, Saldo Atual R$ {Money:.2f}')
    if window == janela5 and event == 'R$ -100':
        if Money >= 100:
            Money -= 100
            Guardado += 100
            print('Você depositou 100 conto')
        else:
            print(f'Você não tem dinheiro o suficiente, Saldo Atual R$ {Money:.2f}')
    if window == janela5 and event == 'R$ -500':
        if Money >= 500:
            Money -= 500
            Guardado += 500
            print('Você depositou 500 conto')
        else:
            print(f'Você não tem dinheiro o suficiente, Saldo Atual R$ {Money:.2f}')
    if window == janela5 and event == 'R$ -1.000':
        if Money >= 1000:
            Money -= 1000
            Guardado += 1000
            print('Você depositou 1000 conto')
        else:
            print(f'Você não tem dinheiro o suficiente, Saldo Atual R$ {Money:.2f}')

    #Retirados
    if window == janela5 and event == 'R$ +50' and Guardado >= 50:
        Money += 50
        Guardado -= 50
    if window == janela5 and event == 'R$ +100' and Guardado >= 100:
        Money += 100
        Guardado -= 100
    if window == janela5 and event == 'R$ +500' and Guardado >= 500:
        Money += 500
        Guardado -= 500
    if window == janela5 and event == 'R$ +1.000' and Guardado >= 1000:
        Money += 1000
        Guardado -= 1000
