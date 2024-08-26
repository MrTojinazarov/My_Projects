def UpdateStrToInt(str_data: str):
    
    res = str()

    for i in range(len(str_data)-1):
        if str_data[i].isdigit() or str_data[i] == '-':
            res = res+str_data[i]
            if not str_data[i+1].isdigit():
                return int(res)
    
    if str_data[len(str_data)-1].isdigit():
            res = res+str_data[len(str_data)-1]

    if res == "":
         res = 0

    return int(res)


str_data = input("str_data = ")

result = UpdateStrToInt(str_data)
print(result)