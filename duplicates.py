text = 'Indivisibilitiesd'

def duplicate_count(text):
    text = text.lower()
    text_lenght = len(text) - 1
    counter = 0
    k = 0
    check_list = []
    while k < len(text) - 1:
        l = 1 
        while l < len(text):
            if k == l:
                l = l + 1
            elif ord(text[k].upper()) == ord(text[0 + l].upper()):
                if text[k] not in check_list:
                    check_list.append(text[k])
                    counter = counter + 1
                l = l + 1
            else:
                l = l + 1
        k = k + 1

    return counter

print(duplicate_count(text))
