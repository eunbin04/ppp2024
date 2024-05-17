def toggle_text(text:str)->str:
    text_list=[]
    for alp in text:
        if ord(alp)<=90:
            small=chr(ord(alp)+32)
            text_list.append(small)
        if ord(alp)>90:
            big=chr(ord(alp)-32)
            text_list.append(big)
    return text_list

def main():
    text=input("변환할 문자를 입력하시오:")
    print(f"{''.join(toggle_text(text))}")

if __name__== "__main__":
    main()