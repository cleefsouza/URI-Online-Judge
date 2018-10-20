import re

while True:
    try:
        old_str = input()
        old_str = old_str.replace("\n"," ")
        new_str = re.sub('[^a-zA-Z0-9 .]', '', re.sub(r'\.\b', ' ', old_str))
        new_str = new_str.split(" ")
        new_list = []

        for x in new_str:
            x = x.replace(".","")
            new_list.append(x.lower())

        new_list.sort()

        for y in new_list:
            print(y)

    except EOFError:
        break
