import PySimpleGUI as sg

sg.theme('DarkAmber')

layout=[ [sg.Text('하고 싶은 말을 적어보세요.')],
         [sg.Text('입력 =>'), sg.InputText()],
         [sg. Button('확인'), sg.Button('취소')]]

window = sg.Window('입력창', layout)

while True:
    event, values=window.read()
    if event==sg.WIN_CLOSED or event=='취소':
        break
    print(f'당신은 {values[0]}라고 입력했습니다.')
window.close()