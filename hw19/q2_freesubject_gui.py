import PySimpleGUI as sg

sg.theme('DarkAmber')

layout=[ [sg.Text('알고 있는 삼각형의 각도 1 =>'), sg.InputText()],
         [sg.Text('알고 있는 삼각형의 각도 2 =>'), sg.InputText()],
         [sg.Button('확인'), sg.Button('취소')],
         [sg.Text('결과 =>'), sg.Output(size=(60, 5))]]
window = sg.Window('삼각형의 나머지 한 각을 구하기', layout)


def tri_angle(first_angle:int, second_angle:int)->int:
    if first_angle+second_angle<180:
        last_angle=180-(first_angle+second_angle)
        return last_angle
    else:
        return "존재할 수 없는 삼각형입니다."

def main():
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '취소':
            break
        first_angle=int(values[0])
        second_angle=int(values[1])
        result=(tri_angle(first_angle, second_angle))
        print(f"알고 있는 각도: {values[0]}º, {values[1]}º  나머지 각도: {result}º")
    window.close()

if __name__== "__main__":
    main()