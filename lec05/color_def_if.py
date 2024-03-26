def colored_name(name, text):
    if name=='red':
        return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(255, 0, 0, text)
    elif name=='blue':
        return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(0, 0, 255, text)
    
print(colored_name('red', 'red'))
print(colored_name('blue', 'blue'))