import PySimpleGUI as sg

def add_remove_linha():
    lista =

    coluna = sg.Column(
        [[sg.pin(sg.Frame('', [[
            sg.T(str(i)),sg.Combo(lista, ), sg.Spin([i for i in range(1,11)], initial_value=1, size=(3,1)), sg.Ok()]],
            key=str(i), visible=False))] for i in range(10)],
        scrollable=True, vertical_scroll_only=True, size=(300, 330))
    layout = [[coluna]] + [[sg.Button('Adicionar', key='-B1-')] + [sg.Button('Remover', key='-B2-')]]


    window = sg.Window('Produtos', layout)
    i = 1
    while True:  # Event Loop
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        if event == '-B1-':
            if i > 9:
                i = 9
            window[str(i)](visible=True)
            i += 1
            coluna.contents_changed()
        if event == '-B2-':
            i -= 1
            if i < 0:
                i = 0
            window[str(i)](visible=False)
            coluna.contents_changed()
        print(values, event)
    window.close()

