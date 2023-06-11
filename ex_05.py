def custom_split(text: str, split_symbol: str = "") -> list:
    result = []
    temp_str = ''
    for i in text:
        if i == split_symbol:
            result.append(temp_str)
            temp_str = ''
        temp_str += i
        
    return result  

lorem = "Amet jfnfn\nnn  jhfjkfdkdk\nkd \njffkkff"

print(custom_split(lorem, "\n"))      