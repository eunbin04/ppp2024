import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.withdraw()

def gui_input(text: str) -> str:
    return simpledialog.askstring(title="입력", prompt=text)

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
    return text_list

def main():
    text=gui_input("변환할 문자를 입력하시오:")
    shift=int(gui_input("몇 칸을 이동할 지 입력하시오:"))
    print(f"{''.join(caesar_encode(text, shift))}")

if __name__== "__main__":
    main()