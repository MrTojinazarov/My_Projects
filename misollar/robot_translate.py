def check_nums(num):
    data = []
    result = ""
    for i in num:
        if i == 0 and i.isdigit():
           result = result + i
        else:
            while num:
                a = int(num % 2)
                num =num // 2
                data.append(a)

            data = data[::-1]
            result = ''.join(map(str, data))
            return result

num = str(input("num = "))

print(check_nums(num))