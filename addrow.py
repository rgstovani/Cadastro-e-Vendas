import PySimpleGUI as sg

def add_remove_linha():
    lista = 'Produto1', 'Produto2'

    coluna = sg.Column(
        [[sg.pin(sg.Frame('', [[
            sg.T(str(i)),sg.Combo(lista, ), sg.Spin([i for i in range(1,11)], initial_value=1, size=(3,1))]],
            key=str(i), visible=False))] for i in range(10)],
        scrollable=True, vertical_scroll_only=True, size=(300, 330))
    layout = [[coluna]] + [[sg.Button('+ Linha', key='-addlinha-')] + [sg.Button('- Linha', key='-removelinha-')] + [sg.Push()] + [sg.Button('Adicionar')]]


    window = sg.Window('Produtos', layout)
    i = 1
    while True:  # Event Loop
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        if event == '-addlinha-':
            if i > 9:
                i = 9
            window[str(i)](visible=True)
            i += 1
            coluna.contents_changed()
        if event == '-removelinha-':
            i -= 1
            if i < 0:
                i = 0
            window[str(i)](visible=False)
            coluna.contents_changed()
        print(values, event)
    window.close()

add_remove_linha()

