import PySimpleGUI as sg
from classeIMC import IMC

linha0 = [sg.Text('Qual sua altura?'), sg.InputText('', key='altura'), sg.Text("cm")]
linha1 = [sg.Text('Qual seu peso?'), sg.InputText('', key='peso'), sg.Text("Kg")]
linha2 = [sg.Text('Seu IMC é: '), sg.Text('', key='imc')]
linha3 = [sg.Button('Calcular IMC', bind_return_key=True)]
container = [linha0, linha1, linha2, linha3]

janela = sg.Window('Calculadora de IMC', container)

while True:
    evento, valores = janela.Read()
    
    if evento == 'Calcular IMC':
        try:
            imc = IMC(float(valores['peso']), float(valores['altura']))
            print(imc.get_classificacao())
            janela['imc'].Update("{:.2f} - {}".format(imc.get_imc(), imc.get_classificacao()))
        except:
            sg.Popup('Erro', 'Peso e altura devem ser números!')

    if evento == sg.WIN_CLOSED:
        break

janela.Close()