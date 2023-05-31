lorem = "Amet jfnfnnn  jhfjkfdkdkkd jffkkff"

lorem_up = lorem.upper()

print(lorem_up)
print(lorem)

find_l = lorem.find('m'.upper())

if find_l >= 0:
    print(f"""Find in position {find_l}""")
else:
    print("Not find")    