import tkinter as tk
from tkinter import simpledialog

window = tk.Tk()
window.withdraw()

def gui_input(text: str) -> str:
    return simpledialog.askstring(title="입력", prompt=text)

def get_chosung(text):
    Chosung_list=['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    chosung=[]
    for gulja in text:
        chosung.append(Chosung_list[(ord(gulja)-ord('가'))//588])
    return chosung

def main():

    hidden_answer=gui_input("초성퀴즈로 출제할 단어를 입력해주세요:")
    problem=get_chosung(hidden_answer)
    print(f"문제입니다. 주어진 초성은 '{''.join(problem)}'입니다.")

    answer=gui_input("답은=>")
    if answer==hidden_answer:
        print("정답입니다!")
    else:
        print("틀렸습니다. 답은 {hidden_answer}입니다.")

if __name__ == "__main__":
    main()