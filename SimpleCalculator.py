import PySimpleGUI as sg

#Create a layout with tectbox and all buttons
layout = [[sg.Input(size=(10,8),key='-Display-',justification='Right')],
          [sg.Button(1),sg.Button(2),sg.Button(3),sg.Button('+')]
          ,[sg.Button(4),sg.Button(5),sg.Button(6),sg.Button('-')]
          ,[sg.Button(7),sg.Button(8),sg.Button(9),sg.Button('*')]
          ,[sg.Button('C'),sg.Button(0),sg.Button('='),sg.Button('/')]
          ,[sg.Button('Exit',size=(10,1),pad=(10,0))]]

window=sg.Window('Calculator',layout)
display =''

while True:
    event,value=window.read()
    try:
        if event == sg.WINDOW_CLOSED or event == 'Exit':
            break
        elif event in '1234567890':
            display += event
            window['-Display-'].update(display)
        elif event in '+-*/':
            display = str(eval(display))
            window['-Display-'].update(display)
            display += event
            window['-Display-'].update(display)
        elif event =='=':
            result = eval(display)
            window['-Display-'].update(result)
        elif event =='C':
            display=''
            window['-Display-'].update(display)
    except ZeroDivisionError:
        display=0
        window['-Display-'].update(display)
        display=''

print(type(display))