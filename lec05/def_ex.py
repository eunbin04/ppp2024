def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)

def hello(name):
    print(f"{colored(255, 0, 0, name)}님 안녕하세요.".format(name))


print(colored(0, 255, 0, 'Hello, World'))
hello("홍길동")

#에러