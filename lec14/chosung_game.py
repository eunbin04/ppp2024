def get_chosung(text):
    Chosung_list=['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅅ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ' 'ㅍ','ㅎ']

    chosung=[]
    for gulja in text:
        #print(gulja, (ord(gulja)-ord('가'))//588, (ord(gulja)-ord('가'))%588)
        chosung.append(Chosung_list[(ord(gulja)-ord('가'))//588])

    return "ㅍㅇㅅ"

def main():

    hidden_answer="스마트팜"
    problem=get_chosung(hidden_answer)
    print(f"문제입니다. 주어진 초성은 '{''.join(problem)}'입니다.")

    # answer=input("답은=>")
    # if answer==hidden_answer:
    #     print("정답입니다!")
    # else: 
    #     print("틀렸습니다. 다시 생각해보세요.")


if __name__ == "__main__":
    main()