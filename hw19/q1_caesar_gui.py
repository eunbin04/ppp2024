import PySimpleGUI as sg

sg.theme('DarkAmber')

layout=[ [sg.Text('카이사르 암호로 변환할 문자 =>'), sg.InputText()],
         [sg.Text('이동할 칸 수 =>'), sg.InputText()],
         [sg.Button('확인'), sg.Button('취소')],
         [sg.Text('변환된 값 =>'), sg.Output(size=(40, 5))]]
window = sg.Window('카이사르 암호', layout)


def caesar_encode(text:str, shift:int)->str:
    text_list=[]
    for alp in text:
            if ord(alp)+shift>90 and ord(alp)+shift<97:
                code=chr(ord(alp)-26+shift)
                text_list.append(code)
            elif ord(alp)+shift>122:
                code=chr(ord(alp)-26+shift)
                text_list.append(code)
            else:
                code=chr(ord(alp)+shift)
                text_list.append(code)
    return ''.join(text_list)

def main():
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '취소':
            break
        text=(values[0])
        shift=int(values[1])
        result=(caesar_encode(text, shift))
        print(f"변환할 문자:{values[0]}, 변환된 문자:{result}")
    window.close()

if __name__== "__main__":
    main()