def num_of_words(file_contents):
    x = file_contents.split()
    return len(x)

def get_chars_dict(file_contents):
    chars = {}
    for c in file_contents:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sort_dict(dic):
    # Create a list of dictionaries and sort it by count in descending order
    sorted_list = [{"char": k, "num": v} for k, v in dic.items() if k.isalpha()]
    sorted_list.sort(key=lambda x: x["num"], reverse=True)
    return sorted_list
