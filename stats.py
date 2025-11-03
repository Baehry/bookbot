def number_of_words(text):
    return len(text.split())

def num_of_char(text):
    d = {}
    for c in text:
        if c.lower() in d:
            d[c.lower()] += 1
        else:
            d[c.lower()] = 1
    return d

def sort_dict(d):
    dict_list = []
    for character in d:
        dict_list.append({
            "char": character,
            "num": d[character]
        })
    dict_list.sort(key=sort_on, reverse=True)
    return dict_list

def sort_on(items):
    return items["num"]