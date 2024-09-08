def decoder(number1=int(input('введите число от 3 до 20: '))):
    password = []
    for i in range(1, number1):
        for g in range(i, number1):
            if i == g:
                continue
            summ = i + g
            if summ == number1 or number1 % summ == 0:
                password += i, g
            else:
                continue
    return password



qwe = decoder()
print(*qwe)
